import pandas as pd
import numpy as np
import time, os
from multiprocessing import Pool

starttime = time.time()
OGtable = pd.read_table("./OriginalSamples/SG2017/SG2017_WC1.txt", header=0)
table_DIST = pd.read_table("./WCDistrib.txt", header=0)

def fragger(table_SIM):
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
    table, transnum = OGtable, 1000000
    table_BU, table_SG = table.copy(), table.copy()
    # Adjust TPM values in OGtable_BU and OGtable_SG
    table_BU["TPM"] = (table_BU["TPM"] * transnum).round().astype(int)
    table_BU = table_BU[table_BU["TPM"] != 0]
    table_SG["TPM"] = (table_SG["TPM"] * (transnum * 1.9)).round().astype(int)
    table_SG = table_SG[table_SG["TPM"] != 0]
    # Simulate fragment generation for each experiment
    #for WC
    table_SIM = table_BU
    WCdist = pd.read_table("./WCDistrib.txt", header=0)
    table_DIST = WCdist
    #for Sg
    table_SIM = table_SG
    SGdist = pd.read_table("./SGDistrib.txt", header=0)
    table_DIST = SGdist
    table_SIM = table_SIM.to_numpy()

    with Pool(os.cpu_count()-10) as pool:
        SimFrags = pool.map(fragger, table_SIM)

    SimTable = pd.concat(SimFrags, axis=0)
    SimTable.to_csv("./SimulatedSamples/SG2017/SG2017_MimiSEQ_WC", index=False)

    print('That took {} seconds'.format(time.time() - starttime))