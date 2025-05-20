import pandas as pd
import numpy as np
import time, os
from multiprocessing import Pool

starttime = time.time()
OGtable = pd.read_table("./OriginalSamples/SG2017/SG2017_WC1.txt", header=0) #This serves as an expression basis. It is a WC sample from A Khong 2017 in TPMs, in this example.
#table_DIST = pd.read_table("./WCDistrib.txt", header=0) #This contains fragmentation distribution, on a gene by gene basis. In this example, it contains distribution from WC samples. 

def fragger(table_SIM): # This is the fragmentation function itself. It is formatted in a way in such only one variable/object is used as input, to facilitate multiprocessing
    fraglength = []
    fragments = []
    GeneID = table_SIM[0]
    TPM = table_SIM[2]
    for t in range(0, TPM):
        GeneLength = table_SIM[1]
        table_Temp = table_DIST[table_DIST["HGNC.symbol"] == GeneID]
        table_Temp = table_Temp[table_Temp["fragments"] <= GeneLength]
        table_Temp["n"] = table_Temp['n'] / table_Temp['n'].sum()
        if len(table_Temp)!=0:
            while True:
                cut = np.random.choice(size=1, a=table_Temp["fragments"], replace=True, p=table_Temp["n"])
                if cut >= GeneLength:
                    fraglength.append(GeneLength)
                    break
                elif cut < GeneLength:
                    fraglength.append(cut)
                    GeneLength = GeneLength-cut

        fragments += fraglength
        fraglength = []

    fragments = pd.DataFrame({"fragments": fragments})
    fragments["Gene"] = GeneID
    return fragments

if __name__ == "__main__":
    # Create two copies of OGtable 
    table, transnum = OGtable, 1000000 # In here, you multiply by how many transcripts you want to simulate in your simmed WC samples
    table_BU, table_SG = table.copy(), table.copy()
    # Adjust TPM values in OGtable_BU and OGtable_SG
    table_BU["TPM"] = (table_BU["TPM"] * transnum).round().astype(int)
    table_BU = table_BU[table_BU["TPM"] != 0]
    table_SG["TPM"] = (table_SG["TPM"] * (transnum * 1.9)).round().astype(int) # In here, you multiply the transnum, by how many more transcripts you want in your simmed SG samples
    table_SG = table_SG[table_SG["TPM"] != 0]
    # Simulate fragment generation for each experiment
    #for WC
    table_SIM = table_BU
    WCdist = pd.read_table("./WCDistrib.txt", header=0) #In here, you select what fragment distribution you want to use for your simmed WC samples.
    table_DIST = WCdist
    #for Sg
    table_SIM = table_SG
    SGdist = pd.read_table("./SGDistrib.txt", header=0) #In here, you select what fragment distribution you want to use for your simmed SG samples.
    table_DIST = SGdist
    table_SIM = table_SIM.to_numpy()

    with Pool(os.cpu_count()-10) as pool: #Select how many multiprocessings you want.
        SimFrags = pool.map(fragger, table_SIM)

    SimTable = pd.concat(SimFrags, axis=0)
    SimTable.to_csv("./SimulatedSamples/SG2017/SG2017_MimiSEQ_WC", index=False) #Choose where, and what is the name you want for your file

    print('That took {} seconds'.format(time.time() - starttime)) #Just for benchmarking purposes
