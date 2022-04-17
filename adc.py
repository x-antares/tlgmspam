from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import functions, types
from conf import api_id
from conf import api_hash
from conf import phone


client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
   client.send_code_request(phone)
   client.sign_in(phone, input('Enter the code: '))
            
            
with open("phones.txt") as file:
    for idx, phone in enumerate(file):
        fn = 'fname' + str(idx)
        ln = 'fname' + str(idx)
        contact = InputPhoneContact(client_id = 0, phone = phone, first_name=fn, last_name=ln)
        result =  client(ImportContactsRequest([contact]))
        
        
print("All contacts added successfull!!")        
