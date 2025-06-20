# Stramlit 예측 UI
import streamlit as st
import pandas as pd
import pickle
from sklearn.datasets import load_iris

st.title("🌸 Iris 분류기 (with MLOps)")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

iris = load_iris()
input_df = st.dataframe(
    pd.DataFrame([iris.data[0]], columns = iris.feature_names)
)

# 사용자 입력
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

input_features = [[sepal_length, sepal_width, petal_length, petal_width]]

if st.button("예측하기"):
    pred = model.predict(input_features)[0]
    st.success(f"예측결과 : {iris.target_names[pred]}")
