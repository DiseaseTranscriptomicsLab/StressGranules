import pandas as pd
import numpy as np
import time, os

starttime = time.time()

# Load data
SedSeqTable = pd.read_table("Control.txt", header=None, sep=" ")  # pSups

# Centrifugation parameters
Acceleration = 20000 # In g
Time = 600 # In seconds
TubeSize = 1.5 # In centimeters

# First, we convert pSup to Proportion of RNA in Pellet.
SedSeqTable[3] = (SedSeqTable[1] + SedSeqTable[2]) / 2
SedSeqTable[3] = 1 - SedSeqTable[3]

# Adapted Spinner function: calculates "s" and returns SedSeqTable with new column
def spinner(SedSeqTable):
    SedSeqTable[4] = (((SedSeqTable[3])) / (Acceleration*Time/TubeSize))
    SedSeqTable[4] = SedSeqTable.iloc[:, 4].apply(lambda x: "{:.3e}".format(x))
    return SedSeqTable

# Run spinner
SedSeqTable = spinner(SedSeqTable)

# Save the updated SedSeqTable
output_path = "Control_processed.txt"
SedSeqTable.to_csv(output_path, sep=' ', index=False, header=False)

print(f"Saved updated SedSeqTable to {output_path}")
