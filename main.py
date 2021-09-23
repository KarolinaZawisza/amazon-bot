import requests as requests
from bs4 import BeautifulSoup
from email_manager import EmailManager

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.82 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pl;q=0.8,ja-JP;q=0.7,ja;q=0.6,pl-PL;q=0.5"
}

url = 'https://www.amazon.com/ASUS-VG328H1B-Supports-Adaptive-sync-FreeSync/dp/B088MKF848/ref=sxin_13_ac_d_mf_rf?ac_' \
      'md=2-1-MzAgdG8gMzkuOSBJbmNoZXM%3D-ac_d_mf_rf_rf&crid=2XFZ04XENRGYD&cv_ct_cx=monitor&dchild=1&' \
      'keywords=monitor&pd_rd_i=B087V5RLFB&pd_rd_r=6074524b-6407-4da6-8335-58964f94aa30&pd_rd_w=iG2DM&pd_rd_' \
      'wg=WUvkR&pf_rd_p=95fb715a-d44a-4a3c-ac61-fb2df95cb7e9&pf_rd_r=HC60K2FBRCCH0V1M2020&qid=1632427442&' \
      'sprefix=moni%2Caps%2C275&sr=1-2-1db1fce3-1628-43df-a6c6-84620ba4aaaa&th=1'

response = requests.get(url=url, headers=header).text

soup = BeautifulSoup(response, 'lxml')
price = int(soup
            .find(name='span', class_='a-size-medium a-color-price priceBlockBuyingPriceString')
            .getText()
            .strip('$')
            .split('.')[0])

original_price = 349

if price < original_price:
    EmailManager.send_email(price, original_price, url)
else:
    print('Price is the same!')


