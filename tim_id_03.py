import requests
import re

def tim_facebook_id(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(link.strip(), headers=headers)
        id_tim_duoc = re.search(r'"userID":"(\d+)"', response.text)
        return id_tim_duoc.group(1) if id_tim_duoc else "Không tìm thấy"
    except:
        return "Lỗi mạng"

# 1. Nhập nhiều link cách nhau bởi dấu phẩy
danh_sach_nhap = input("Dán các link Facebook vào đây (cách nhau bởi dấu phẩy): ")
cac_link = danh_sach_nhap.split(',')

print(f"\n--- Bắt đầu đi tìm {len(cac_link)} ID cho bạn đây... ---")

# 2. Mở "cuốn sổ" ket_qua.txt để ghi (chế độ 'a' là ghi thêm vào cuối)
with open("ket_qua_id.txt", "a", encoding="utf-8") as file:
    for link in cac_link:
        id_fb = tim_facebook_id(link)
        ket_qua = f"{link.strip()} -> ID: {id_fb}"
        
        print(ket_qua) # Hiện lên màn hình
        file.write(ket_qua + "\n") # Ghi vào file .txt

print("\n--- Đã xong! Bạn kiểm tra file 'ket_qua_id.txt' nhé! ---")