import streamlit as st
import pandas as pd

# 제목
st.title("🌍 MBTI 국가별 데이터 미리보기 📊")

# CSV 파일 불러오기 (같은 폴더에 있다고 가정)
df = pd.read_csv("countriesMBTI_16types.csv")

# 설명 문구
st.markdown("안녕하세요! 👋 이 데이터셋은 **국가별 MBTI 유형 분포**를 담고 있어요.")
st.markdown("아래에서 **상위 5줄**을 확인해 보세요 🔎")

# 데이터 상위 5줄 출력
st.subheader("📌 상위 5줄 데이터")
st.dataframe(df.head())
