import requests
from bs4 import BeautifulSoup
from send_email import sendMail
url1 = "https://www.trendyol.com/trendyolmilla/siyah-yirtmac-detayli-orme-tayt-twoaw22ta0004-p-119315455?boutiqueId=595874&merchantId=968"


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

page = requests.get(url1, headers=headers)

htmlPage = BeautifulSoup(page.content, 'html.parser')

productTitle = htmlPage.find("h1", class_="pr-new-br")

price = htmlPage.find("span", class_ = "prc-slg").getText()

image = htmlPage.find("img" , class_ = "base-product-image")

convertedPrice = float(price.replace(",", ".").replace(" TL", ""))

if(convertedPrice <= 150):
    print("Price drop on the product")
    htmlEmailContent = """\
    <html>
    <head></head>
    <body>
    <h3>{0}</h3>
    <br/>
    {1}
    <br/>
    <p>Ürün Linki: {2}<p/>
    </body>
    </html>
    """.format(productTitle, image, url1)
    sendMail("your-email","a price drop on the product",htmlEmailContent)

print(productTitle)
print(price)
print(convertedPrice)
print(image)

print(test)