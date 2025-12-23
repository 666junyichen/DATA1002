# Data Directory

This directory contains the datasets used in the DATA1002 project.

## Structure

- `raw/` - Original, immutable data
- `processed/` - Cleaned and processed data ready for analysis
- `sample_data.csv` - Sample dataset for demonstration

## Data Sources

Add information about where the data comes from, including:
- Source URLs or references
- Date of collection
- Any preprocessing done before adding to this repository
- Data dictionary or column descriptions

## Usage

Load data using pandas:

```python
import pandas as pd

# Load sample data
df = pd.read_csv('data/sample_data.csv')
```

## Notes

- Large data files (>100MB) should not be committed to git
- Use `.gitignore` to exclude large data files
- Consider using cloud storage or data repositories for large datasets
