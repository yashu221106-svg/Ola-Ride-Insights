
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Ola Ride Insights",
    page_icon="🚕",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/OLA_Cleaned_Data.csv")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df

df = load_data()

st.title("🚕 Ola Ride Insights Dashboard")
st.caption("Ride-Sharing and Mobility Analytics")

st.success("Dataset loaded successfully!")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

vehicle_options = ["All"] + sorted(df["Vehicle_Type"].dropna().unique().tolist())
status_options = ["All"] + sorted(df["Booking_Status"].dropna().unique().tolist())
payment_options = ["All"] + sorted(df["Payment_Method"].dropna().unique().tolist())

selected_vehicle = st.sidebar.selectbox("Vehicle Type", vehicle_options)
selected_status = st.sidebar.selectbox("Booking Status", status_options)
selected_payment = st.sidebar.selectbox("Payment Method", payment_options)

filtered_df = df.copy()

if selected_vehicle != "All":
    filtered_df = filtered_df[filtered_df["Vehicle_Type"] == selected_vehicle]

if selected_status != "All":
    filtered_df = filtered_df[filtered_df["Booking_Status"] == selected_status]

if selected_payment != "All":
    filtered_df = filtered_df[filtered_df["Payment_Method"] == selected_payment]

# KPI metrics
st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Bookings", f"{len(filtered_df):,}")

successful = filtered_df[
    filtered_df["Booking_Status"] == "Success"
]

col2.metric("Successful Bookings", f"{len(successful):,}")

revenue = successful["Booking_Value"].sum()
col3.metric("Successful Ride Revenue", f"₹{revenue:,.0f}")

# Booking status chart
st.subheader("Booking Status Breakdown")

status_data = filtered_df["Booking_Status"].value_counts().reset_index()
status_data.columns = ["Booking Status", "Bookings"]

