from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import functions, types
import time

api_id = 14705741
api_hash = '28680abc0e9e0a5f8d0b85cc8a45c8bb'
phone = '+380988437624'
SLEEP_TIME = 30

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
   client.send_code_request(phone)
   client.sign_in(phone, input('Enter the code: '))
            
            
with open("phones.txt") as file:
    for idx, add_phone in enumerate(file):
        fn = str(idx+1)
        ln = str(idx+1)
        contact = InputPhoneContact(client_id = 0, phone = add_phone, first_name=fn, last_name=ln)
        result =  client(ImportContactsRequest([contact]))
        print("Waiting {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)
        
        
print("All contacts added successfull!!")        
