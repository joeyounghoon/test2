import streamlit as st

# 사이드바에 'OptimalBotAI' 텍스트 추가
st.sidebar.title('OptimalBotAI')


# 페이지 바 분리를 위한 선픽과 후픽 바 생성
st.sidebar.markdown('---')  # 선픽

# 선픽 이후의 추가 항목 예제
if st.sidebar.button('선픽'):
    st.sidebar.write("You selected Option 1")
if st.sidebar.button('후픽'):
    st.sidebar.write("You selected Option 2")
