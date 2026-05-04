import requests
import re

def tim_facebook_id(link):
    print(f"--- Đang đi tìm ID cho bạn đây... ---")
    
    # Giả vờ làm một người dùng bình thường để Facebook không đuổi ra
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # Robot đi lấy dữ liệu từ trang web về
        response = requests.get(link, headers=headers)
        noidung = response.text
        
        # Robot dùng kính lúp soi tìm dãy số sau chữ 'userID'
        id_tim_duoc = re.search(r'"userID":"(\d+)"', noidung)
        
        if id_tim_duoc:
            return id_tim_duoc.group(1)
        else:
            return "Hic, không tìm thấy rồi!"
    except:
        return "Lỗi rồi, bạn kiểm tra lại mạng nhé!"

# Phần để bạn nhập link
link_fb = input("Dán link Facebook vào đây đi: ")
ket_qua = tim_facebook_id(link_fb)
print(f"Số ID bí mật là: {ket_qua}")