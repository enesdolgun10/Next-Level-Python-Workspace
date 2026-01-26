import vonage

# if you want to manage your secret, please do so by visiting your API Settings page in your dashboard
client = vonage.Client(key="3cd69207", secret="NslvlcunRSRmNN4v")
sms = vonage.Sms(client)


responseData = sms.send_message({
    "from":"Deneme",
    "to":"905078845423",
    "text":"bu sms python ile gönderildi"
})

if responseData["messages"][0]["status"] == 0:
    print("Mesajınız gönderildi")
else:
    print(f"hata olustu :{responseData['messages'][0]['error-text']}")