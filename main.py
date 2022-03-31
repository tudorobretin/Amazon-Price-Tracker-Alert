from bs4 import BeautifulSoup
import requests
import smtplib
import os

KEY = os.environ['password']
TARGET_PRICE = 1250
URL = "https://www.amazon.com/Apple-iPhone-12-Pro-Max/dp/B09JF9WMR9/?_encoding=UTF8&pd_rd_w=yM93S&pf_rd_p=50bfa0f0-85f6-48ff-8c9a-ca997a42b714&pf_rd_r=HKMJF730KT6ETTGKXAF4&pd_rd_r=3b5b1736-57d1-4e86-8141-8035e41b82c4&pd_rd_wg=cNiDw&ref_=pd_gw_exports_top_sellers_unrec"


def send_mail():
    my_email = "tudorobretin@gmail.com"
    password = KEY

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        message = f"Iphone price dropped below your target price of ${TARGET_PRICE}!\n" \
                  f"Link: {URL}"
        subject = "Amazon price alert!"
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tudorobre@gmail.com",
            msg=f"Subject:{subject}\n\n{message}"
         )


header = {
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
response = requests.get(url=URL, headers=header)
html = response.text
soup = BeautifulSoup(html, "html.parser")

price = int(soup.find_all(name="span", class_="a-offscreen")[0].getText().strip("$").split(".")[0])

if price <= TARGET_PRICE:
    send_mail()

