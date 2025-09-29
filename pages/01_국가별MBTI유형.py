import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="국가별 MBTI 비율 대시보드", page_icon="🌍", layout="centered")

st.title("🌍 국가별 MBTI 비율 대시보드")
st.caption("나라를 선택하면 해당 국가의 MBTI 분포를 확인할 수 있어요. 📊")

# 데이터 불러오기
CSV_PATH = "countriesMBTI_16types.csv"
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

try:
    df = load_data(CSV_PATH)
except FileNotFoundError:
    st.error("CSV 파일을 찾을 수 없어요. 같은 폴더에 **countriesMBTI_16types.csv**가 있는지 확인해 주세요.")
    st.stop()

# 컬럼 분리
country_col = "Country"
mbti_cols = [c for c in df.columns if c != country_col]

# 국가 선택
countries = df[country_col].sort_values().tolist()
sel_country = st.selectbox("🌐 국가 선택", countries, index=0)

# 선택 국가 데이터 가공 (세로→긴 형식)
row = df.loc[df[country_col] == sel_country, mbti_cols].iloc[0]
data = (
    row.reset_index()
       .rename(columns={"index": "MBTI", 0: "value"})
       .sort_values("value", ascending=True)  # 가로막대에서 위로 갈수록 큰 값
)

# 색상 팔레트 (부드러운 파스텔톤, 16색)
palette = [
    "#80cbc4", "#aed581", "#ffcc80", "#90caf9",
    "#f48fb1", "#ce93d8", "#ffab91", "#81d4fa",
    "#b39ddb", "#c5e1a5", "#fff59d", "#9fa8da",
    "#ffccbc", "#a5d6a7", "#b0bec5", "#e6ee9c"
]

# Plotly 가로 막대그래프
fig = px.bar(
    data,
    x="value",
    y="MBTI",
    orientation="h",
    color="MBTI",
    color_discrete_sequence=palette,
    labels={"value": "비율", "MBTI": "MBTI 유형"},
    title=f"🇺🇳 {sel_country}의 MBTI 분포 🍀"
)

fig.update_traces(
    texttemplate="%{x:.1%}",
    textposition="outside",
    hovertemplate="유형: %{y}<br>비율: %{x:.2%}<extra></extra>"
)

fig.update_layout(
    xaxis_tickformat=".0%",
    uniformtext_minsize=10,
    uniformtext_mode="hide",
    margin=dict(l=60, r=30, t=70, b=40),
    legend_title_text="유형",
)

st.plotly_chart(fig, use_container_width=True)

# 부가 정보
st.markdown(
    f"""
**{sel_country} 요약**  
- 가장 높은 유형: **{data.iloc[-1]['MBTI']}** ({data.iloc[-1]['value']:.1%})  
- 가장 낮은 유형: **{data.iloc[0]['MBTI']}** ({data.iloc[0]['value']:.1%})  
"""
)

with st.expander("📋 원시 데이터(선택 국가) 보기"):
    show_df = data.copy().sort_values("value", ascending=False)
    show_df["value"] = (show_df["value"] * 100).round(2).astype(str) + "%"
    st.dataframe(show_df.rename(columns={"value": "비율(%)"}), use_container_width=True)

st.caption("Tip: 다른 나라로 바꿔보며 분포의 차이를 비교해 보세요! ✈️")
