# Exploratory Data Analysis with SQL

## Project Overview

This project demonstrates how SQL can be used to perform Exploratory Data Analysis (EDA) on a sales dataset. The analysis includes data exploration, filtering, sorting, aggregation, and extraction of meaningful insights using SQL queries.

## Objectives

- Learn SQL fundamentals
- Explore and understand data
- Filter records using WHERE
- Sort records using ORDER BY
- Generate summary statistics
- Perform category-wise analysis
- Extract meaningful business insights

## Tools Used

- SQL
- MySQL / SQLite / PostgreSQL
- GitHub

## Dataset Description

The dataset contains sales transaction records with the following fields:

| Column | Description |
|----------|-------------|
| id | Unique record identifier |
| product | Product name |
| category | Product category |
| amount | Sales amount |
| city | City of sale |

## SQL Concepts Covered

- CREATE TABLE
- INSERT INTO
- SELECT
- WHERE
- ORDER BY
- DISTINCT
- COUNT()
- AVG()
- MIN()
- MAX()
- SUM()
- GROUP BY

## EDA Workflow

```text
Create Dataset
      ↓
Load Data
      ↓
Explore Data
      ↓
Filter Records
      ↓
Sort Records
      ↓
Aggregate Data
      ↓
Analyze Results
      ↓
Generate Insights
```

## Sample SQL Queries

### View Complete Dataset

```sql
SELECT * FROM sales;
```

### Filter Electronics Products

```sql
SELECT *
FROM sales
WHERE category = 'Electronics';
```

### Sort Sales by Amount

```sql
SELECT *
FROM sales
ORDER BY amount DESC;
```

### Category-wise Average Sales

```sql
SELECT category,
       AVG(amount) AS average_sales
FROM sales
GROUP BY category;
```

## Key Findings

- Electronics products generated the highest sales values.
- Furniture products had lower average sales amounts.
- Sales performance varied across cities.
- Aggregation functions helped summarize data effectively.
- SQL queries revealed useful business patterns and trends.

## Project Structure

```text
exploratory-data-analysis-with-sql/
│
├── README.md
├── sql_eda_analysis.sql
├── query_outputs.txt
├── dataset.csv
└── images/
    ├── sql_workflow.png
    ├── eda_process.png
    ├── sql_query_flow.png
    └── data_analysis_cycle.png
```

## Future Improvements

- Analyze larger datasets
- Use JOIN operations
- Add subqueries
- Create SQL views
- Integrate SQL with Python
- Build dashboards for visualization

## Conclusion

This project demonstrates the use of SQL for Exploratory Data Analysis. By applying filtering, sorting, grouping, and aggregation techniques, valuable insights can be extracted from structured datasets. SQL provides a strong foundation for data analysis and decision-making.
