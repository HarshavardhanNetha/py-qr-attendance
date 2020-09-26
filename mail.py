import smtplib

user='sender_mail'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(user,'sender_pwd')

message = "Test Mail"
server.sendmail(user,'recepient mail',message)
server.quit()
