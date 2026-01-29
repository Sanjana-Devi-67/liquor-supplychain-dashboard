# AI-Enabled Liquor Supply Chain Governance Dashboard

This project is a Proof of Concept (POC) developed to demonstrate how AI and data analytics can improve governance, compliance, and revenue protection in the liquor supply chain.

The system is designed from the perspective of a Revenue Officer in the Liquor Dispatch Department and provides an interactive dashboard for monitoring permit compliance, route deviations, and risk patterns.

---

## 🎯 Problem Statement

The liquor supply chain faces challenges such as:
- Over-dispatch beyond permitted quantities
- Unauthorized route deviations leading to diversion or smuggling
- Manual monitoring and delayed detection of violations

This POC demonstrates how these issues can be identified automatically using data-driven and AI-based techniques.

---

## 🧠 Solution Overview

The solution follows a two-layer architecture:

### 1. Backend Analytics (Offline Processing)
- Permit vs dispatch reconciliation
- AI-based anomaly detection on dispatch patterns
- GPS-based route deviation analysis
- Consolidation of all checks into a final risk classification

The backend generates a consolidated output file:
- `final_governance_output.csv`

### 2. Interactive Dashboard (Frontend)
- Built using Streamlit
- Displays key metrics, visual insights, and detailed tables
- Allows filtering and searching of permits and vehicles
- Includes a manual risk calculator for scenario-based evaluation
- Generates and allows download of a governance summary report

---

## 🖥️ Dashboard Features

- Overview metrics (total permits, high-risk cases, violations)
- Interactive charts for risk distribution and violation reasons
- Searchable and filterable permit & vehicle table
- Manual risk calculator for user-entered values
- Summary report generation and download

---

## 🛠️ Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit
- GitHub (version control)
- Streamlit Cloud (deployment)

---


---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py


