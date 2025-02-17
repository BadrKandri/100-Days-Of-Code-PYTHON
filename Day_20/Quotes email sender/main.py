import smtplib
import datetime as dt
import random

my_mail = 'bidrissikandri@gmail.com'
password = 'sxfrjxijasuldwgo'
receiver = 'traxeratorgamer@gmail.com'
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()#secure my mail
connection.login(user=my_mail,password=password)

now=dt.datetime.now()
quotes_list = []

with open ("quotes.txt",mode= "r") as file:
    for quote in file:
        quote = quote.strip()  # Remove newlines
        quotes_list.append(quote)
    
if now.year == 2025 and now.month == 2 and now.day == 12 and now.hour == 21 and now.minute == 6:
    
    random_quote=random.choice(quotes_list)
    print(random_quote)
    connection.sendmail(from_addr=my_mail,to_addrs=receiver,msg=f"Subject: Todays quote\n\n{random_quote}")
    connection.close()
    print(f"Email is sent to: {receiver}")
else:
    print('Email is not sent')

