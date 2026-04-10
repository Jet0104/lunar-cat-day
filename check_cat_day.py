from datetime import datetime, timedelta
import requests
import pytz

# ===== Julian Day =====
def jd_from_date(dd, mm, yy):
    a = int((14 - mm) / 12)
    y = yy + 4800 - a
    m = mm + 12*a - 3
    jd = dd + int((153*m + 2)/5) + 365*y + int(y/4) - int(y/100) + int(y/400) - 32045
    return jd

# ===== Can Chi chuẩn =====
def get_can_chi(date):
    jd = jd_from_date(date.day, date.month, date.year)

    can_list = ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
    chi_list = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]

    can = can_list[(jd + 9) % 10]
    chi = chi_list[(jd + 1) % 12]

    return can, chi

# ===== TIMEZONE FIX =====
tz = pytz.timezone("Asia/Singapore")
tomorrow = datetime.now(tz) + timedelta(days=1)

can, chi = get_can_chi(tomorrow)

if chi == "Mão":
    msg = f"Ngày mai ({tomorrow.strftime('%d-%m-%Y')}) là {can} {chi} 🐰"
    requests.post("https://ntfy.sh/lunar-mao-days", data=msg)
else:
    print(f"{tomorrow.strftime('%d-%m-%Y')} là {can} {chi}")
