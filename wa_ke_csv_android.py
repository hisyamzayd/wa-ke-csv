import os
import pandas as pd
import sys
import re

file_list = os.listdir(os.getcwd()+'/raw data android')

whatsapp_list = list()
for file in file_list:
    if file.endswith('.txt'):
        whatsapp_list.append(file)
if not whatsapp_list:
    print('there is no whatsapp chat file')
#     sys.exit()
    
for file in whatsapp_list:
    with open('raw data android/'+file, 'r', encoding='utf-8') as f:
        timestamp_list = list()
        sender_list = list()
        messages_list = list()
        
        chats = f.read()
        chats = " ".join(chats.split()) #remove excess space and new line
        re_new_line = re.compile("(\s)\d{1,2}/\d{1,2}/\d{1,4}\,*\s\d{1,2}\:*\.*\d{1,2}\s\w*", re.S) 
        chats = re_new_line.sub(lambda m: m.group().replace(' ', "\n", 1), chats) #space between chats replaced with new line
        chats = chats.split('\n')
        for chat in chats:
            hasil = re.match("(\d{1,2}/\d{1,2}/\d{1,4}\,*\s\d{1,2}\:*\.*\d{1,2}\s\w*)\s*\-\s([a-zA-Z\s]+)\:\s([\S\s]*)", chat)
            if hasil:  
                timestamp_list.append(hasil.group(1))
                sender_list.append(hasil.group(2))
                messages_list.append(hasil.group(3))
        
        df = pd.DataFrame(
            list(zip(timestamp_list, sender_list, messages_list)),
            columns=['timestamp', 'sender', 'messages']
        )
        nama_file = 'hasil csv/' + file.replace('.txt', '.csv')
        df.to_csv(nama_file, index=False)