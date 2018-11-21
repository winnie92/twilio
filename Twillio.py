
# coding: utf-8

# In[56]:


from twilio.rest import Client

from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup_by_location('los angeles')
condition = location.condition

messageBody = location.location.city+'\n'+condition.date+'\nCondition: '+condition.text+'\ntemp: '+condition.temp
TWILIO_ACCOUNT_SID = 'AC7d65bce1467aad34581adbc6a251104f'
TWILIO_AUTH_TOKEN = '4252ca9743420d35194ace29253ace11'
TO_NUMBER = '+15083733224'
FROM_NUMBER = '+13517771070'
try:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
                         body=messageBody,
                         from_=FROM_NUMBER,
                         to=TO_NUMBER
                     )
    print('Send message success!')
    print(message.sid)
except:
    print('Message failed to send!')


