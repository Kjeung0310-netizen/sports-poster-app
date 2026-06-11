import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

# 사이드바에서 입력받기
with st.sidebar:
    st.header("포스터 설정")
    user_text = st.text_input("응원 문구를 입력하세요!", "최원준 화이팅!")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")

# 이미지 로드
response = requests.get("https://i.imgur.com/NrESXUa.jpeg")
img = Image.open(BytesIO(response.content))

# 메인 화면
col1, col2 = st.columns([1, 2])

with col2:
    st.image(img, use_container_width=True)
    
    # 텍스트 크기 매핑
    font_map = {"작게": "30px", "중간": "60px", "크게": "90px"}
    
    # 포스터 문구 표시
    st.markdown(f"""
        <div style="
            text-align: center; 
            font-size: {font_map[size_option]}; 
            font-weight: bold; 
            color: white; 
            text-shadow: 3px 3px 5px black; 
            margin-top: -300px;
        ">
            {user_text}
        </div>
    """, unsafe_allow_html=True)

    # 이미지 저장 기능
    st.write("---")
    buf = BytesIO()
    img.save(buf, format="JPEG")
    st.download_button(
        label="📥 포스터 파일 저장하기",
        data=buf.getvalue(),
        file_name="poster.jpg",
        mime="image/jpeg"
    )
