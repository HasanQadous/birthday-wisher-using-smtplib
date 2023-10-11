##################### Extra Hard Starting Project ######################
import random
import pandas
import smtplib
import datetime as dt

MY_MAIL = "hassan_tariq74@outlook.com"
MY_PASS = "Hasn1998"

data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()

today_tuple = (now.month, now.day)

birth_dic = {(data_row["month"], data_row["day"]): data_row
             for (index, data_row) in data.iterrows()}

if today_tuple in birth_dic:
    birthday_person = birth_dic[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        content = file.read()
        content.replace("[Name]", birthday_person["name"])

    with smtplib.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_PASS)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=birthday_person["email"], msg=content)






