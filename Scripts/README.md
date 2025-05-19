# Scripts

This folder contains Bash scripts used for preprocessing datasets prior to downstream analyses.

## Folder Structure

- **`fastqc.sh`**  
  Example Bash script for running [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) on FASTQ files to assess sequence quality.

- **`trimmomatic.sh`**  
  Example Bash script for trimming adapter sequences from FASTQ files using [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic).  
  Adapter sequences must be provided in an additional file.  
  If you use this script or Trimmomatic in your workflow, please cite the original authors:  
  *Bolger et al., Bioinformatics (2014), [PMC4103590](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4103590/)*

- **`alignment.sh`**  
  Example Bash script for aligning reads to a reference genome using [STAR](https://github.com/alexdobin/STAR).  
  If you use this script or STAR, please cite the original publication:  
  *Dobin et al., Bioinformatics (2013), [PMC3530905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3530905/)*

## Citation

If you use this repository or any of its contents, please cite our associated publication, as well as the tools referenced above when applicable:

> [Insert full citation and DOI once available]
