import configparser

config = configparser.ConfigParser()

config.read('data.ini')

api_id = config.get('user_data', 'api_id')
api_hash = config.get('user_data', 'api_hash')
phone = config.get('user_data', 'phone')
txt_spam = config.get('spam_text', 'txt_spam')

