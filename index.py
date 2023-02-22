import streamlit as st

# 创建导航菜单
menu = ['Home', 'Page 1', 'Page 2', 'Page 3']
choice = st.sidebar.selectbox('Select Page', menu)

# 显示页面内容
if choice == 'Home':
    st.title('Welcome to the Home Page')
    st.write('This is the homepage of my app.')
elif choice == 'Page 1':
    st.title('Welcome to Page 1')
    st.write('This is page 1 of my app.')
elif choice == 'Page 2':
    st.title('Welcome to Page 2')
    st.write('This is page 2 of my app.')
else:
    st.title('Welcome to Page 3')
    st.write('This is page 3 of my app.')