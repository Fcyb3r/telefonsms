import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '+905555555555', #telefon no buraya
  'message': 'привет я fcчвєr bu bir deneme mesajıdır',
  'key': 'textbelt',
})
print(resp.json())