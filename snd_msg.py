# work with another users as usuall user

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
#from conf import api_id
#from conf import api_hash
#from conf import phone
#from conf import txt_spam

api_id = 14705741
api_hash = '28680abc0e9e0a5f8d0b85cc8a45c8bb'
phone = '+380988437624'


SLEEP_TIME = 30
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
    
with open("user_ids.txt") as file:
    for user_id in file:
        receiver = InputPeerUser(user_id,'0')
        try:
            print("Sending Message to:", user['name'])
            client.send_message(receiver, txt_spam)
            print("Waiting {} seconds".format(SLEEP_TIME))
            time.sleep(SLEEP_TIME)
        except PeerFloodError:
            print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            client.disconnect()
            sys.exit()
        except Exception as e:
            print("Error:", e)
            print("Trying to continue...")
            continue
client.disconnect()
print("Done. Message sent to all users.")


