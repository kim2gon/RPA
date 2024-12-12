from fastapi import FastAPI
import qrcode.constants
app = FastAPI()

from fastapi import Form
from fastapi import File,UploadFile
import shutil
from pathlib import Path

from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO

@app.post("/qrcode/")
async def genertae_qr(data: str = Form(...)):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 바이너리 데이터로 변환
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")


def loginDB(userId, userPassword):
    import sqlite3
    
    conn = sqlite3.connect('education.db')
    cursor = conn.cursor()
    
    query = 'SELECT * FROM user WHERE userId = ? AND userPassword = ?'
    cursor.execute(query, (userId, userPassword))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        print("Login successful!")
        print("User Info:",result) # 쿼리 결과 출력
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False
    
@app.post("/login")
def login_form(userid: str = Form(...), userpassword: str = Form(...)):
    result = loginDB (userid, userpassword)
        
    if result == True :
        return {"msg": f"{userid}님 반갑습니다."}
    else :
        return {"msg": f"로그인에 실패했습니다."}

from fastapi.staticfiles import StaticFiles
app.mount("/",StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = '127.0.0.1', port=8000, log_level = "info")