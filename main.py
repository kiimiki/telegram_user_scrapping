from telethon.sync import TelegramClient
from telethon import errors
from tqdm import tqdm
import pandas as pd


api_id = " "
api_hash = " "
phone = " "
client = TelegramClient(phone, int(api_id), api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

dialogs = client.get_dialogs()

df = pd.DataFrame()
channels = []
header = ['User Channel', 'First Name', 'Last Name', 'user id']
channel_n = []
fname = []
lname = []
userid = []
for d in dialogs:
    if d.is_channel:
        channels.append(d.title)

print(channels)

for channel in tqdm(channels):
    c = channel
    try:
        for partic in client.iter_participants(c):
            channel_n.append(c)
            try:
                if partic.first_name:
                    name = partic.first_name
            except None:
                name = "Null"
            try:
                if partic.last_name:
                    last = partic.last_name
            except None:
                last = "Null"
            try:
                if partic.id:
                    uid = partic.id
            except None:
                uid = "Null"
            fname.append(name)
            lname.append(last)
            userid.append(uid)
            # print(channel, name, last, uid)
    except errors.ChatAdminRequiredError:
        continue
# print(channel_n, fname, lname, userid)
df['User Chat'] = channel_n
df['First Name'] = fname
df['Last Name'] = lname
df['User ID'] = userid
df.to_csv('users.csv', index=False)
print('HappyEnd')
