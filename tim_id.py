import streamlit as st
import requests
import re

# Tạo tiêu đề cho trang web
st.title("🕵️ Máy Dò ID Facebook Thần Kỳ")
st.write("Dán link vào đây và mình sẽ tìm số ID giúp bạn!")

# Tạo ô nhập liệu
link_fb = st.text_input("Nhập link Facebook cá nhân:")

if st.button("Bắt đầu tìm kiếm"):
    if link_fb:
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(link_fb, headers=headers)
            id_tim_duoc = re.search(r'"userID":"(\d+)"', response.text)
            
            if id_tim_duoc:
                st.success(f"🎉 Tìm thấy rồi! ID là: {id_tim_duoc.group(1)}")
            else:
                st.error("Hic, không tìm thấy ID nào cả.")
        except:
            st.warning("Có lỗi xảy ra, kiểm tra lại link nhé!")