# ⚽ Mini Sports Analytics Dashboard

An interactive, responsive Flask web application designed for processing, analyzing, and visualizing tournament sports data (FIFA World Cup dataset). The platform combines interactive **Chart.js** visuals, customizable **DataTables.net** statistical tables, and dynamic **Jinja2** templating inside a clean **Bootstrap 5** user interface.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-4.x-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)

---

## 🌟 Key Features

* **📊 Exploratory Data Analysis (EDA):**
  * **Dynamic Year Filtering:** Filter all KPIs, charts, and tables by specific tournament edition years.
  * **Interactive Visualizations:** Descending-sorted **Chart.js** bar charts (Top Participating Teams) and doughnut charts (Tournament Stage Breakdown).
  * **Visual Venue Tables:** Custom tables with inline Bootstrap progress bars scaled dynamically according to max venue/city values.
* **📋 Statistical Analysis & Temporal KPIs:**
  * Interactive **DataTables.net** integration featuring live searching, multi-column sorting (e.g., Primary: Matches DESC | Secondary: Name ASC), and fast pagination.
  * Overflow-protected layout ensuring smooth performance across standard display sizes.
* **🧹 Data Preprocessing:**
  * Clean processing pipeline handling raw match data, missing values, and calculated summary metrics (KPIs).

---

## 🛠️ Technology Stack

| Domain | Technologies Used |
| :--- | :--- |
| **Backend** | Python 3, Flask, Jinja2 |
| **Data Processing** | Pandas, NumPy |
| **Frontend UI** | HTML5, CSS3, Bootstrap 5 |
| **Data Visuals & Tables** | Chart.js, DataTables.net, jQuery |

---

## 📁 Repository Structure

```text
├── app/
│   ├── __init__.py          # Flask Application Factory
│   ├── routes.py            # Route Handlers (Home, Preprocessing, EDA, Stats)
│   └── utils/
│       └── eda_helpers.py   # Dataset load & KPI extraction pipeline
├── templates/
│   ├── base.html            # Core Layout & Navigation
│   ├── index.html           # Dashboard Landing Page
│   ├── eda.html             # EDA View (Charts, Summary KPIs, Venue Tables)
│   ├── statistics.html      # Statistical View (DataTables with Filters)
│   └── preprocessing.html   # Data Pipeline Overview
├── static/
│   ├── css/                 # Custom Styling Adjustments
│   └── data/                # Raw & Cleaned Datasets (.csv)
├── requirements.txt         # Dependencies List
├── run.py                   # App Entry Point
└── README.md                # Project Documentation