import requests, json
from flask import Flask

app = Flask(__name__)


@app.route('/')
def default():
    file = requests.post('https://api.uptimerobot.com/v2/getMonitors?api_key=enterYourAPIKeyHere', verify=False)
    data = json.loads(file.text)
    monitors = data['monitors']
    for val in monitors:
        status = val['status']
        frendlyName = val['friendly_name']
        monitorUrl = val['url']
        if status == 9:
            result = requests.get(f'https://api.telegram.org/botEnterYourBotAPIHere/sendMessage?chat_id=enterYouChatIDhere&parse_mode=html&text=Обнаружена проблема: {frendlyName} is down%0AСодержание проблемы: Site is down. Status code: {status}%0A%0AURL: {monitorUrl}%0AКод статуса: {status}')
    return '!', 200