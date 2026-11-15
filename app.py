import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍽️")

st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 눌러 오늘의 점심 메뉴를 랜덤으로 추천받아 보세요!")

# 추천할 점심 메뉴 리스트
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "초밥",
    "파스타",
    "쌀국수",
    "햄버거",
    "비빔밥",
    "마라탕",
    "순대국밥",
    "짜장면",
    "짬뽕",
    "칼국수",
    "샌드위치 & 샐러드",
    "카레라이스",
    "부대찌개",
    "라멘",
]

# 버튼 클릭 시 랜덤 메뉴 출력
if st.button("🎲 메뉴 추천받기", type="primary"):
    selected_menu = random.choice(lunch_menus)
    st.balloons()
    st.success(
        f"오늘의 추천 점심 메뉴는 **{selected_menu}**입니다! 맛있게 드세요 😋"
    )
