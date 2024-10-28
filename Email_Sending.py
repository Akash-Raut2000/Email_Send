import smtplib as s
ob =s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("email and pass")
subjec="Test"
body="I love p ytho"
massage="Sun:{}\n\n{}".format(subject,b)
listadd=["abc@gmail.com,xyz@gmail.com"]
ob.sendmail("abc@gmail.com",listadd,manage)
print("send mail")
quit(email)