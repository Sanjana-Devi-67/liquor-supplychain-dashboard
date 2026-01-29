import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI-Enabled Liquor Supply Chain Dashboard",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("final_governance_output.csv")

df = load_data()

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Manual Risk Calculator"]
)

# ==================================================
# ================= DASHBOARD PAGE =================
# ==================================================
if page == "Dashboard":

    st.title("🍾 AI-Enabled Liquor Supply Chain Governance Dashboard")
    st.write("Interactive dashboard for monitoring permit compliance, route deviations, and risk patterns.")

    # ---------------- TOP METRICS ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Permits", df["permit_id"].nunique())
    col2.metric("High Risk Cases", (df["final_risk"] == "High Risk").sum())
    col3.metric("Permit Violations", (df["permit_status"] == "Violation").sum())
    col4.metric("Route Deviations", (df["route_status"] == "Deviated").sum())

    # ---------------- USER CONTROLS ----------------
    st.subheader("⚙️ User Controls")

    colA, colB = st.columns(2)

    with colA:
        risk_filter = st.selectbox(
            "Filter by Risk Level",
            options=["All", "High Risk", "Normal"]
        )

    with colB:
        search_text = st.text_input("Search by Permit ID or Vehicle ID")

    # ---------------- APPLY FILTERS ----------------
    filtered_df = df.copy()

    if risk_filter != "All":
        filtered_df = filtered_df[filtered_df["final_risk"] == risk_filter]

    if search_text:
        filtered_df = filtered_df[
            filtered_df["permit_id"].astype(str).str.contains(search_text, case=False) |
            filtered_df["vehicle_id"].astype(str).str.contains(search_text, case=False)
        ]

    # ---------------- VISUALIZATION: RISK DISTRIBUTION ----------------
    st.subheader("📊 Risk Distribution")

    risk_counts = filtered_df["final_risk"].value_counts()

    fig1, ax1 = plt.subplots()
    risk_counts.plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Risk Level")
    ax1.set_ylabel("Count")

    st.pyplot(fig1)

    # ---------------- VISUALIZATION: REASONS ----------------
    st.subheader("⚠️ Reasons for Risk Detection")

    reason_counts = {
        "Permit Violations": (filtered_df["permit_status"] == "Violation").sum(),
        "AI Anomalies": (filtered_df["anomaly_status"] == "Anomaly").sum(),
        "Route Deviations": (filtered_df["route_status"] == "Deviated").sum()
    }

    fig2, ax2 = plt.subplots()
    pd.Series(reason_counts).plot(kind="bar", ax=ax2)
    ax2.set_ylabel("Count")

    st.pyplot(fig2)

    # ---------------- DATA TABLE ----------------
    st.subheader("📋 Detailed Permit & Vehicle Data")

    st.dataframe(
        filtered_df[
            ["permit_id", "vehicle_id", "permit_status",
             "anomaly_status", "route_status", "final_risk"]
        ],
        use_container_width=True
    )

    # ---------------- REPORT GENERATION ----------------
    st.subheader("📄 Generate Summary Report")

    if st.button("Generate Report"):

        top_risky = filtered_df[filtered_df["final_risk"] == "High Risk"] \
            .head(5)[["permit_id", "vehicle_id"]]

        report_text = f"""
AI-Enabled Liquor Supply Chain Governance – Summary Report
---------------------------------------------------------

Total permits analyzed        : {df["permit_id"].nunique()}
High risk cases identified    : {(df["final_risk"] == "High Risk").sum()}
Permit violations detected    : {(df["permit_status"] == "Violation").sum()}
AI anomalies detected         : {(df["anomaly_status"] == "Anomaly").sum()}
Route deviations detected     : {(df["route_status"] == "Deviated").sum()}

Top High-Risk Permits & Vehicles:
{top_risky.to_string(index=False)}

Recommended Actions:
- Inspect high-risk vehicles immediately
- Audit permits with repeated violations
- Increase monitoring for deviated routes
- Use compliance trends for predictive enforcement

(This report is generated using simulated district-level data for POC purposes.)
"""

        st.session_state["report"] = report_text
        st.success("Report generated successfully")

    # ---------------- DOWNLOAD REPORT ----------------
    if "report" in st.session_state:
        st.download_button(
            label="⬇️ Download Report",
            data=st.session_state["report"],
            file_name="governance_summary_report.txt",
            mime="text/plain"
        )

# ==================================================
# ============ MANUAL RISK CALCULATOR PAGE =========
# ==================================================
if page == "Manual Risk Calculator":

    st.title("🧮 Manual Risk Calculator")
    st.write("Manually evaluate compliance and risk for a single dispatch case.")

    permitted_qty = st.number_input(
        "Permitted Quantity",
        min_value=0,
        value=1000
    )

    dispatched_qty = st.number_input(
        "Dispatched Quantity",
        min_value=0,
        value=1000
    )

    route_deviation = st.number_input(
        "Route Deviation Distance",
        min_value=0.0,
        value=0.1,
        step=0.01
    )

    deviation_threshold = st.slider(
        "Allowed Route Deviation Threshold",
        min_value=0.05,
        max_value=1.0,
        value=0.2,
        step=0.05
    )

    if st.button("Calculate Risk"):

        permit_status = "Violation" if dispatched_qty > permitted_qty else "Normal"
        route_status = "Deviated" if route_deviation > deviation_threshold else "Normal"

        final_risk = "High Risk" if (
            permit_status == "Violation" or route_status == "Deviated"
        ) else "Normal"

        st.subheader("📊 Evaluation Result")

        st.write(f"**Permit Status:** {permit_status}")
        st.write(f"**Route Status:** {route_status}")
        st.write(f"**Final Risk:** {final_risk}")
