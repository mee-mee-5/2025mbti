import streamlit as st
import pandas as pd
import altair as alt

# 제목
st.title("🌍 MBTI 국가별 Top 10 분포 그래프 📊")

# CSV 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 컬럼 목록 (Country 제외)
mbti_types = df.columns[1:]

# MBTI 유형 선택
selected_mbti = st.selectbox("🔎 MBTI 유형을 선택하세요:", mbti_types)

# 선택한 MBTI 기준 상위 10개 국가
top10 = df[["Country", selected_mbti]].nlargest(10, selected_mbti)

# Altair 그래프
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X("Country:N", sort="-y",
                axis=alt.Axis(
                    labelAngle=-45,      # 글자 대각선
                    labelFontSize=12,    # 글자 크기
                    labelOverlap=False   # 겹치지 않도록
                )),
        y=alt.Y(f"{selected_mbti}:Q", title=f"{selected_mbti} 비율"),
        tooltip=["Country", selected_mbti]
    )
    .properties(
        title=f"Top 10 국가별 {selected_mbti} 분포",
        width=700,   # 그래프 넓게
        height=450
    )
)

st.altair_chart(chart, use_container_width=True)
