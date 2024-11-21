import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
spade_results = pd.read_csv('spade_hypnogram_results.csv')

# Visualization: Encryption Time vs Decryption Time
plt.figure(figsize=(10, 6))
plt.hist(spade_results["Encryption Time (s)"], bins=50, alpha=0.7, label="Encryption Time (s)")
plt.hist(spade_results["Decryption Time (s)"], bins=50, alpha=0.7, label="Decryption Time (s)")
plt.title("Distribution of Encryption and Decryption Times")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()

# Visualization: Storage Overhead Distribution
plt.figure(figsize=(10, 6))
plt.hist(spade_results["Storage Overhead (x)"], bins=20, alpha=0.7, color='orange', label="Storage Overhead (x)")
plt.title("Distribution of Storage Overhead")
plt.xlabel("Storage Overhead (x)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()

# Visualization: Sample Encryption and Decryption Times by File
sample = spade_results.head(50)  # Take a sample of 50 files
plt.figure(figsize=(12, 6))
plt.plot(sample.index, sample["Encryption Time (s)"], marker='o', label="Encryption Time (s)")
plt.plot(sample.index, sample["Decryption Time (s)"], marker='x', label="Decryption Time (s)")
plt.title("Sample Encryption and Decryption Times")
plt.xlabel("File Index")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
