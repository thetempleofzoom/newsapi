import requests
from sendemail import send_email
from datetime import date, timedelta

keyword='bitcoin'
fromdate = date.today()
fromdate = str(fromdate- timedelta(days=1))



url = f'https://newsapi.org/v2/everything?q={keyword}' \
    f'&from={fromdate}' \
      '&sortBy=publishedAt'\
    '&apiKey=297dd2fa073043748f2f8616c02d8204' \
      '&language=en'

print(url)

requ = requests.get(url)
#json gives dict, text gives string
contents = requ.json()
print(contents)

message_body = ""
for article in contents["articles"][:50]:
    if article['title'] is not None:
        message_body = f'{message_body} \n\n {article["title"]} ' \
                   f'\n {article["description"]}' \
                   f'\n {article["url"]}' 


print(message_body)
message = f"""\
subject:news from apifeed 
{message_body}"""

#code entire message in utf for it to work, not just message body
message = message.encode('utf-8')

send_email(message)