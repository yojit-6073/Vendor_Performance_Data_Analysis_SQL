# Vendor Performance Analysis

An end-to-end data analytics project to evaluate vendor performance, optimize procurement costs, and deliver actionable insights through Python, SQLite, and Power BI.

---

## 📌 Project Overview

**Vendor Performance Analysis** is a comprehensive business analytics solution designed to enhance inventory and sales management in the retail and wholesale industry.  
By analyzing vendor and brand performance, the project identifies cost-saving opportunities, optimizes procurement strategies, and provides stakeholders with insights through a fully interactive Power BI dashboard.

Built using:
- 🐍 Python for data processing  
- 🗄 SQLite for local structured data storage  
- 📊 Power BI for real-time dashboarding  

---

## 🎯 Goals

-  Analyze the impact of bulk purchasing on unit cost savings  
-  Identify underperforming vendors and brands for corrective action  
- Optimize purchase and freight costs to enhance profitability  
- Build an interactive Power BI dashboard for vendor-level KPI tracking  
- Assess inventory turnover to reduce holding costs and improve efficiency  

---

## 🧱 Project Pipeline

### 1. Data Ingestion
- **Input**: `sales.csv`, `purchases.csv`, `begin_inventory.csv`, `end_inventory.csv`, `purchase_prices.csv`, `vendor_invoice.csv`  
- **Script**: `ingestion_db.py` loads the CSVs into a structured `SQLite` database `inventory.db`
- 
  ![image](https://github.com/user-attachments/assets/9edf3cee-f735-4cb5-beef-9a33e9179de7)

- **Tools**: Python, SQLite  

---

### 2. Data Processing & Aggregation
- **Script**: `get_vendor_summary.py`  
- **Output**: Cleaned dataset: `vendor_sales_summary.csv` for dashboarding  

---

### 3. Exploratory Data Analysis (EDA)
- **Notebook**: `Vendor Performance Analysis.ipynb`, `Exploratory Data Analysis.ipynb`  
- **Libraries**: `pandas`, `matplotlib`, `seaborn`, `scipy.stats`  

📌 Performed:
- Statistical testing (e.g., t-tests on vendor margins)  
- Correlation analysis (e.g., 0.999 between purchases and sales)  
- Profitability distribution plots  
- Freight cost vs. unit cost analysis  
- Missing value heatmaps  

---

### 4. Data Cleaning
- Removed nulls, zero/negative margins  
- Standardized columns and optimized dtypes  
- Filtered out unsold stock (sales = 0)  

---

### 5. Power BI Dashboard
- **File**: `vendor_performance_dashboard.pbix`
  ![image](https://github.com/user-attachments/assets/aa318900-7dbf-4f01-abf1-fb60f7e975ca)


📊 Visualizations:
- Top Vendors by Sales and Profit  
- Vendor-wise Freight Contribution  
- Inventory Turnover Trends  
- Drilldowns on low-performing brands  

🔍 Features: Slicers, interactive filters, vendor-level breakdowns  

---

## 🧰 Tech Stack

| Tool         | Purpose                                 |
|--------------|------------------------------------------|
| Python       | Data processing (`pandas`, `scipy`)      |
| SQLite       | Lightweight structured DB                |
| Power BI     | Visualization + stakeholder dashboard    |
| Jupyter      | EDA + prototyping                        |
| VS Code      | Script development                       |

## The Analysis:

### Correlation Matrix:
![image](https://github.com/user-attachments/assets/e5d6f9f7-148d-45d3-81b7-d3982fde84ef)

### Brands that needs Promotional or Pricing Adjustments which exhibit lower sales performance but higher profit margins
![image](https://github.com/user-attachments/assets/a4e53ce6-fdae-4d49-9ec8-823d0d7128ec)

### Which vendors and brands demonstrate the highest sales performance?
![image](https://github.com/user-attachments/assets/70dd5e78-6a40-43d4-bf2b-c902b9d99450)

### How much of total procurement is dependent on the top vendors?
![image](https://github.com/user-attachments/assets/aff51e22-dcc0-4b9f-bbf7-1e8fe4a86f2f)

### Does purchasing in bulk reduce the unit price, and what is the optimal purchase volume for cost savings?
![image](https://github.com/user-attachments/assets/fc15b267-8808-46bb-9a25-949f82e63b17)

### What is the 95% confidence intervals for profit margins of top-performing and low-performing vendors?
![image](https://github.com/user-attachments/assets/d9a3b9f7-f811-417e-b2fc-7ebe4bc7a0b5)

## ✅ Important Notes

- `sales_sample.csv` is provided instead of full `sales.csv` (>1GB)  
- To rebuild inventory.db, run ingestion_db.py with all required datasets placed in datasets/.

## 🚀 Getting Started

To get this project up and running locally, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/yojit-6073/vendor-performance-analysis.git
cd vendor-performance-analysis
```

### 2.Install Required Python Libraries
- Make sure you have Python installed. Then run:
```bash
pip install pandas matplotlib seaborn scipy
```

### 3. Set Up the SQLite Database
- Place all required CSV files into the datasets/ folder and run the ingestion script:
```bash
python ingestion_db.py
```
- This will generate inventory.db containing all the structured tables.

### 4. Run Analysis Scripts / Notebooks
- You can either run the script or explore interactively using Jupyter:
```bash
jupyter notebook Vendor\ Performance\ Analysis.ipynb
python get_vendor_summary.py
```
-This will output the vendor_sales_summary.csv file used for the dashboard.

### 5. Launch Power BI Dashboard
- Open the following file in Power BI Desktop:
```bash
vendor_performance_dashboard.pbix
```

---

## 👨‍💻 Author

**Yojit Kapoor**  
🎓 B.Tech (Information Technology & Business Informatics), IIIT Allahabad  
📧 [yojit49@gmail.com](mailto:yojit49@gmail.com)  
🔗 [GitHub](https://github.com/yojit-6073)  
🔗 [LinkedIn](https://linkedin.com/in/yojit-kapoor-337542293)

---

> Built with 💻 and ☕ by Yojit Kapoor. If you found this project helpful, feel free to ⭐ the repo!


