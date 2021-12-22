import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active

sheet.append(["이름","번호","생년월일"])
a = "이예원"
b = "010-0000-0000"
c = "021107"
sheet.append([a,b,c])
wb.save("test2file.xlsx")