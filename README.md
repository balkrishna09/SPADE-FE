SPADE Functional Encryption Implementation
This README provides instructions on how to run the SPADE Functional Encryption (FE) implementation and reproduce the results for Hypnogram and DNA datasets.

Requirements
To run the code, ensure the following dependencies are installed:
Python Version:
•	Python 3.7 or higher
Required Libraries:
•	os
•	random
•	time
•	pandas
•	concurrent.futures
•	matplotlib (for visualization)
You can use pip to install to download missing dependencies for eg: “pip install pandas matplotlib”


The project includes the following files and directories:
•	spade_implementation.py: Main implementation of the SPADE scheme.
•	Visualize.py: Graphs for CSV file.
•	datasets/hypnogram/: Directory containing Hypnogram dataset files.
•	datasets/dna/: Directory containing DNA dataset files.
•	spade_hypnogram_results.csv: Results of the Hypnogram dataset.
•	spade_dna_results.csv: Results of the DNA dataset.

How to Run the Code
1.	Clone or download the project repository “https://github.com/balkrishna09/SPADE-FE”
2.	Place the datasets in the respective directories:
o	Hypnogram files in datasets/hypnogram/
o	DNA files in datasets/dna/
3.	Open the terminal or command prompt and navigate to the directory containing spade_implementation.py. You can also open the project folder in any IDE such as pycharm or spyder and run code.
4.	Run the script: “python spade_implementation.py”
5.	Code will create a CSV file for each data set.
6.	Now open visualize.py file and change the CSV file location accordingly and run the code to get graph.


Contact
For questions or issues, please contact: Email: Balkrishna.giri@tuni.fi or Balkrishna.giri07@gmail.com
GitHub: https://github.com/your_repo




