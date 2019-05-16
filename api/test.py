import requests
from random import randint

def WindSpeed():
    #Creates makeshift WindSpeed data to send to server
    return randint(0,20)


def Temp():
    #Creates makeshift Temp data to send to server
    return randint(0,20)


post_data = {'username':'tom', 'dob':'1988-05-21'}
#POSTs post_data to server
r = requests.post('http://127.0.0.1:5000', data = post_data)
print (r.text)
