import streamlit as st
import pandas as pd
import altair as alt

# 제목
st.title("🌍 MBTI 유형별 상위 10개 국가 📊")

# CSV 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 유형 리스트 (Country 제외)
mbti_types = [col for col in df.columns if col != "Country"]

# 드롭다운 메뉴
selected_type = st.selectbox("🔎 MBTI 유형을 선택하세요", mbti_types)

# 선택한 유형의 상위 10개 국가 추출
top10 = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)

# Altair 그래프 생성
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X("Country", sort="-y", title="국가"),
        y=alt.Y(selected_type, title=f"{selected_type} 비율"),
        tooltip=["Country", selected_type]
    )
    .properties(
        title=f"🌟 {selected_type} 상위 10개 국가",
        width=600,
        height=400
    )
)

# 그래프 출력
st.altair_chart(chart, use_container_width=True)

# 상위 10개 데이터도 표로 함께 보여주기
st.subheader("📌 상위 10개 국가 데이터")
st.dataframe(top10.reset_index(drop=True))
