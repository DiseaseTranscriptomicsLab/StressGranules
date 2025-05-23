import pandas as pd
import numpy as np
import time, os

starttime = time.time()

# Load data
OGtable = pd.read_table("SG2017_WC1.txt", header=0)  # Expression table (TPMs) from which to start centrifugation simulation
SedSeqTable = pd.read_table("YeastSs.txt", header=0, sep=" ")  # Table with Yeast Molecular RNAs. Replace with Human file, if needed

# Centrifugation parameters
CentrifugationN = 3 # Number of centrifugations performed
Acceleration = 18000 # In g
Time = 1200 # In seconds
TubeSize = 2 # In centimeters

# Spinner function: calculates "d" and returns WeightTable with new column
def spinner(weight_table):
    # Compute S using np.where based on 'Cromo' values
    S = np.where(
        weight_table['Cromo'] == 'Mito',
        np.cbrt((weight_table['Length'])**(1/3)) * 3.23e-11 + 1.17e-9, # Formula to apply in mitochondrial RNAs
        np.cbrt((weight_table['Length'])**(1/3)) * 6.09e-11 + 3.88e-10 # Formula to apply to other RNAs
    )

    # Calculate 'd' using S and store it in the dataframe
    weight_table['d'] = (S * Acceleration * Time) / TubeSize # To calculate percentage of each RNA that precipitates

    return weight_table
if __name__ == "__main__":
    # Run spinner to calculate 'd'
    WeightTable = spinner(SedSeqTable)

    # Merge OGtable with WeightTable using gene ID column (assumed to be the first column)
    # Adjust column names as needed based on your actual files
    merged = OGtable.merge(WeightTable[['Gene', 'd']], left_on='GeneID', right_on='Gene')

    # Multiply TPM by d, CentrifugationN times
    for _ in range(CentrifugationN): #To multiply by the number of centrifugations performed
        merged['TPM'] = merged['TPM'] * merged['d']

    # Save result
    output_path = "./SimulatedSamples/SG2017/SG2017_MimiSEQ_SedSeq_SG1.csv" #To name and save our simulated file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    merged.to_csv(output_path, index=False)

    print('That took {} seconds'.format(time.time() - starttime)) # For benchmarking purposes
