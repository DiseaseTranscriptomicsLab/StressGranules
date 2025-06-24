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

- **`YEAST_Bulk_1.txt`**  
  TPM expression values for a whole-cell yeast sample from A. Khong, 2017  
  [GSE99304](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99304)

- **`MolecularWeights.csv`**  
  Molecular weights for RNA transcripts (no modifications included).

- **`MolecularWeights_ac4C.csv`**  
  Molecular weights for RNA transcripts with **ac4C** modifications.

- **`MolecularWeights_m6A.csv`**  
  Molecular weights for RNA transcripts with **m6A** modifications.

- **`Azide0.5.txt`**; **`Control.txt`**; **`Ethanol.txt`**; **`HSStress.txt`**   
  Contains pSup of yeast submitted to centrifugation, in the corresponding experimental conditions.
  Based on: H. Glauninger, 2024  
  [GSE265963](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE265963)

- **`HumanSs.txt`**  
  Contains RNA transcript lengths and chromosome of origin for *Homo sapiens*.

- **`SedSeq_to_SpinSim_Converter.py`**  
  Python 3 script for converting pSup into sedimentation coefficients. pSup is obtained from yeast data (Glauninger, 2024).  Resulting files are in the `Dataset` folder in the root.
  [GSE265963](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE265963)

- **`SpinSim.py`**  
  Python 3 script for running the original SpinSim pipeline using molecular weights.  
  Can incorporate RNA modifications.

- **`SpinSim_SedSeq.py`**  
  Python 3 script for running the SpinSim pipeline using sedimentation coefficients calculated from yeast data (Glauninger, 2024), adapted for usage with human whole cell expression values. 
  [GSE265963](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE265963)

- **`SpinSim_SedSeq_Yeast.py`**  
  Python 3 script for running the SpinSim pipeline using sedimentation coefficients calculated from yeast data (Glauninger, 2024), for direct usage with yeast whole cell expression values. 
  [GSE265963](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE265963)

## Citation

If you use this repository or any of its contents, please cite our associated publication and the relevant original studies referenced above:

> [Insert full citation and DOI once available]
