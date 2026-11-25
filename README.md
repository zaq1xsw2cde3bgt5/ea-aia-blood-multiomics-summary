# Pretreatment blood multiomics group summaries

This repository contains group-level RNA, single-cell and serum-protein summary statistics for an exploratory six-patient study of pain outcomes after routine electroacupuncture during aromatase inhibitor treatment for breast cancer. Blood was collected before treatment. Three participants were selected in each later pain-outcome category. These data do not establish clinical prediction, treatment efficacy or an electroacupuncture-specific mechanism.

## Contents

- `data/bulk_rna_group_statistics.csv.gz`: all 46,714 exported RNA group contrasts; individual TPM columns have been removed.
- `data/serum_protein_group_statistics.csv.gz`: all 4,391 quantified protein group contrasts; individual abundance columns have been removed.
- `data/single_cell_celltype_group_statistics.csv.gz`: source exploratory cell-level contrasts by cell type. Patients, not cells, are biological replicates.
- `data/cell_proportion_group_statistics.csv`: six outcome-group comparisons using patient-level permutation statistics.
- Other `data/` files contain reported RNA/protein enrichment and RNA–protein group correspondence.
- `metadata/data_dictionary.csv` documents columns. `metadata/data_files.json` records row counts, descriptions and SHA-256 checksums.
- `scripts/validate_public_package.py` checks package hashes, row counts and the absence of individual expression columns.

The `.csv.gz` files are ordinary UTF-8 comma-separated tables compressed with gzip. They can be read with `pandas.read_csv(path)` or standard Python `gzip` and `csv` libraries. Empty fields retain source missingness. Numeric values and row ordering are preserved as exported, rather than recomputed or rounded during packaging.

## Statistical interpretation

RNA `padj` is the reported correction. `all_rows_BH_q` is the additional check across all 46,714 exported P values; 21 of the 26 reported-adjusted screening features pass that check. No protein passes BH correction across 4,391 proteins. Protein GO within-ontology and pooled correction results are both retained. The Hallmark table contains only the three delivered results, not the entire tested gene-set family. Source zero P values, where present, are preserved and should not be interpreted as exact probabilities of zero. Full analysis pipelines, alignment workflows and model fits are not included or claimed to be reproducible from these summaries alone.

## Data access and raw-data status

This is a summary-statistics release. Participant-level bulk count/TPM tables, single-cell count matrices and the original sample key remain outside this public repository. FASTQ/BAM/CRAM reads and raw mass-spectrometry files were not located in the three service-delivery folders inspected on 25 November 2026. The service's single-cell `raw_matrix` denotes an unfiltered count matrix, not raw sequencing reads. No GEO/SRA/ProteomeXchange accession has been obtained. This repository does not replace any domain-repository deposit or reviewer-access arrangement required by a journal.

Requests for permitted participant-level data should be directed to Jiuda Zhao (jiudazhao@126.com), Qinghai University Affiliated Hospital, and remain subject to consent and institutional ethics/privacy requirements. A controlled-access route has not yet been established.

## Provenance and rights

Tables were prepared from existing service exports and manuscript-check outputs. This packaging step removes participant columns and standardizes documentation; it does not rerun sequencing, fit new models or generate experimental observations. Absolute source paths and original participant codes are kept in a local private provenance ledger and are not published.

The study manuscript is not yet published. No article DOI or database accession is claimed. A public reuse license has not been assigned; contact the corresponding author for reuse terms. Do not infer an open-data license merely from repository visibility.

## Validate

Run `python scripts/validate_public_package.py` from the repository root. It uses only the Python standard library.
