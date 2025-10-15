# Source Code Directory

This directory contains Python source code modules for the DATA1002 project.

## Modules

### data_processing.py
Core module for data processing and cleaning operations:
- `load_data()` - Load data from CSV files
- `check_missing_values()` - Identify missing data
- `handle_missing_values()` - Handle missing data with various strategies
- `detect_outliers()` - Detect outliers using IQR or Z-score methods
- `normalize_data()` - Normalize numerical data
- `get_summary_statistics()` - Generate comprehensive statistics

## Usage

Import modules in your notebooks or scripts:

```python
from src.data_processing import load_data, check_missing_values

# Load and check data
df = load_data('data/sample_data.csv')
missing = check_missing_values(df)
```

## Adding New Modules

When adding new functionality:
1. Create well-documented functions with type hints
2. Include docstrings with parameter and return descriptions
3. Add example usage in the module's `if __name__ == "__main__"` block
4. Update this README with the new module information
