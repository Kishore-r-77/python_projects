# my_email = "kishorework77@gmail.com"
# to_address = "kishorelesnar77@gmail.com"
# password="wzkpjrbpqbnkpiik"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs=to_address, msg="Hello")
# connection.close()


import smtplib

my_email = "kishorework77@gmail.com"
to_address = "kishorelesnar77@gmail.com"
password = "wzkpjrbpqbnkpiik"

# Use SMTP_SSL and specify the port
connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# Login to the email account
connection.login(user=my_email, password=password)

# Send the email
connection.sendmail(from_addr=my_email, to_addrs=to_address, msg="Subject: Test\n\nHello")

# Close the connection
connection.quit()



