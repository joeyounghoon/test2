import streamlit as st

# 사이드바에 'OptimalBotAI' 텍스트 추가
st.sidebar.title('OptimalBotAI')

# 사이드바에 셀렉트박스를 추가하여 페이지를 선택할 수 있게 합니다.
page = st.sidebar.selectbox('Select a page:', ['Home', 'Page 1', 'Page 2'])

# 선택된 페이지에 따라 다른 내용을 표시합니다.
if page == 'Home':
    st.title('Home Page')
    st.write("Welcome to the OptimalBotAI homepage!")
elif page == 'Page 1':
    st.title('Page 1')
    st.write("This is Page 1 of the OptimalBotAI website.")
elif page == 'Page 2':
    st.title('Page 2')
    st.write("This is Page 2 of the OptimalBotAI website.")

# 페이지 바 분리를 위한 선픽과 후픽 바 생성
st.sidebar.markdown('---')  # 선픽
st.sidebar.write('Additional Options')  # 후픽

# 선픽 이후의 추가 항목 예제
if st.sidebar.button('Option 1'):
    st.sidebar.write("You selected Option 1")
if st.sidebar.button('Option 2'):
    st.sidebar.write("You selected Option 2")
