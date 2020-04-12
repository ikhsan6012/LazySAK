import requests
import sys
import json
from bs4 import BeautifulSoup as bs
from random import randint

BASE_URL = 'https://logbook.pajak.go.id/'

with requests.Session() as s:
  def getToken(url):
    res = s.get(url)
    soup = bs(res.content, 'html.parser')
    token = soup.select_one('[name=token]')['value']
    return token

  def getData(token):
    data = open('config.json')
    data = json.load(data)
    data2 = {}

    if data['pernyataan']['value'] != 1:
      print('"pernyataan.value" Harus 1!')
      sys.exit()
    
    is_error = False
    for key in data:
      if data[key]['required'] == True and not data[key]['value']:
        print('"' + key + '.value" Tidak Boleh 0 (Nol) atau Kosong!')
        is_error = True
      if not(data[key]['type'] == 'checkbox' and data[key]['value'] == 2):
        if (key == 'latitude' or key == 'longitude') and data[key]['value'] == 'default':
          ipinfo = s.get('https://ipinfo.io/json')
          ipinfo = ipinfo.json()
          latitude, longitude = ipinfo['loc'].split(',')
          data2[key] = eval(key)
        else: data2[key] = data[key]['value']
    if is_error == True: sys.exit()

    data2['accuracy'] = randint(10, 1000)
    data2['token'] = token
    return data2
  
  def login(nip, password):
    token = getToken(BASE_URL)
    url = BASE_URL + 'login/validate/'
    data = { 'token': token, 'nip': nip, 'password': password }
    res = s.post(url, data=data)
    if 'refresh' in res.headers.keys():
      print('Login Berhasil!')
      return
    print('Login Gagal. NIP atau Password Salah!')
    sys.exit()

  def isi_logbook():
    token = getToken(BASE_URL + 'SelfAssessmentKesehatan/form')
    data = getData(token)
    res = s.post(BASE_URL + 'SelfAssessmentKesehatan/add', data=data)
    if 'refresh' in res.headers.keys():
      print('Gagal Menyimpan SAK!')
    else:
      print('Berhasil Menyimpan SAK!')
      print('zzzzzzzzzzzzzzzzzzzzz Selamat Tidur Lagi zzzzzzzzzzzzzzzzzzzzz')
      sys.exit()

  if __name__ == '__main__':
    def is_number(s):
      try:
        float(s)
        return True
      except ValueError:
        return False

    def get_nip():
      nip = ''
      if len(sys.argv) > 1: nip = sys.argv[1]
      else: nip = input('Masukkan NIP: ')
      if not nip:
        print('NIP Tidak Boleh Kosong!')
        nip = get_nip()
      if is_number(nip) == False:
        print('NIP Tidak Boleh Berisi Karakter Selain Digit!')
        nip = get_nip()
      if len(nip) != 9:
        print('NIP Harus 9 Digit!')
        nip = get_nip()
      return nip

    def get_password():
      password = ''
      if len(sys.argv) > 2: password = sys.argv[2]
      else: password = input('Masukkan Password: ')
      if not password:
        print('Password Tidak Boleh Kosong!')
        password = get_password()
      return password

    nip = get_nip()
    password = get_password()

    login(nip, password)
    isi_logbook()