fig = px.pie(
    status_data,
    names="Booking Status",
    values="Bookings",
    hole=0.4,
    title="Booking Status Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# Daily ride volume
st.subheader("Ride Volume Over Time")

daily_data = (
    filtered_df.groupby("Date")["Booking_ID"]
    .count()
    .reset_index(name="Bookings")
)

fig2 = px.line(
    daily_data,
    x="Date",
    y="Bookings",
    markers=True,
    title="Daily Ride Volume"
)

st.plotly_chart(fig2, use_container_width=True)

# Dataset preview
st.subheader("Filtered Ride Data")
st.dataframe(filtered_df.head(100), use_container_width=True)

st.caption("Ola Ride Insights | Project Dashboard")


# Revenue by Payment Method
st.subheader("Revenue by Payment Method")

revenue_data = (
    successful.groupby("Payment_Method")["Booking_Value"]
    .sum()
    .reset_index()
)

fig3 = px.bar(
    revenue_data,
    x="Payment_Method",
    y="Booking_Value",
    title="Revenue by Payment Method",
    text_auto=".2s"
)

st.plotly_chart(fig3, use_container_width=True)


# Top 5 Customers by Total Booking Value
st.subheader("Top 5 Customers by Total Booking Value")

top_customers = (
    successful.groupby("Customer_ID")["Booking_Value"]
    .sum()
    .nlargest(5)
    .reset_index()
)

fig4 = px.bar(
    top_customers,
    x="Customer_ID",
    y="Booking_Value",
    title="Top 5 Customers by Total Booking Value",
    text_auto=".2s"
)

st.plotly_chart(fig4, use_container_width=True)

# Top 5 Vehicle Types by Ride Distance
st.subheader("Top 5 Vehicle Types by Ride Distance")

vehicle_distance = (
    filtered_df.groupby("Vehicle_Type")["Ride_Distance"]
    .sum()
    .nlargest(5)
    .reset_index()
)

fig5 = px.bar(
    vehicle_distance,
    x="Vehicle_Type",
    y="Ride_Distance",
    title="Top 5 Vehicle Types by Ride Distance",
    text_auto=".2s"
)

st.plotly_chart(fig5, use_container_width=True)

# Incomplete Rides by Reason
st.subheader("Incomplete Rides by Reason")

incomplete_data = (
    filtered_df[filtered_df["Incomplete_Rides"] == "Yes"]
    ["Incomplete_Rides_Reason"]
    .value_counts()
    .reset_index()
)

incomplete_data.columns = ["Reason", "Number of Rides"]

fig6 = px.bar(
    incomplete_data,
    x="Reason",
    y="Number of Rides",
    title="Incomplete Rides by Reason",
    text_auto=True
)

st.plotly_chart(fig6, use_container_width=True)

# Driver Ratings Distribution
st.subheader("Driver Ratings Distribution")

driver_ratings = (
    filtered_df["Driver_Ratings"]
    .dropna()
    .value_counts()
    .sort_index()
    .reset_index()
)

driver_ratings.columns = ["Rating", "Number of Rides"]

fig7 = px.bar(
    driver_ratings,
    x="Rating",
    y="Number of Rides",
    title="Driver Ratings Distribution"
)

st.plotly_chart(fig7, use_container_width=True)


# Customer Ratings Distribution
st.subheader("Customer Ratings Distribution")

customer_ratings = (
    filtered_df["Customer_Rating"]
    .dropna()
    .value_counts()
    .sort_index()
    .reset_index()
)

customer_ratings.columns = ["Rating", "Number of Rides"]

fig8 = px.bar(
    customer_ratings,
    x="Rating",
    y="Number of Rides",
    title="Customer Ratings Distribution"
)

st.plotly_chart(fig8, use_container_width=True)

# Customer vs Driver Ratings
st.subheader("Customer vs Driver Ratings")

rating_comparison = filtered_df[
    ["Customer_Rating", "Driver_Ratings"]
].dropna()

fig9 = px.scatter(
    rating_comparison,
    x="Customer_Rating",
    y="Driver_Ratings",
    title="Customer vs Driver Ratings",
    labels={
        "Customer_Rating": "Customer Rating",
        "Driver_Ratings": "Driver Rating"
    }
)

st.plotly_chart(fig9, use_container_width=True)

# SQL Query Results Section
st.header("📊 SQL Query Results")

sql_success = filtered_df[
    filtered_df["Booking_Status"] == "Success"
]

# Q1 - Successful Bookings
st.subheader("Q1 – Successful Bookings")
st.metric("Total Successful Bookings", len(sql_success))
st.dataframe(sql_success.head(10), use_container_width=True)

# Q2 - Average Ride Distance by Vehicle Type
st.subheader("Q2 – Average Ride Distance by Vehicle Type")

q2 = (
    sql_success.groupby("Vehicle_Type")["Ride_Distance"]
    .mean()
    .reset_index(name="Average_Ride_Distance")
    .sort_values("Average_Ride_Distance", ascending=False)
)

st.dataframe(q2, use_container_width=True)

# Q3 - Customer Cancellations
st.subheader("Q3 – Customer Cancellations")

q3 = filtered_df[
    filtered_df["Booking_Status"] == "Canceled by Customer"
]

st.metric("Total Customer Cancellations", len(q3))

# Q4 - Top 5 Customers by Successful Rides
st.subheader("Q4 – Top 5 Customers by Successful Rides")

q4 = (
    sql_success.groupby("Customer_ID")
    .size()
    .reset_index(name="Total_Rides")
    .sort_values("Total_Rides", ascending=False)
    .head(5)
)

st.dataframe(q4, use_container_width=True)

# Q5 - Driver Cancellations for Personal & Car Related Issue
st.subheader("Q5 – Driver Cancellations")

q5 = filtered_df[
    (filtered_df["Booking_Status"] == "Canceled by Driver") &
    (filtered_df["Canceled_Rides_by_Driver"] == "Personal & Car related issue")
]

st.metric("Personal & Car Related Cancellations", len(q5))

# Q6 - Prime Sedan Driver Ratings
st.subheader("Q6 – Prime Sedan Driver Ratings")

prime_sedan = sql_success[
    sql_success["Vehicle_Type"] == "Prime Sedan"
]["Driver_Ratings"].dropna()

if not prime_sedan.empty:
    st.write("Maximum Rating:", prime_sedan.max())
    st.write("Minimum Rating:", prime_sedan.min())

# Q7 - UPI Bookings
st.subheader("Q7 – UPI Bookings")

q7 = filtered_df[
    filtered_df["Payment_Method"] == "UPI"
]

st.metric("Total UPI Bookings", len(q7))
st.dataframe(q7.head(10), use_container_width=True)

# Q8 - Average Customer Rating by Vehicle Type
st.subheader("Q8 – Average Customer Rating by Vehicle Type")

q8 = (
    sql_success.groupby("Vehicle_Type")["Customer_Rating"]
    .mean()
    .reset_index(name="Average_Customer_Rating")
    .sort_values("Average_Customer_Rating", ascending=False)
)

st.dataframe(q8, use_container_width=True)

# Q9 - Successful Booking Revenue
st.subheader("Q9 – Total Successful Booking Value")

q9 = sql_success["Booking_Value"].sum()

st.metric("Total Successful Booking Revenue", f"₹{q9:,.2f}")

# Q10 - Incomplete Rides by Reason
st.subheader("Q10 – Incomplete Rides by Reason")

q10 = (
    filtered_df[filtered_df["Incomplete_Rides"] == "Yes"]
    ["Incomplete_Rides_Reason"]
    .value_counts()
    .reset_index()
)

q10.columns = ["Incomplete_Rides_Reason", "Total_Incomplete_Rides"]

st.dataframe(q10, use_container_width=True)