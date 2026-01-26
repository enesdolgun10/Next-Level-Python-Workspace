import smtplib
from email.mime.text import MIMEText


port = 587 
smpt_server = "smtp-relay.brevo.com"
login = "a0e1cd001@smtp-brevo.com"
password = "xsmtpsib-04af1271f743ff3bdf95747600b4afadb0fd0bc39c9ddbd07fedf790902acedf-oY8WNa91RWyejBHo" 
apikey = "xsmtpsib-04af1271f743ff3bdf95747600b4afadb0fd0bc39c9ddbd07fedf790902acedf-oY8WNa91RWyejBHo"

sender_email = "enesdlgnforgames@gmail.com"
receiver_email = "neber82418@ixunbo.com"

email_list = ["enesdolgun33@gmail.com,neber82418@ixunbo.com"]

text = """
    Merhaba, bu eposta Python ile gönderildi.    
"""

message = MIMEText(text,"plain")
message["Subject"] = "Merhaba bu konu"
message["From"] = sender_email
message["To"] = receiver_email
# message["To"] = ",".join(email_list)

with smtplib.SMTP(smpt_server, port) as server:
    server.starttls()
    server.login(login,password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("Eposta gönderildi.")
