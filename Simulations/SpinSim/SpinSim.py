import pandas as pd
import numpy as np
import time, os

starttime = time.time()

# Load data
OGtable = pd.read_table("SpinSim/SG2017_WC1.txt", header=0)  # Expression table (TPMs) from which to start centrifugation. Whole Cell sample for A. Khong 2017 in example
WeightTable = pd.read_table("SpinSim/MolecularWeights.csv", header=0, sep=" ")  # Molecular weights of RNAs

# Centrifugation parameters
CentrifugationN = 3 # Number of centrifugations performed
Acceleration = 18000 # In g
Time = 1200 # In seconds
TubeSize = 2 # In centimeters

# Spinner function: calculates "d" and returns WeightTable with new column
def spinner(weight_table):
    weight_table['d'] = (((weight_table.iloc[:, 0]) ** (1/3)) * Acceleration * Time) / TubeSize * 1e-13 #This formula calculates the amount from each RNA that precipitates. We multiply by 1e-13 to maintain in silico S values on the same ballpark as real ones (S is in svedbergs)
    return weight_table

if __name__ == "__main__":
    # Run spinner to calculate 'd'
    WeightTable = spinner(WeightTable)

    # Merge OGtable with WeightTable using gene ID column (assumed to be the first column)
    # Adjust column names as needed based on your actual files
    merged = OGtable.merge(WeightTable[['Gene', 'd']], left_on='GeneID', right_on='Gene')

    # Multiply TPM by d, CentrifugationN times
    for _ in range(CentrifugationN): #To multiply through number of centrifugations
        merged['TPM'] = merged['TPM'] * merged['d']

    # Save result
    output_path = "./SimulatedSamples/SG2017/SG2017_MimiSEQ_SG1.csv" #The name which we want to give to our file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    merged.to_csv(output_path, index=False)

    print('That took {} seconds'.format(time.time() - starttime)) #For benchmarkking purposes
