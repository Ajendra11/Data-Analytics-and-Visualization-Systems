# data_audit_report_week1

# Week 0 Data Audit Report: Nepal Real Estate Dataseta

**Team Project Portfolio**

## 1. Introduction

This report documents our team's initial findings after auditing a raw dataset of 2,211 real estate listings in Nepal. Our main goal for this sprint was to check if the data could be trusted for downstream analysis and dashboards. We looked for missing values, clerical errors, and inconsistencies across the columns.

---

## 2. Dataset Overview & Missing Values

When we first loaded the dataset, we verified basic shape parameters:

- **Total Records:** 2,211 rows
- **Total Attributes:** 18 columns

### Missing Value Analysis

We noticed that multiple columns contain missing or blank entries (`NaN` or `None`). The features with the most significant gaps are:

- **Floors:** Missing 1,172 values
- **Year:** Missing 1,629 values
- **Road Type:** Missing 785 values
- Other structural columns like `Bedroom`, `Bathroom`, and `Build Area` also have scattered missing points.

### Our Strategy for Handling Missing Data

1. **Target Filtering:** If the main target variable (`Price`) is missing or invalid, we drop the row completely. Guessing prices would ruin the training capability of any future predictive models.
2. **Local Group Imputation:** For missing structural numbers like `Bedroom` or `Bathroom`, we group the data by `City` and fill in the missing cells using the localized **Median**. Housing features are heavily dependent on geographic locations (e.g., typical apartments in Kathmandu vs. standalone houses in Chitwan).
3. **Categorical Fill:** For unrecorded text data like `Amenities` or `Road Type`, we fill them with placeholder strings like `'None Listed'` so our script loops do not throw runtime exceptions.

---

## 3. Data Quality Issues Identified

During our audit sprint, we flagged three critical systemic flaws that completely distort the raw data metrics:

### 3.1 Inconsistent Unit Formats (The Area Problem)

The raw `Area` column is stored entirely as text strings and mixes completely different layout systems. Some listings are written in modern measurements like `"1200 Sq. Ft."`, while others use traditional Nepalese systems like `"4 Aana"` or hyphenated land values like `"1-2-0-0"` (*Ropani-Aana-Paisa-Daam*).

- **The Impact:** This completely breaks data comparisons. If we plot this raw data on a chart, Python treats a plot size of `"4"` (Aana) as mathematically smaller than a `"500"` Sq. Ft. studio apartment, even though 4 Aana is roughly 1,369 Sq. Ft.

### 3.2 Human Clerical Typos (The Price Outlier Problem)

We discovered severe data entry mistakes in the `Price` column. Normal residential houses are occasionally listed for completely impossible amounts—either a tiny price like `1,000 NPR` or an astronomical value like `10,000,000,000+ NPR` (over 10 Billion).

- **The Impact:** If we run a basic mathematical average (`.mean()`) on the uncleaned dataset, these multi-billion typing mistakes pull the entire baseline average upward, creating a highly inflated and incorrect representation of the actual Nepalese housing market.

### 3.3 Location Text Fragmentation

The same geographic cities are spelled or formatted inconsistently throughout the column (e.g., mixing casing like `Kathmandu` and `kathmandu`, or using abbreviations like `KTM`).

- **The Impact:** When running frequency counts (`.value_counts()`), Python splits a single real-world city into multiple false sub-categories, ruining local density calculations.

---

## 4. Visual Evidence & Data Cleaning

To prove our data audit findings, we generated and isolated individual diagnostic plots before and after building our data transformation scripts.

### 4.1 Before Cleaning (Raw Observations)

- **Chart 1 (Raw Box Plot):** Because of the multi-billion NPR outlier entries, the box plot elements for our top 5 cities were squished completely flat against the bottom axis line. The chart was unreadable unless forced onto an alternative log scale.
- **Chart 2 (Raw Scatter Plot):** The price-to-area dots were completely randomized. Because the area values mixed *Aana* and *Square Feet* strings directly on the same axis, no clear correlation could be established.

### 4.2 After Cleaning (Transformation Results)

We wrote a custom Python transformation loop using Regular Expressions (`re`) to extract the numbers from strings and map everything into a standard unit layout.

- **Chart 3 (Cleaned Box Plot):** With the extreme outliers removed, the box boundaries are open, readable, and display authentic market spread medians across **Kathmandu, Lalitpur, Pokhara, Bhaktapur, and Chitwan**.
- **Chart 4 (Cleaned Scatter Plot):** By isolating our top 5 cities and converting all traditional units (Aana/Ropani) into uniform **Square Feet**, the data points arranged themselves into a cohesive cluster. Our added red regression line shows a clear, logical market trend: as true land size scales up, property valuation steadily increases.

---

## 5. Conclusion & Next Steps

Our sprint confirms that real-world raw marketplace data cannot be used blindly in engineering pipelines or dashboards without rigorous validation rules. Moving forward into Week 1, our team has built a clean, reproducible workspace repository. The next task will be to convert this cleaning pipeline into production-ready ingestion scripts.