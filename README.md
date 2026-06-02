# Integrating SQL with EDA Analysis

## Project Overview

This project demonstrates the integration of SQL and Exploratory Data Analysis (EDA) using Python. Data is stored in an SQL database, retrieved through SQL queries, and analyzed using the Pandas library.

## Objectives

* Create and manage a database using SQL
* Retrieve data using SQL queries
* Perform Exploratory Data Analysis (EDA)
* Generate summary statistics
* Analyze category-wise and city-wise sales
* Integrate SQL with Python for data analysis

## Tools and Technologies

* Python
* SQL (SQLite)
* Pandas
* GitHub

## Dataset Description

The dataset contains sales transaction records.

| Column   | Description              |
| -------- | ------------------------ |
| id       | Unique record identifier |
| product  | Product name             |
| category | Product category         |
| amount   | Sales amount             |
| city     | City of sale             |

## Project Workflow

```text
Create Database
       ↓
Store Data in SQL
       ↓
Execute SQL Queries
       ↓
Load Data into Pandas
       ↓
Perform EDA
       ↓
Generate Insights
       ↓
Conclusion
```

## Features

* Database creation using SQLite
* Data insertion using SQL commands
* Data retrieval using SQL queries
* Summary statistics generation
* Category-wise sales analysis
* City-wise sales analysis
* SQL and Python integration

## Project Structure

```text
integrating-sql-with-eda-analysis/
│
├── README.md
├── sql_eda_integration.py
├── dataset.csv
├── output.txt
└── images/
    ├── sql_workflow.png
    ├── eda_process.png
    ├── sql_python_integration.png
    └── data_analysis_cycle.png
```

## Analysis Performed

* Dataset inspection
* First five records display
* Dataset information summary
* Descriptive statistics
* Total record count
* Average sales calculation
* Highest and lowest sales identification
* Category-wise sales analysis
* City-wise sales analysis

## Key Findings

* Electronics products generated higher sales than furniture products.
* Sales varied across different cities.
* SQL efficiently stored and retrieved data.
* Pandas simplified exploratory data analysis.
* Combining SQL and Python improved data analysis capabilities.

## Future Improvements

* Use larger datasets
* Add data visualizations
* Perform advanced SQL queries
* Integrate with MySQL or PostgreSQL
* Build interactive dashboards

## Conclusion

This project demonstrates how SQL and Python can work together for Exploratory Data Analysis. SQL is used for data storage and retrieval, while Pandas is used for analysis and insight generation. This integration provides an efficient workflow for real-world data analysis projects.
