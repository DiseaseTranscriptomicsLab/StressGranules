# Files

This folder contains essential reference files and key outputs from our analyses. Users are welcome to utilise these resources for their own applications, with appropriate citation.

## Repository Structure

- **`TranscriptLength.txt`**  
  Contains canonical transcript lengths, obtained from [Ensembl BioMart](https://www.ensembl.org/biomart/martview/).  
  The file includes a header for clarity.

- **`SG1.txt` and `SG2.txt`**  
  Stress granule (SG) gene signatures defined using elastic net regression:
  - `SG1`: Generated with an alpha parameter of 0.75  
  - `SG2`: Generated with an alpha parameter of 0.5  

  Discovery datasets:
  - [GSE138988](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE138988) (T. Matheny, 2019)
  - [GSE119977](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119977) (T. Matheny, 2021)

  Validation dataset:
  - [GSE173953](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173953) (M. Paget, 2023)

  For methodological details, please refer to the Methods section of the associated publication.

- **`MergedWCSig.txt`**  
  Represents the purified whole-cell (WC) transcriptomic signal associated with SG assembly, after batch effect removal.  
  Derived from the following datasets:
  - [GSE138988](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE138988) (T. Matheny, 2019)
  - [GSE119977](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119977) (T. Matheny, 2021)
  - [GSE173953](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173953) (M. Paget, 2023)

  See the publication’s Methods section for processing details.

- **`SGEnrichedTranscripts.txt`**  
  Contains transcripts identified as enriched or depleted in stress granules, after appropriate normalisation and controls.  
  Based on:
  - [GSE138058](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE138058) (S.N. Somasekharan, 2020)
  - [GSE212380](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212380) (P. Kudrin, 2024)
  - [PRJNA1152621](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA1152621) (S. Rajachandran)

## Citation

If you use this repository or any of its contents, please cite our associated publication (and corresponding studies used to generate the files):

> [Insert full citation and DOI once available]
