import pandas as pd
import numpy as np
import time, os

starttime = time.time()

# Load data
OGtable = pd.read_table("YEAST_Bulk_3.txt", header=0)  # Expression table (TPM values)
SedSeqTable = pd.read_table("Azide0.5_processed.txt", header=None, sep=" ")  # S values

# Centrifugation parameters
CentrifugationN = 3  # Number of centrifugations performed
Acceleration = 18000  # In g
Time = 1200  # In seconds
TubeSize = 2  # In centimeters

def spinner(sed_seq_table):
    # Assign appropriate column names
    sed_seq_table.columns = ['ID', 'Col1', 'Col2', 'pPellet', 'S']

    # Convert S to float if it's in scientific notation as string
    sed_seq_table['S'] = sed_seq_table['S'].astype(float)

    # Calculate 'd'
    sed_seq_table['d'] = (sed_seq_table['S'] * Acceleration * Time) / TubeSize

    # Return relevant columns for merging
    return sed_seq_table[['ID', 'd']]

if __name__ == "__main__":
    # Compute 'd'
    WeightTable = spinner(SedSeqTable)

    # Merge OGtable with WeightTable on GeneID
    merged = OGtable.merge(WeightTable, on='ID')

    # Apply centrifugation effect
    for _ in range(CentrifugationN):
        merged['TPM'] = merged['TPM'] * merged['d']

    # Save result
    output_path = "./SimulatedSamples/SG2017/SG3_Yeast.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    merged.to_csv(output_path, index=False)

    print('That took {:.2f} seconds'.format(time.time() - starttime))
