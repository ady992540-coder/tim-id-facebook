import streamlit as st
import requests
import re

st.title("🕵️ Máy Dò ID Facebook Thần Kỳ")
st.write("Dán link vào đây và mình sẽ tìm số ID giúp bạn!")

link_fb = st.text_input("Nhập link Facebook cá nhân:")

if st.button("Bắt đầu tìm kiếm"):
    if link_fb:
        # ĐÂY LÀ PHẦN TRANG ĐIỂM XỊN XÒ MỚI
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.google.com/'
        }
        
        try:
            response = requests.get(link_fb, headers=headers, timeout=10)
            
            # Chúng mình dùng "kính lúp" mạnh hơn để soi nhiều chỗ khác nhau
            # Cách 1: Soi trong userID
            id_tim_duoc = re.search(r'"userID":"(\d+)"', response.text)
            
            # Cách 2: Nếu cách 1 không thấy, soi trong fb://profile/
            if not id_tim_duoc:
                id_tim_duoc = re.search(r'fb://profile/(\d+)', response.text)
                
            if id_tim_duoc:
                st.success(f"🎉 A ha! Tìm thấy rồi! ID là: {id_tim_duoc.group(1)}")
            else:
                st.error("Hic, Facebook vẫn giấu kỹ quá, không tìm thấy rồi!")
        except:
            st.warning("Có vẻ như mạng đang bị nghẽn, bạn thử lại nhé!")