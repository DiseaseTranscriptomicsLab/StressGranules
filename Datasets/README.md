# Datasets

This folder contains code necessary to run the analyses I performed on each dataset. I always provide both an R markdown file, as well as an html file of the analyses.

## Repository Structure

### Centrifugation 

Analyses related to the SedSeq dataset used, 

- **`Centrifugation/`**
In this folder, I present all analyses pertaining to the dataset by **H. Glauninger, 2024**.
**GSE265963** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE265963))

  - **`Azide0.5_processed.txt`**: **`Control_processed.txt`**; **`Ethanol_processed.txt`**; **`HSStress_processed.txt`**
  These files contain the calculated average sedimentation coefficients for yeast, in the corresponding experimental condition.

### PBodies 

Analyses related to the PBody datasets used, 

- **`PBodies/`**
In this folder, I present all analyses pertaining to the datasets by **T. Matheny, 2019** and **S. Kodali, 2024**
**GSE138988** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE138988))
**GSE224858** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE224858))
**GSE224752** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE224752))

  - **`SGcontrolledbyPB.txt`**
  This file contains the SG signal compared to the stressed PB signal. Thus, theoritically controlled for the DC Method.


### Senescence 

Analyses related to the Senescence dataset used, 

- **`Senescence/`**
In this folder, I present all analyses pertaining to the dataset by **V. López-Polo, 2024**.
**GSE236521** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE236521))

### WCTranscriptome 

Analyses related to whole-cell transcriptome datasets used, and process used to develop the stress granule signatures, and corresponding testing on TCGA data. 

- **`GSE173953`**
In these files, I present all analyses pertaining to the dataset by **M. Paget, 2023**.
**GSE173953** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173953))

- **`TMatheny`**
In these files, I present all analyses pertaining to the datasets by **T. Matheny, 2019 & 2021**.
**GSE138988** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE138988))
**GSE119977** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119977))

- **`MergedWC`**
In these files, I present all analyses pertaining to the integration of the datasets by ** M.Paget, 2023, and T. Matheny, 2019 & 2021**.
**GSE173953** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173953))
**GSE138988** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE138988))
**GSE119977** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119977))

- **`Signature_markeR_Bi.Rmd`**
In this file, I present all analyses pertaining to the development of the SGScore signatures, using the markeR package originally developed by **R. Martins-Silva, 2025**. Due to the long knitting duration, only markdown format is available.
**markeR** ([GitHub Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173953](https://github.com/DiseaseTranscriptomicsLab/markeR)))

- **`SIGNATURE_TCGA.Rmd`**
In this file, I present all analyses pertaining to the usage of the SGScore signatures, testing them on **GDC TCGA Data**. Due to the long knitting duration, only markdown format is available.
**TCGA** ([GDC Portal Link](https://portal.gdc.cancer.gov/)))

### SGTranscriptome 

Analyses related to isolated SG transcriptome datasets used. 

- **`GSE99304`**
In these files, I present all analyses pertaining to the dataset by **A. Khong, 2017**.
**GSE99304** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99304))

- **`GSE138988`**
In these files, I present all analyses pertaining to the dataset by **T. Matheny, 2019**.
**GSE138988** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE138988))

- **`GSE121575`**
In these files, I present all analyses pertaining to the dataset by **A. Padrón, 2019**.
**GSE121575** ([NCBI GEO Link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121575))

## Citation

If you use this repository or any of its contents, please cite our associated publication and the relevant original studies referenced above:

> [Insert full citation and DOI once available]
