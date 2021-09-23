import smtplib
from envr import MAIN_EMAIL, MAIN_EMAIL_PASSWORD, MAY_EMAIL


class EmailManager:

    @staticmethod
    def send_email(price, original_price, url):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MAIN_EMAIL, password=MAIN_EMAIL_PASSWORD)
            connection.sendmail(from_addr=MAIN_EMAIL,
                                to_addrs=MAY_EMAIL,
                                msg='SUBJECT: Price drop!\n\n'
                                    'The item you were watching on Amazon is cheaper now!\n'
                                    f'Current price: ${price}.00\n'
                                    f'Previous price: ${original_price}.00 (${({original_price}-price)}.00 cheaper!)\n'
                                    f'Check it out here: {url}'.encode('utf-8')
                                )
            print(f'Send to {MAY_EMAIL}')