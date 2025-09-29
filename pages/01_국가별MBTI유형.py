import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("🌍 나라별 MBTI 비율 시각화 📊")

# CSV 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 나라 선택
selected_country = st.selectbox("🏳️ 나라를 선택하세요:", df["Country"].unique())

# 해당 나라 데이터 가져오기
country_data = df[df["Country"] == selected_country].iloc[0, 1:]  # Country 제외
mbti_df = pd.DataFrame({
    "MBTI": country_data.index,
    "비율": country_data.values
})

# Plotly 세로 막대그래프
fig = px.bar(
    mbti_df,
    x="MBTI",
    y="비율",
    color="MBTI",
    text="비율",
    color_discrete_sequence=px.colors.qualitative.Pastel,  # 예쁜 파스텔 톤
    title=f"✨ {selected_country} 의 MBTI 비율 ✨"
)

# 그래프 꾸미기
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(
    xaxis_title="MBTI 유형 🧩",
    yaxis_title="비율 (%) 📈",
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    bargap=0.4
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
