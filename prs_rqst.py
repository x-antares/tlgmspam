from telethon.sync import TelegramClient
from telethon import functions, types
#from conf import api_id
#from conf import api_hash
#from conf import phone

api_id = 14705741
api_hash = '28680abc0e9e0a5f8d0b85cc8a45c8bb'
phone = '+380988437624'

with TelegramClient(phone, api_id, api_hash) as client:
    result = client(functions.contacts.GetContactsRequest(
        hash=0
    ))
    print(result.stringify())
    file = open('read.txt', 'w')
    file.write(result.stringify())
    file.close()
    
    
print("Parsing data...")            
