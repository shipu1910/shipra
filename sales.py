import streamlit as st
import pandas as pd
import base64
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# ---------- Page Config ----------
st.set_page_config(
    page_title="Sales Prediction App",
    layout="centered"
)


# ---------- Background Image ----------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("bg.jpg")


# ---------- Title ----------
st.title("📊 Sales Prediction App")


# ---------- Load Data ----------
@st.cache_data
def load_data():
    return pd.read_csv("sales_1000_data.csv")

df = load_data()


# ---------- Dataset Preview ----------
st.subheader("Dataset Preview")
st.dataframe(df)


# ---------- Features and Target ----------
X = df[["AdvertisingSpend", "StoreVisitors", "Discount"]]
Y = df["Sales"]


# ---------- Train-Test Split ----------
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)


# ---------- Model Training ----------
model = LinearRegression()
model.fit(X_train, Y_train)


# ---------- Predictions ----------
pred = model.predict(X_test)


# ---------- Model Evaluation ----------
r2 = r2_score(Y_test, pred)
mse = mean_squared_error(Y_test, pred)
mae = mean_absolute_error(Y_test, pred)


# ---------- Display Metrics ----------
st.subheader("📈 Model Performance")
st.write(f"**R² Score:** {r2 * 100:.2f}%")
st.write(f"**Mean Squared Error:** {mse:.2f}")
st.write(f"**Mean Absolute Error:** {mae:.2f}")


# ---------- User Input ----------
st.subheader("🔮 Predict Sales")

ad_spend = st.number_input("Advertising Spend", min_value=0)
visitors = st.number_input("Store Visitors", min_value=0)
discount = st.number_input("Discount (%)", min_value=0)


# ---------- Prediction ----------
if st.button("Predict Sales"):
    new_data = pd.DataFrame(
        [[ad_spend, visitors, discount]],
        columns=["AdvertisingSpend", "StoreVisitors", "Discount"]
    )

    prediction = model.predict(new_data)[0]

    st.success(f"Predicted Sales Value: {prediction:.2f}")

    if prediction > 0:
        st.info("✅ Sales Profit")
    else:
        st.error("❌ Sales Loss")



