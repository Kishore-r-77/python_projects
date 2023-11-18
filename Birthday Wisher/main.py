# # my_email = "kishorework77@gmail.com"
# # to_address = "kishorelesnar77@gmail.com"
# # password="wzkpjrbpqbnkpiik"
# #
# # connection = smtplib.SMTP("smtp.gmail.com")
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(from_addr=my_email, to_addrs=to_address, msg="Hello")
# # connection.close()
#
#
# import smtplib
#
# my_email = "kishorework77@gmail.com"
# to_address = "kishorelesnar77@gmail.com"
# password = "wzkpjrbpqbnkpiik"
#
# # Use SMTP_SSL and specify the port
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#
#     # Login to the email account
#     connection.login(user=my_email, password=password)
#
#     # Send the email
#     connection.sendmail(from_addr=my_email, to_addrs=to_address, msg="Subject: Test\n\nHello Aswathy's Guy")
#
# # # Close the connection
# # connection.quit()

import datetime as dt

now=dt.datetime.now()
print(now.year)

date_of_birth = dt.datetime(year=1996,month=4,day=21,hour=2,minute=10)
print(date_of_birth)