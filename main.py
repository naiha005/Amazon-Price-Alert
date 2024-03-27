import smtplib
import requests
import lxml
import os
from dotenv import load_dotenv
from smtplib import SMTP
from bs4 import BeautifulSoup

load_dotenv()

product_url = "https://www.amazon.com/SAMSUNG-FreeSync-Advanced-Frameless-LS27C392EANXGO/dp/B0BP927N3C?ref_=Oct_DLandingS_D_9d476093_6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    'referer': 'https://www.amazon.com/',
    }

response = requests.get(url=product_url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

product_title = soup.find(name="span", id="productTitle").get_text()
print(product_title)

product_price = soup.find(name="span", class_="a-price-whole").get_text().split(".")[0]
float_product_price = float(product_price)
print(float_product_price)

BUY_PRICE = 200

def send_email():
    email = os.getenv("USER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            # to_addrs=user_email,
            to_addrs='WRITE EMAIL ADDRESS',
            from_addr=email,
            msg=f"subject: Amazon price alert \n\n {product_title}is now ${product_price}\n {product_url}"
        )


if float_product_price < BUY_PRICE:
    # user_email = input("enter your email address: ")
    send_email()
    print("email sent")





