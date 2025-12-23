# Reports Directory

This directory contains generated reports, figures, and visualizations from the analysis.

## Contents

- **Figures**: Plots and charts generated during analysis
- **Reports**: Written summaries and findings
- **Presentations**: Slides or presentation materials

## File Naming Convention

Use descriptive names that include:
- Date (YYYY-MM-DD format)
- Type of visualization or report
- Brief description

Example:
- `2025-01-15_distribution_analysis.png`
- `2025-01-20_final_report.pdf`
- `correlation_heatmap.png`

## Generating Reports

Reports can be generated from Jupyter notebooks:

```python
# Save figure
plt.savefig('reports/figure_name.png', dpi=300, bbox_inches='tight')

# Export notebook to HTML
# jupyter nbconvert --to html notebooks/data_analysis.ipynb --output-dir=reports/
```

## Notes

- Keep reports organized by date or project phase
- Include figure captions and descriptions
- Version control generated files only if they're final deliverables
