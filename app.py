import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analisis Pengangguran & Pendidikan", layout="wide")

st.title("📊 Analisis Tingkat Pengangguran Berdasarkan Pendidikan")

# Upload data
st.sidebar.header("📂 Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📁 Data Mentah")
    st.dataframe(df)

    # Pilih kolom
    st.sidebar.header("⚙️ Pengaturan Kolom")
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_columns) < 2:
        st.error("Dataset harus memiliki minimal dua kolom numerik.")
    else:
        education_col = st.sidebar.selectbox("Kolom Tingkat Pendidikan", numeric_columns)
        unemployment_col = st.sidebar.selectbox("Kolom Tingkat Pengangguran", numeric_columns)


    # Korelasi
    correlation = df[education_col].corr(df[unemployment_col])
    st.metric(label="📈 Korelasi Pendidikan vs Pengangguran", value=f"{correlation:.3f}")

    # Scatter plot
    st.subheader("🔍 Scatter Plot Pendidikan vs Pengangguran")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=education_col, y=unemployment_col, ax=ax)
    st.pyplot(fig)

    # Regresi Linear
    X = df[[education_col]].values
    y = df[unemployment_col].values
    model = LinearRegression()
    model.fit(X, y)
    pred_y = model.predict(X)

    st.subheader("📉 Hasil Regresi Linear")
    st.write(f"Persamaan regresi: **y = {model.coef_[0]:.3f} * x + {model.intercept_:.3f}**")
    st.write(f"R-squared: **{model.score(X, y):.3f}**")

    fig2, ax2 = plt.subplots()
    sns.regplot(x=X.flatten(), y=y, ax=ax2, line_kws={"color": "red"})
    st.pyplot(fig2)

else:
    st.warning("Silakan upload file CSV terlebih dahulu.")
