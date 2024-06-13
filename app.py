import streamlit as st

# 사이드바에 'OptimalBotAI' 텍스트 추가
st.sidebar.title('OptimalBotAI')


# 페이지 바 분리를 위한 선픽과 후픽 바 생성
st.sidebar.markdown('---')  # 선픽

# 선픽 이후의 추가 항목 예제
st.sidebar.page_link('pages/선픽.py')
   
st.sidebar.page_link('pages/후픽.py')
  
