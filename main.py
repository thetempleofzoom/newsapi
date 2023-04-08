import requests
from sendemail import send_email


url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2023-03-08&sortBy=publishedAt&"\
    "apiKey=297dd2fa073043748f2f8616c02d8204"

#apikey = "297dd2fa073043748f2f8616c02d8204"

requ = requests.get(url)
#json gives dict, text gives string
contents = requ.json()


message_body = ""
for article in contents["articles"]:
    message_body = f'{message_body} \n\n {article["title"]} ' \
                   f'\n {article["description"]}'

message_body = message_body.encode('utf-8')
print(message_body)
message = f"""\
subject:news from apifeed 
{message_body}"""

send_email(message_body)