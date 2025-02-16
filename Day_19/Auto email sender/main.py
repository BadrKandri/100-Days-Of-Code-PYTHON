##################### auto mail sender ######################
#info: smtp is the agent that take ur email and send it to the server then to the receiver mail box

import pandas as pd
import datetime as dt
import random
import smtplib

now= dt.datetime.now()
df=pd.read_csv('birthdays.csv')
# print(df)

my_mail = 'bidrissikandri@gmail.com'
password = 'sxfrjxijasuldwgo'
receiver = df.loc[0,'email']
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()#secure my mail
connection.login(user=my_mail,password=password)

if now.year == df.loc[0,'year'] and now.month == df.loc[0,'month'] and now.day == df.loc[0,'day'] :
    randomn_file=(f"letter_templates/letter_{random.randint(1,3)}.txt")
    with open(randomn_file,mode='r') as file:
        data = file.read()
        message=data.replace("[NAME]", df.loc[0,'name'])
    connection.sendmail(from_addr=my_mail,to_addrs=receiver,msg=f"Subject: HAPPY BIRTHDAY\n\n{message}")
    connection.close()
    print(f"Email is sent to: {df.loc[0,'name']}")        
else:
    print("error")
