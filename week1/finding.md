# Data Audit Findings Report week1

# Data Audit Findings Report

**Course Component: DAVS WEEK1 — Real Estate Data Analysis Pipeline**

## 1. Executive Summary

During this initial orientation sprint, our team conducted a thorough data audit on a raw web-scraped dataset containing 2,211 real estate listings across Nepal. The primary purpose of this investigation was to determine whether the raw dataset could be directly ingested into downstream analytical dashboards or predictive machine learning models.

Our core finding is that **the raw dataset cannot be trusted blindly**. Significant data quality issues, including user text fragmentation, severe typographical price outliers, and incompatible structural unit formats, completely skew standard baseline metrics unless a custom automated cleaning pipeline is established first.

---

## 2. Key Data Quality Findings

### 2.1 The Inconsistent Unit Formatting Problem (Land Area Collision)

- **Discovery:** The raw `Area` column is stored entirely as unstructured text objects rather than uniform numbers. It randomly blends multiple architectural notation systems. Modern listings record land sizes in square feet (e.g., `"1200 Sq. Ft."`), while traditional entries use localized Nepalese measurement terms (e.g., `"4 Aana"`, `"1 Ropani"`, or hyphenated municipal strings like `"1-2-0-0"` denoting *Ropani-Aana-Paisa-Daam*).
- **Analytical Impact:** This structural collision entirely breaks any numerical comparisons or sorting functions. Because Python processes these mixed strings alphabetically, it registers a numerical value of `"4"` (Aana) as mathematically smaller than a `"500"` square feet studio apartment, even though 4 Aana translates to over 1,300 Square Feet.

### 2.2 Typographical Clerical Errors (Extreme Price Outliers)

- **Discovery:** We identified severe data-entry errors within the property `Price` column. Multiple typical suburban residential homes are listed with extreme pricing boundaries—either absurdly undervalued at `1,000 NPR` or astronomically high at over `10,000,000,000+ NPR` (exceeding 10 Billion NPR).
- **Analytical Impact:** If an analyst runs a basic mathematical mean (`.mean()`) across the raw dataset to report average market values, these multi-billion typing slips pull the entire baseline upward. This creates an artificially inflated and deeply inaccurate representation of authentic Nepalese housing valuations.

### 2.3 Structural Feature Data Sparsity (Missing Values)

- **Discovery:** The dataset suffers from massive data gaps across essential categorical and numerical property attributes:
    - **Year Built:** Missing 1,629 observations
    - **Floors:** Missing 1,172 observations
    - **Road Type:** Missing 785 observations
- **Analytical Impact:** Dropping these missing records entirely would erase more than half of our dataset. Instead, our pipeline requires local group imputation (filling structural metrics using the localized geographic **Median** of the specific `City`), ensuring our data volume stays robust without distorting regional housing patterns.

---

## 3. Empirical Visual Evidence

To validate our findings to stakeholders, we isolated and saved individual diagnostic charts before and after running our cleanup processing loops inside the `/content/visualization/` folder:

- **Chart 1 (`chart1_raw_box.png`):** The raw price distribution box plot. Because the multi-billion outliers extend so high, the actual market interquartile boxes for our top 5 cities are squished entirely flat against the zero axis line, rendering the plot completely unreadable without utilizing a logarithmic adjustment.
- **Chart 2 (`chart2_raw_scatter.png`):** The raw price-to-area scatter plot. The data points appear as a chaotic cloud with no discernible shape because localized unit measurements (like small single-digit *Aana* numbers) are plotted on the same exact horizontal scale as multi-thousand square feet indicators.
- **Chart 3 (`chart3_clean_box.png`):** The post-remediation box plot. Trimming the extreme ceiling values opens up the boxes completely, revealing realistic, clean real estate price distributions across **Kathmandu, Lalitpur, Pokhara, Bhaktapur, and Chitwan**.
- **Chart 4 (`chart4_clean_scatter.png`):** The post-remediation scatter plot. Once our regular expression (`re`) parser extracts numbers and transforms all mixed string units uniformly into **Square Feet**, a clean, positive market trend emerges. The red trendline clearly demonstrates that property prices scale logically with true physical size.

---

## 4. Architectural Next Steps

Having established a reproducible cleaning function that resolves these text anomalies, our team's workspace repository is now structurally validated. For the upcoming sprint, we are fully prepared to scale these data transformation scripts into production-ready ingestion pipelines.