# Public Release Checklist

Use this checklist before pushing selected files to a public GitHub repository.

## Safe To Publish

- `README.md`
- `STAGE_1/项目说明.md`
- `STAGE_2/项目说明.md`
- `STAGE_3/项目说明.md`
- Cleaned CSV files after confirming their source allows redistribution
- Exported code files after removing local paths and personal identifiers

## Review Before Publishing

- `.docx` reports: may contain names, IDs, submission metadata, comments, and internal notes.
- `.ipynb` notebooks: may contain local paths, usernames, output metadata, and contributor identifiers.
- `.pdf` exports: may contain cover pages, names, IDs, or embedded report metadata.
- `.zip` files: may include original private files, duplicate reports, or unreviewed metadata.

## Recommended Cleanup

- Replace local absolute paths with relative paths.
- Rename files that contain contributor IDs or usernames.
- Remove submission cover pages and internal planning notes from public reports.
- Keep raw data only when the original source license allows redistribution.
- Prefer publishing cleaned datasets, reproducible notebooks, and concise documentation.

## Suggested Repository Names

- `applied-data-analytics-economic-health`
- `covid-economic-impact-health-prediction`
- `python-data-analysis-economic-health`

Recommended: `applied-data-analytics-economic-health`

This name is broad enough to cover both the economic analysis and health prediction parts while still making the repository purpose clear.
