from datetime import datetime, timedelta
import requests
import pytz
from lunarcalendar import Converter, Solar

tz = pytz.timezone("Asia/Singapore")

def get_can_chi(date):
    solar = Solar(date.year, date.month, date.day)
    lunar = Converter.Solar2Lunar(solar)
    return lunar.day8Char  # (can, chi)

tomorrow = datetime.now(tz) + timedelta(days=1)

can, chi = get_can_chi(tomorrow)

if chi == "Mão":
    msg = f"Ngày mai ({tomorrow.strftime('%d-%m-%Y')}) là {can} {chi} 🐰"
    requests.post("https://ntfy.sh/lunar-mao-days", data=msg)
else:
    print(f"{tomorrow.strftime('%d-%m-%Y')} là {can} {chi} (không phải ngày Mão)")
