import streamlit as st
import pandas as pd
import altair as alt

# 제목
st.title("🌍 MBTI 유형 상위 10개 시각화 📊")

# CSV 파일 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 컬럼만 추출
mbti_cols = [col for col in df.columns if col != "Country"]

# 각 MBTI 유형별 평균값 계산
mbti_mean = df[mbti_cols].mean().reset_index()
mbti_mean.columns = ["MBTI", "Average"]

# 상위 10개 유형 선택
top10 = mbti_mean.sort_values(by="Average", ascending=False).head(10)

# Altair 막대그래프
chart = (
    alt.Chart(top10)
    .mark_bar(color="teal")
    .encode(
        x=alt.X("Average:Q", title="평균 비율"),
        y=alt.Y("MBTI:N", sort="-x", title="MBTI 유형"),
        tooltip=["MBTI", "Average"]
    )
    .properties(
        title="📊 MBTI 유형별 평균 상위 10개"
    )
)

# 출력
st.altair_chart(chart, use_container_width=True)
