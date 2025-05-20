# Simulations

This folder contains the files and code necessary to run both simulation pipelines: **MimiSeq** (fragmentation-based) and **SpinSim** (centrifugation-based).

## Repository Structure

### MimiSeq

Files and scripts related to the MimiSeq simulation pipeline.

- **`SG2017_WC1.txt`**  
  TPM expression values for a whole-cell sample from A. Khong, 2017  
  [GSE99304](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99304)

- **`SG2017_SG1.txt`**  
  TPM expression values for a stress granule sample from A. Khong, 2017  
  [GSE99304](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99304)

- **`WCDistrib.zip`**  
  Zipped `.txt` file containing fragmentation probabilities for the whole-cell sample (A. Khong, 2017)  
  [GSE99304](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99304)

- **`SGDistrib.zip`**  
  Zipped `.txt` file containing fragmentation probabilities for the stress granule sample (A. Khong, 2017)  
  [GSE99304](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99304)

- **`Mimi-seq.py`**  
  Python 3 script for running the MimiSeq simulation pipeline.

### SpinSim

Files and scripts related to the SpinSim simulation pipeline.

- **`SG2017_WC1.txt`**  
  TPM expression values for a whole-cell sample from A. Khong, 2017  
  [GSE99304](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99304)

- **`MolecularWeights.csv`**  
  Molecular weights for RNA transcripts (no modifications included).

- **`MolecularWeights_ac4C.csv`**  
  Molecular weights for RNA transcripts with **ac4C** modifications.

- **`MolecularWeights_m6A.csv`**  
  Molecular weights for RNA transcripts with **m6A** modifications.

- **`YeastSs.txt`**  
  Contains RNA transcript lengths, chromosome of origin, and sedimentation coefficients under stress and unstressed conditions for *Saccharomyces cerevisiae*.  
  Based on: H. Glauninger, 2024  
  [GSE265963](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE265963)

- **`HumanSs.txt`**  
  Contains RNA transcript lengths and chromosome of origin for *Homo sapiens*.

- **`SpinSim.py`**  
  Python 3 script for running the original SpinSim pipeline using molecular weights.  
  Can incorporate RNA modifications.

- **`SpinSim_SedSeq.py`**  
  Python 3 script for running the SpinSim pipeline using sedimentation coefficients calculated from yeast data (Glauninger, 2024).  
  [GSE265963](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE265963)

## Citation

If you use this repository or any of its contents, please cite our associated publication and the relevant original studies referenced above:

> [Insert full citation and DOI once available]
