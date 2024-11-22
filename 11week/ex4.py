import qrcode  #pip install qrcode
A = input("학번을 입력하시오 : ")
B = input("이름을 입력하시오 : ")
C = input("전공을 입력하시오 : ")
qr_data = f"학번: {A}이름: {B}전공: {C}"
qr_img = qrcode.make(qr_data)

save_path = 'my_info_data.png'
qr_img.save(save_path)