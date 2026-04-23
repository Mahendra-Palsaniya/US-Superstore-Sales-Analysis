import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main-title {
    text-align: center;
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    padding: 20px;
    border-radius: 12px;
    color: white;
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 15px;
}

.sub-text {
    text-align: center;
    color: gray;
    margin-bottom: 25px;
}

.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.15);
}

.metric {
    font-size: 28px;
    font-weight: bold;
    color: #2575fc;
}

.label {
    color: gray;
    font-size: 14px;
}

.chart-box {
    background-color: #0f172a;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
}

.chart-title {
    color: white;
    font-size: 15px;
    margin-bottom: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="main-title">Superstore Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Explore sales, profit, customers and regional performance</div>', unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
df = pd.read_excel("Superstore.xlsx")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔎 Filters")

year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

segment = st.sidebar.multiselect(
    "Segment",
    df["Segment"].unique(),
    default=df["Segment"].unique()
)

region = st.sidebar.multiselect(
    "Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

# ---------------- FILTER DATA ----------------
filtered = df[
    (df["Year"] == year) &
    (df["Segment"].isin(segment)) &
    (df["Region"].isin(region))
]

if filtered.empty:
    st.warning("No data available")
    st.stop()

# ---------------- KPI CARDS ----------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="metric">${filtered['Sales'].sum():,.0f}</div>
        <div class="label">Total Sales</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="metric">${filtered['Profit'].sum():,.0f}</div>
        <div class="label">Total Profit</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="metric">{filtered['Order ID'].nunique()}</div>
        <div class="label">Total Orders</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="metric">${filtered['Sales'].mean():.2f}</div>
        <div class="label">Avg Order Value</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- ROW 1 ----------------
col1, col2 = st.columns(2)

# MAP
with col1:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Sales by State</div>', unsafe_allow_html=True)

    state_sales = filtered.groupby("State")["Sales"].sum().reset_index()

    fig1 = px.choropleth(
        state_sales,
        locations="State",
        locationmode="USA-states",
        color="Sales",
        color_continuous_scale="Blues",
        scope="usa"
    )

    fig1.update_layout(template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# CATEGORY-YEAR
with col2:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Sales by Category & Year</div>', unsafe_allow_html=True)

    cat_year = df.groupby(["Year", "Category"])["Sales"].sum().reset_index()

    fig2 = px.bar(cat_year, x="Year", y="Sales", color="Category")
    fig2.update_layout(template="plotly_dark")

    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ROW 2 ----------------
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Segment Distribution</div>', unsafe_allow_html=True)

    seg = filtered.groupby("Segment")["Sales"].sum().reset_index()
    fig3 = px.pie(seg, names="Segment", values="Sales", hole=0.6)
    fig3.update_layout(template="plotly_dark")

    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Category Share</div>', unsafe_allow_html=True)

    cat = filtered.groupby("Category")["Sales"].sum().reset_index()
    fig4 = px.pie(cat, names="Category", values="Sales", hole=0.6)
    fig4.update_layout(template="plotly_dark")

    st.plotly_chart(fig4, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ROW 3 ----------------
col5, col6 = st.columns(2)

with col5:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Shipping Mode Distribution</div>', unsafe_allow_html=True)

    ship = filtered["Ship Mode"].value_counts().reset_index()
    ship.columns = ["Ship Mode", "Count"]

    fig5 = px.bar(ship, x="Ship Mode", y="Count")
    fig5.update_layout(template="plotly_dark")

    st.plotly_chart(fig5, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Sales vs Profit</div>', unsafe_allow_html=True)

    scatter = filtered.groupby("Category")[["Sales", "Profit"]].sum().reset_index()

    fig6 = px.scatter(scatter, x="Sales", y="Profit", size="Sales", color="Category")
    fig6.update_layout(template="plotly_dark")

    st.plotly_chart(fig6, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)