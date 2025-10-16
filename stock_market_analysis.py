import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Global Stock Dashboard", layout="centered")
st.title("🌍 Global Stock Market Analysis")

# Step 1: Free-text input for any ticker
ticker = st.text_input("Enter any stock ticker (e.g., AAPL, TSLA, INFY.NS, RELIANCE.NS):", "AAPL")

# Step 2: Fetch and display data
if ticker:
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="1mo")

        if not df.empty:
            st.subheader(f"📊 Price History for {ticker}")
            st.dataframe(df)

            # Step 3: Line chart of closing prices
            st.line_chart(df["Close"])

            # Step 4: Volume bar chart
            st.subheader("📊 Trading Volume")
            st.bar_chart(df["Volume"])

            # Step 5: Moving Averages
            df["SMA_5"] = df["Close"].rolling(window=5).mean()
            df["SMA_10"] = df["Close"].rolling(window=10).mean()
            st.subheader("📉 Moving Averages")
            st.line_chart(df[["Close", "SMA_5", "SMA_10"]])

            # Step 6: Candlestick Chart
            st.subheader("📈 Candlestick Chart")
            fig = go.Figure(data=[go.Candlestick(
                x=df.index,
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"]
            )])
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("No data found. Please check the ticker symbol.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")




