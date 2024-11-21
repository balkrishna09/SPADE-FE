import os
import random
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd


# SPADE Implementation
class SPADE:
    def __init__(self, security_param=64):  # Reduced security param for debugging
        self.security_param = security_param
        self.msk = None
        self.mpk = None

    def setup(self, num_users):
        """Generate master secret key and master public key."""
        self.msk = [random.randint(1, 2 ** self.security_param - 1) for _ in range(num_users)]
        self.mpk = [pow(2, key, 2 ** self.security_param - 1) for key in self.msk]
        # Ensure no zero values in mpk
        if any(val == 0 for val in self.mpk):
            raise ValueError("Generated invalid public key (mpk) with zero value.")
        return self.msk, self.mpk

    def encrypt(self, data, user_key):
        """Encrypt data using the user's private key and master public key."""
        encrypted_data = []
        for value in data:
            noise = random.randint(1, 10)
            cipher = ((value + noise) * user_key) % self.mpk[0]
            encrypted_data.append((cipher, noise))  # Store noise with cipher for decryption
        return encrypted_data

    def key_derivation(self, user_index):
        """Derive decryption key for a specific user."""
        return self.msk[user_index]

    def decrypt(self, encrypted_data, user_key):
        """Decrypt data using the derived decryption key."""
        decrypted_data = []
        for cipher, noise in encrypted_data:
            value = ((cipher // user_key) - noise) % self.mpk[0]
            decrypted_data.append(value)
        return decrypted_data


# Data Handling and Processing
def read_hypnogram_data(file_path):
    """Read Hypnogram dataset from file."""
    with open(file_path, 'r') as file:
        data = [int(line.strip()) for line in file.readlines()]
    return data


def read_dna_data(file_path):
    """Read DNA dataset and map sequences to integers."""
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}  # DNA mapping
    data = []
    with open(file_path, 'r') as file:
        content = file.read().replace("\n", "")  # Remove line breaks
        data = [mapping[char] for char in content if char in mapping]
    return data


def process_file(file_path, data_type, spade, user_key, decryption_key):
    """Process a single file: encrypt and decrypt, measure storage overhead and time."""
    if data_type == 'hypnogram':
        data = read_hypnogram_data(file_path)
    elif data_type == 'dna':
        data = read_dna_data(file_path)
    else:
        raise ValueError("Unknown data type.")

    # Measure encryption time
    start_time = time.time()
    encrypted_data = spade.encrypt(data, user_key)
    encryption_time = time.time() - start_time

    # Measure decryption time
    start_time = time.time()
    decrypted_data = spade.decrypt(encrypted_data, user_key)
    decryption_time = time.time() - start_time

    # Calculate storage overhead
    original_size = len(data) * 4  # Assuming each integer is 4 bytes
    encrypted_size = len(encrypted_data) * 8  # Assuming each (cipher, noise) tuple is 8 bytes
    storage_overhead = encrypted_size / original_size

    return {
        "File": file_path,
        "Original Data (Sample)": data[:10],
        "Decrypted Data (Sample)": decrypted_data[:10],
        "Encryption Time (s)": encryption_time,
        "Decryption Time (s)": decryption_time,
        "Storage Overhead (x)": storage_overhead
    }


def process_directory_parallel(directory, data_type, spade, user_key, decryption_key):
    """Process all dataset files in a directory using parallel processing."""
    file_list = [os.path.join(directory, filename) for filename in os.listdir(directory) if
                 os.path.isfile(os.path.join(directory, filename))]
    results = []
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_file, file_path, data_type, spade, user_key, decryption_key)
            for file_path in file_list
        ]
        for future in futures:
            results.append(future.result())
    return results


def test_spade():
    # Initialize SPADE
    spade = SPADE(security_param=64)  # Reduced for debugging
    num_users = 10
    msk, mpk = spade.setup(num_users)

    # Debug: Print master keys
    print("Master Secret Key (msk):", msk)
    print("Master Public Key (mpk):", mpk)

    # Set directories for datasets
    hypnogram_dir = r"C:\Users\Rishi\Desktop\Tampere\security protocols\course work 2\datasets\hypnogram"
    dna_dir = r"C:\Users\Rishi\Desktop\Tampere\security protocols\course work 2\datasets\dna"

    # Select a user key for encryption
    user_key = random.randint(1, 10)
    user_index = 0
    decryption_key = spade.key_derivation(user_index)

    # Process Hypnogram data
    print("\nProcessing Hypnogram dataset...")
    hypnogram_results = process_directory_parallel(hypnogram_dir, 'hypnogram', spade, user_key, decryption_key)

    # Save Hypnogram results to CSV
    hypnogram_df = pd.DataFrame(hypnogram_results)
    hypnogram_csv = "spade_hypnogram_results.csv"
    hypnogram_df.to_csv(hypnogram_csv, index=False)
    print(f"Hypnogram results saved to '{hypnogram_csv}'")

    # Process DNA data
    print("\nProcessing DNA dataset...")
    dna_results = process_directory_parallel(dna_dir, 'dna', spade, user_key, decryption_key)

    # Save DNA results to CSV
    dna_df = pd.DataFrame(dna_results)
    dna_csv = "spade_dna_results.csv"
    dna_df.to_csv(dna_csv, index=False)
    print(f"DNA results saved to '{dna_csv}'")


if __name__ == "__main__":
    test_spade()
