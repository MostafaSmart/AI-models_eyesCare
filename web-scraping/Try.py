import requests
from bs4 import BeautifulSoup
import json
import base64

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}


folder = '25/img25/'
url = "https://downpic.cc/shutter/"
gett= 'get'
down = 'download'

session = requests.Session()
response = session.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    input_element = soup.find('input', {'type': 'hidden', 'name': 'csrfmiddlewaretoken'})
    value = input_element.get('value')
    formData = {
    "csrfmiddlewaretoken": value,
    "url": "https://www.shutterstock.com/fr/image-photo/close-anterior-uveitis-posterior-synechia-during-313334819"
    }
    response2 = session.post(url+gett, data=formData)
    if response2.status_code == 200:
        data = response2.json()
        if data["code"] == 0:
            print('code 0')
        elif data["code"] == 1:
            name = 'mm'
            dd = json.dumps(data)
            parsed_data = json.loads(dd)
            link = 'https://downpic.cc/'
            link = link+parsed_data['link']
            
            rr = requests.get(link)
            if rr.status_code == 200:
                filename = folder + f'{name}.jpg'
                with open(filename, 'wb') as file:
                    file.write(rr.content)
                    print('done')
    
    
    
    
    