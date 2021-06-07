from twilio.rest import Client 

 
account_sid = 'account_sid' 
auth_token = 'auth_token'
client = Client(account_sid, auth_token) 
fgo=client.password

url=open('D:/Dell/Desktop/Codes/debug.log')
print(url)
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body="",
                              to='whatsapp:YOURNUMPER' 
                          )

