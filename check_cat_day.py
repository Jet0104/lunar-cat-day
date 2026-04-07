from datetime import datetime, timedelta
import requests
import math

# ===== Julian Day =====
def jd_from_date(dd, mm, yy):
    a = int((14 - mm) / 12)
    y = yy + 4800 - a
    m = mm + 12*a - 3
    jd = dd + int((153*m + 2)/5) + 365*y + int(y/4) - int(y/100) + int(y/400) - 32045
    return jd

# ===== Can Chi ngày =====
def get_day_can_chi(jd):
    can = (jd + 9) % 10
    chi = (jd + 1) % 12

    can_list = ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
    chi_list = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]

    return can_list[can], chi_list[chi]

# ===== Check ngày Mão =====
def is_mao_day(date):
    jd = jd_from_date(date.day, date.month, date.year)
    _, chi = get_day_can_chi(jd)
    return chi == "Mão"

# ===== MAIN =====
# check ngày mai (để báo trước 1 ngày)
tomorrow = datetime.utcnow() + timedelta(days=1)

if is_mao_day(tomorrow):
    msg = f"Ngày mai ({tomorrow.strftime('%d-%m-%Y')}) là ngày Mão 🐰"
    requests.post("https://ntfy.sh/lunar-mao-days", data=msg)
