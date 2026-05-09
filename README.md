# Applied Data Analytics: Economic Impact and Health Prediction

## Overview

This repository presents a three-stage applied data analytics project covering data cleaning, exploratory analysis, visualization, and predictive modelling. The work combines two analytical themes: the economic impact of COVID-19 in Australia, with a focus on NSW, and global health outcome prediction using Sustainable Development Goal 3 indicators.

本仓库展示了一个三阶段应用数据分析项目，覆盖数据清洗、探索性分析、可视化和预测建模。项目包含两个分析主题：以 NSW 为重点的 COVID-19 对澳大利亚经济的影响，以及基于可持续发展目标 3 健康指标的全球健康结果预测。

## Project Scope

The project is organized around a complete analytics workflow:

项目按照完整的数据分析流程组织：

1. Data preparation: collected, cleaned, filtered, reshaped, and merged multiple public datasets.
2. Exploratory analysis: produced grouped summaries and visualizations to communicate economic trends.
3. Predictive modelling: trained and evaluated regression models for health indicator prediction.

1. 数据准备：收集、清洗、筛选、重塑并合并多个公开数据集。
2. 探索性分析：生成分组汇总和可视化，用于解释经济趋势。
3. 预测建模：训练并评估回归模型，用于健康指标预测。

## Repository Structure

```text
STAGE_1/  Data preparation and multi-source dataset integration
STAGE_2/  Exploratory analysis, grouped summaries, and visual communication
STAGE_3/  Predictive modelling with global health indicators
docs/     Supporting project notes and public release checklist
```

```text
STAGE_1/  数据准备与多源数据集整合
STAGE_2/  探索性分析、分组汇总与可视化表达
STAGE_3/  基于全球健康指标的预测建模
docs/     项目辅助说明与公开发布检查清单
```

## Data Themes

The economic analysis uses monthly public datasets related to international student enrolments, public transport activity, labour market indicators, and airport passenger movement from 2019 to 2021. The health prediction analysis uses cleaned SDG Goal 3 indicators covering multiple countries, regions, years, and health system measures.

经济分析使用 2019 至 2021 年的月度公开数据，主题包括国际学生注册、公共交通出行、劳动力市场指标和机场客流。健康预测分析使用清洗后的可持续发展目标 3 指标数据，覆盖多个国家、区域、年份和健康系统指标。

## Methods And Tools

Python was used for data processing, aggregation, visualization, and modelling. Main libraries and methods include pandas, NumPy, matplotlib, grouped aggregation, time-series comparison, regression modelling, K-nearest neighbors regression, support vector regression, Bayesian ridge regression, RMSE, and R-squared evaluation.

项目使用 Python 进行数据处理、聚合、可视化和建模。主要工具与方法包括 pandas、NumPy、matplotlib、分组聚合、时间序列对比、回归建模、K 近邻回归、支持向量回归、贝叶斯岭回归、RMSE 和 R-squared 评估。

## Key Outputs

- Integrated four economic datasets into a 36-row, 35-field analytical dataset covering 2019-2021 monthly observations.
- Built grouped summaries and charts showing major changes in travel, employment, transport, and international education activity during the pandemic period.
- Identified a drop in airport passenger movement from 44.4M in 2019 to 7.9M in 2021 in the curated passenger dataset.
- Prepared a cleaned health indicator dataset with 163 records and 28 fields across five global regions.
- Compared multiple regression approaches for health outcome prediction and evaluated model performance using RMSE and R-squared.

- 将四类经济数据整合为一个包含 36 行、35 个字段的分析数据集，覆盖 2019 至 2021 年月度观测。
- 构建分组汇总和图表，展示疫情期间旅行、就业、交通和国际教育活动的显著变化。
- 在整理后的机场客流数据中识别出客流量从 2019 年 44.4M 降至 2021 年 7.9M。
- 准备了一个包含 163 条记录、28 个字段、覆盖五个全球区域的健康指标清洗数据集。
- 对比多种健康结果预测回归方法，并使用 RMSE 与 R-squared 评估模型表现。

## Privacy And Public Use

This public-facing documentation avoids personal identifiers and institution-specific details. Original reports and notebooks may contain local paths, contributor identifiers, or submission metadata; review the public release checklist before publishing selected files.

本公开说明不包含个人身份信息和具体机构信息。原始报告和 notebook 中可能包含本地路径、贡献者标识或提交元数据；发布前请先检查公开发布清单。
