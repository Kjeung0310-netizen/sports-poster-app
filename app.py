import streamlit as st

st.set_page_config(layout="wide")
st.title("⚾ 응원 포스터 생성기")

col1, col2 = st.columns([1, 2])

with col1:
    user_text = st.text_input("응원 문구를 입력하세요!", "최원준 화이팅!")
    size = st.select_slider("글자 크기", options=["작게", "중간", "크게"])

with col2:
    st.image("https://i.imgur.com/NrESXUa.jpeg", use_container_width=True)
    font_map = {"작게": "30px", "중간": "60px", "크게": "90px"}
    st.markdown(f"""
        <div style="text-align: center; font-size: {font_map[size]}; font-weight: bold; color: white; text-shadow: 3px 3px 5px black; margin-top: -300px;">
            {user_text}
        </div>
    """, unsafe_allow_html=True)
