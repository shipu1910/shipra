import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Title
st.title("🏠 House Price Prediction App")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("house_price.csv")
    return df

df = load_data()

st.write("### Dataset Preview")
st.dataframe(df.head())

st.write("Shape of dataset:", df.shape)

# Feature selection
X = df[['Size_sqft', 'Bedrooms', 'Age_years']]
y = df['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

st.write("### Enter House Details")

# User Inputs
size = st.number_input("Size (sqft)", min_value=500, max_value=10000, value=2500)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
age = st.number_input("Age (years)", min_value=0, max_value=100, value=5)

# Prediction
if st.button("Predict Price"):
    new_data = np.array([[size, bedrooms, age]])
    prediction = model.predict(new_data)
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")

    import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# App Title
st.title("🩺 Disease Prediction App")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("disease_prediction.csv")
    return df

df = load_data()

st.write("### Dataset Preview")
st.dataframe(df.head())
st.write("Shape of dataset:", df.shape)

# Features & Target
X = df.drop("Disease", axis=1)
y = df["Disease"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

st.write("## Enter Symptoms")

# Create input fields dynamically based on dataset columns
user_input = []

for column in X.columns:
    value = st.selectbox(f"{column}", [0, 1])
    user_input.append(value)

# Prediction
if st.button("Predict Disease"):
    input_data = np.array([user_input])
    prediction = model.predict(input_data)
    st.success(f"Predicted Disease: {prediction[0]}")

