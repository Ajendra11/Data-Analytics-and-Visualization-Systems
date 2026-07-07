# Nepal Real Estate Analytics System 🇳🇵
**Course Component: DAVS WEEK1 — Sprint 1 Repository**

Welcome to our data engineering and analytics repository for Nepalese housing market trends. This project centers on auditing, scrubbing, and standardizing messy real estate web-scraped data so it can be reliably used for building business dashboards and machine learning models.

---

## 👥 Team Directory & Roles
* 🏃 **Sprint Coordinator:** Shiv Kumar Yadav — Workflow, Trello tracking, review alignment
* 🐍 **Data Engineer:** *Seraj Haidar Rain* — Jupyter notebook scripting & engineering pipelines
* 🔍 **Analytical Validator:** *Safal Joshi* — Mathematical checks, outlier filters, audit
* 🏗 **System Designer:** *Kashyap Adhikari* — System architecture, scaling limits, data origins
* ✍️ **Documentation Lead:** Ajendra Rai — Workspace architecture & repository markdown translation

---

## 📂 Repository Structure

Our workspace is organized into explicit modules to maintain production standards:

```text
nepal-housing-analytics-system/   
│
├── README.md                     <-- High-level team overview (This file)
├── FINDINGS.md                   <-- Data audit anomalies report 
├── SUMMER.ipynb                  <-- Our finalized, fully executed Jupyter notebook
│
└── visualization/                <-- Generated diagnostic and cleaned plots
    ├── chart1_raw_box.png        <-- Raw skewed distribution box plot
    ├── chart2_raw_scatter.png    <-- Messy mixed-unit coordinate scatter plot
    ├── chart3_clean_box.png      <-- Post-remediation regional price boxes
    └── chart4_clean_scatter.png  <-- Validated structural market trendline