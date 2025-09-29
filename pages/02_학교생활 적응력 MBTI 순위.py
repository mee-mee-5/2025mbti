import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("🌍 나라별 MBTI 비율 & 학교생활 적응 순위 반영 📊")

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

# 학교생활 적응이 잘 되는 TOP5 MBTI 유형
school_adapt_top5 = ["ESFJ", "ENFJ", "ESFP", "ENFP", "ESTJ"]

# 색상 매핑: TOP5는 특별히 강조 (나머지는 회색)
mbti_df["색상"] = mbti_df["MBTI"].apply(
    lambda x: "학교생활 적응 TOP5 🌟" if x in school_adapt_top5 else "기타 MBTI"
)

# Plotly 세로 막대그래프
fig = px.bar(
    mbti_df,
    x="MBTI",
    y="비율",
    color="색상",
    text="비율",
    color_discrete_map={
        "학교생활 적응 TOP5 🌟": "#FF9999",  # 따뜻한 핑크 강조
        "기타 MBTI": "#B0C4DE"             # 은은한 회색-파랑
    },
    title=f"✨ {selected_country} 의 MBTI 분포 (학교생활 적응 순위 반영) ✨"
)

# 그래프 꾸미기
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(
    xaxis_title="MBTI 유형 🧩",
    yaxis_title="비율 (%) 📈",
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    bargap=0.4,
    legend_title="분류"
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
