import streamlit as st
#to run it: python3 -m streamlit run app.py
# https://docs.streamlit.io/library/get-started

st.title('title of your application')
st.markdown('for example here is a **bold text**')

st.sidebar.title('title of the sidebar')

agree = st.checkbox('Click Me!')

if agree:
    st.write('Great!')
    st.markdown('this is *italic text*')

side_check = st.sidebar.checkbox('Click Checkbox')
if side_check:
    st.sidebar.write('Sidebar checkbox has been clicked')