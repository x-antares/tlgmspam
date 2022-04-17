from telethon.sync import TelegramClient
from telethon import functions, types
from conf import api_id
from conf import api_hash
from conf import phone

with TelegramClient(phone, api_id, api_hash) as client:
    result = client(functions.contacts.GetContactsRequest(
        hash=0
    ))
    print(result.stringify())
    file = open('read.txt', 'w')
    file.write(result.stringify())
    file.close()
    
    
print("Parsing data...")            
