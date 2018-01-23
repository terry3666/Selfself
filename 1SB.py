# -*- coding: utf-8 -*-

import KRIS
from KRIS.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

kr = KRIS.LINE()
#kr.login(qr=True)
kr.login(token='')#Akun utama
kr.loginResult()

kr1 = KRIS.LINE()
#kr1.login(qr=True)
kr1.login(token='')#Asist 1
kr1.loginResult()

kr2 = KRIS.LINE()
#kr2.login(qr=True)
kr2.login(token='')#Asist 2
kr2.loginResult()

kr3 = KRIS.LINE()
#kr3.login(qr=True)
kr3.login(token='')#Asist 3
kr3.loginResult()

kr4 = KRIS.LINE()
#kr4.login(qr=True)
kr4.login(token='')#Asist 4
kr4.loginResult()

kr5 = KRIS.LINE()
#kr5.login(qr=True)
kr5.login(token='')#Asist 5
kr5.loginResult()

print "╔═════════════════════════╗\n║╔═══════════════════════╗║\n║╠❂➣KRIS BERHASIL LOGIN ║║\n║╚═══════════════════════╝║\n╚═════════════════════════╝"
reload(sys)
sys.setdefaultencoding('utf-8')

#album = None
#image_path = 'tmp/tmp.jpg'

helpMessage ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣Key1
║╠❂➣Key2
║╠❂➣Key3
║╠❂➣Say (txt)
║╠❂➣Kr say (text)
║╠❂➣Apakah (text)
║╠❂➣Kapan (txt)
║╠❂➣welcome
║╠❂➣.. (text)
║╠❂➣Time
║╠❂➣rate @
║╠❂➣Gcreator
║╠❂➣Creator
║╠❂➣Spam on (jml) (Text)
║╠❂➣image
║╠❂➣ig
║╠❂➣youtube
║╠❂➣lirik
║╠❂➣music
║╠❂➣zodiAK
║╠❂➣Mimic on/off
║╠❂➣Micadd @
║╠❂➣Micdel @
║╠❂➣Miclist
║╠❂➣Getcover @
║╠❂➣Tag on/off
║╠❂➣Getpp @
║╠❂➣Getinfo @
║╠❂➣Getinfo2
║╠❂➣Sambut on/off
║╠❂➣pergi on/off
║╠❂➣setview
║╠❂➣viewseen
║╠❂➣CCtv
║╠❂➣Intip
║╠❂➣Crot (tagall)
║╠❂➣Absen
║╠❂➣Gift
║╠❂➣Ranita pergi (ngeluarkan bot)
║╚════════════
║   UNTUK PUBLIK
║ SILAHKAN GUNAKAN
╚═════════════
"""

key1Message ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣qr on/oғғ
║╠❂➣gυeѕт on/oғғ
║╠❂➣мeмвer on/oғғ
║╠❂➣groυp on/oғғ
║╠❂➣ĸιcĸ on/oғғ
║╠❂➣cancel on/oғғ
║╚════════════
╚═════════════

╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣wιĸι [тeхт]
║╠❂➣ιg [тeхт]
║╠❂➣ιмage [тeхт]
║╠❂➣vιdeo [тeхт]
║╠❂➣zodιaĸ [тeхт]
║╠❂➣yoυтυвe [тeхт]
║╠❂➣lιrιĸ [тeхт]
║╠❂➣ιdlιne [тeхт]
║╠❂➣мυѕιc [тeхт]
║╠❂➣тιмe [тιмe]
║╠❂➣ѕay [тeхт]
║╚════════════
╚═════════════
"""

key2Message ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣тr-ιd = ιndoneѕιa
║╠❂➣тr-мy = мyanмar
║╠❂➣тr-en = englιѕн
║╠❂➣тr-тн = тнaιland
║╠❂➣тr-ja = japaneѕe
║╠❂➣тr-мѕ = мalayѕιa
║╠❂➣тr-ιт = ιтalιan
║╠❂➣тr-тr = тυrĸιѕн
║╠❂➣тr-aғ = aғrιĸaanѕ
║╠❂➣тr-ѕq = alвanιan
║╠❂➣тr-aм = aмнarιc
║╠❂➣тr-ar = araвιc
║╠❂➣тr-нy = arмenιan
║╚════════════
╚═════════════

╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣nĸ [naмe]
║╠❂➣vĸ [naмe]
║╠❂➣nυĸe
║╠❂➣lυrĸιng > Cctv
║╠❂➣тeѕ
║╠❂➣reѕpon
║╠❂➣ѕpeed
║╠❂➣glιѕт
║╠❂➣тagall/Crot
║╠❂➣reѕтarт
║╠❂➣cn [тeхт]
║╠❂➣cѕ [тeхт]
║╠❂➣мe
║╠❂➣craѕн
║╚════════════
╚═════════════
"""

key3Message ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣ѕeт
║╠❂➣тag on/oғғ
║╠❂➣тag2 on/oғғ
║╠❂➣aυтolιĸe on/oғғ
║╠❂➣add on/oғғ
║╠❂➣joιn on/oғғ
║╠❂➣ѕнare on/oғғ
║╠❂➣coммenт on/oғғ
║╠❂➣ĸ on/oғғ
║╠❂➣njoιn on/oғғ
║╠❂➣pergi on/oғғ
║╚════════════
╚═════════════

╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣gιғт
║╠❂➣gιғт 1
║╠❂➣gιғт 2
║╠❂➣gιғт 3
║╚════════════
╚═════════════
"""

key4Message ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣geтnaмe @
║╠❂➣geтвιo @
║╠❂➣geтιnғo @
║╠❂➣geтpp @
║╠❂➣geтcover @
║╠❂➣geтмιd @
║╠❂➣geтgroυp
║╠❂➣ѕeтιмage [lιnĸ]
║╠❂➣papιмage
║╠❂➣ѕeтvιdeo [lιnĸ]
║╠❂➣papvιdeo
║╠❂➣мycopy @
║╠❂➣мyвacĸυp
║╚════════════
╚═════════════
"""
KAC=[kr,kr1,kr2,kr3,kr4,kr5]
AST=[kr1,kr2,kr3,kr4,kr5]
mid = kr.getProfile().mid
Amid = kr1.getProfile().mid
Bmid = kr2.getProfile().mid
Cmid = kr3.getProfile().mid
Dmid = kr4.getProfile().mid
Emid = kr5.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid]
induk=[mid]
asist=[Amid,Bmid,Cmid,Dmid,Emid]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1",Amid,Bmid,Cmid,Dmid,Emid]
owner=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
wait = {
    "contact":False,
    "alwayRead":False,
    "autoJoin":True,
    "autoCancel":{"on":True,"members":1},
    "leaveRoom":False,
    "timeline":False,
    "autoAdd":True,
    "detectMention":True,
    "message":"""👉😊☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\n\nby Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««""",
    "lang":"JP",
    "comment":"""👉😊☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\n\nby Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««""",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "QrProtect":False,
    "MProtection":False,
    "Protectguest":False,
    "Protectcancel":False,
    "autoKick":False,
    "auto":True,
    "tag":False,
    "tag2":False,
    "likeOn":False,
    "winvite":False,
    "Wc":True,
    "Wc2":True,
    "Lv":True,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "protectionOn":False,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

settings = {
    "simiSimi":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = kr.getProfile()
mybackup = kr.getProfile()
contact = kr1.getProfile()
mybackup = kr1.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
backup = kr.getProfile()
contact = kr1.getProfile()
backup = kr1.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
profile = kr.getProfile()
contact = kr1.getProfile()
profile = kr1.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")
agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")
#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

#def autolike():
#    for zx in range(0,100):
#      hasil = kr.activity(limit=100)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
#          kr.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#          kr.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
#          print "Like"
#        except:
#          pass
#      else:
#          print "Already Liked"
#time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = kr.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')


def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e

def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True



def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "► @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         kr.sendMessage(msg)
    except Exception as error:
        print error

def removeAllMessages(self, lastMessageId):
     return self._client.removeAllMessages(0, lastMessageId)
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={"MENTION":'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       kr.sendMessage(msg)
    except Exception as error:
       print error

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait['autoAdd'] == True:
                kr.findAndAddContactsByMid(op.param1)
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    kr.sendText(op.param1,str(wait['message']))
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr.sendText(msg.to,text)
                        kr1.sendText(msg.to,text)

#==========================[Kris]===========================
        if op.type == 55:
            try:
                group_id = op.param1
                user_id=op.param2
                subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
            except Exception as e:
                print e
#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+kr.getProfile().displayName in msg.text:
                if wait["tag"] == True:
                    tanya = msg.text.replace("@"+kr.getProfile().displayName,"")
                    jawab = ("Kenapa Tag Si "+kr.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung ownernya biar anu hihi..!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈","Nah ngetag lagi si "+kr.getProfile().displayName+" mending ajak mojok aja ownernya dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈")
                    jawaban = random.choice(jawab)
                    random.choice(KAC).sendText(msg.to,jawaban)
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = kr.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  random.choice(KAC).sendImageWithURL(msg.to,ret_)
                                  break  
        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+kr.getProfile().displayName in msg.text:
                if wait["tag2"] == True:
                    tanya = msg.text.replace("@"+kr.getProfile().displayName,"")
                    jawab = "Ada apa ngetag "+kr.getProfile().displayName+"Mau usil ya..!!!\nKick ah Lu kicker ya yg suka usil..!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈","Nah ngetag lagi "+kr.getProfile().displayName+" Usil mulu di Kick ah...!!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈"
                    jawaban = random.choice(jawab)
                    random.choice(KAC).sendText(msg.to,jawaban)
                    random.choice(AST).kickoutFromGroup(msg.to,[msg.from_])
                    random.choice(KAC).inviteIntoGroup(msg.to,admin)
#==========================[Kris]===========================
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in Bots:
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#==========================[Kris]===========================
        if op.type == 13:
           if wait["Protectguest"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in Bots:
                    random.choice(AST).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#==========================[Kris]===========================
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in Bots:
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
#==========================[Kris]===========================
        if op.type == 11:
            if wait["QrProtect"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in Bots:
                    G = random.choice(AST).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(AST).updateGroup(G)
#==========================[Kris]===========================
        if op.type == 17:
            if wait["Wc"] == True:
                if op.param2 in Bots:
                    return
                ginfo = kr.getGroup(op.param1)
                gm = Message()
                gm.to = op.param1
                gm.text = ("╔═════════════" + "\n║" + kr.getContact(op.param2).displayName + "\n╠═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╠═════════════\n║No Baper,No nakal,No Ngeyel ya..!! \n╚═════════════")
                random.choice(KAC).sendMessage(gm)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc2"] == True:
                if op.param2 in Bots:
                    return
                G = kr.getGroup(op.param1)
                h = kr.getContact(op.param2)
                random.choice(KAC).sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                random.choice(KAC).sendText(op.param1, "╔═════════════" + "\n║" + kr.getContact(op.param2).displayName  +  "\n╠═════════════\n║Nah Baper Dia :v \n╠═════════════\n║Belum di Anu Kayanya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#==========================[Kris]===========================
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr.sendText(msg.to,text)
                        kr1.sendText(msg.to,text)
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = kr.getGroup(op.param1)
                    except:
                        try:
                            G = kr1.getGroup(op.param1)
                        except:
                            try:
                                G = kr2.getGroup(op.param1)
                            except:
                                try:
                                    G = kr3.getGroup(op.param1)
                                except:
                                    try:
                                        G = kr4.getGroup(op.param1)
                                    except:
                                        try:
                                            G = kr5.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        kr.updateGroup(G)
                    except:
                        try:
                            kr1.updateGroup(G)
                        except:
                            try:
                                kr2.updateGroup(G)
                            except:
                                try:
                                    kr3.updateGroup(G)
                                except:
                                    try:
                                        kr4.updateGroup(G)
                                    except:
                                        try:
                                            kr5.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            kr1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kr3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kr4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kr5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        kr1.sendText(op.param1,"please do not change group name-_-")
#==========================[Kris]===========================
        if op.type == 13:
            print op.param3
            if op.param3 in mid:
                if op.param2 in owner or Bots:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in owner or Bots:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in owner or Bots:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in owner or Bots:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in owner or Bots:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in owner or Bots:
                    kr5.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in mid:
                if op.param2 in Amid:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Bmid:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Cmid:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Dmid:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Emid:
                    kr.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Amid:
                if op.param2 in mid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Bmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Cmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Dmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Emid:
                    kr1.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Bmid:
                if op.param2 in mid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Amid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Cmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Dmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Emid:
                    kr2.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Cmid:
                if op.param2 in mid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Amid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Bmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Dmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Emid:
                    kr3.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Dmid:
                if op.param2 in mid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Amid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Bmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Cmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Emid:
                    kr4.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Emid:
                if op.param2 in mid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Amid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Bmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Cmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Dmid:
                    kr5.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots or admin:
                        kr.acceptGroupInvitation(op.param1)
                    else:
                        kr.rejectGroupInvitation(op.param1)
                    
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots or admin:
                        kr1.acceptGroupInvitation(op.param1)
                    else:
                        kr1.acceptGroupInvitation(op.param1)
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr1.leaveGroup(op.param1)
                    
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots or admin:
                        kr2.acceptGroupInvitation(op.param1)
                    else:
                        kr2.acceptGroupInvitation(op.param1)
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                        kr2.leaveGroup(op.param1)
                    
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots or admin:
                        kr3.acceptGroupInvitation(op.param1)
                    else:
                        kr3.acceptGroupInvitation(op.param1)
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        kr3.leaveGroup(op.param1)
                    
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots or admin:
                        kr4.acceptGroupInvitation(op.param1)
                    else:
                        kr4.acceptGroupInvitation(op.param1)
                        kr4.kickoutFromGroup(op.param1,[op.param2])
                        kr4.leaveGroup(op.param1)
                    
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots or admin:
                        kr5.acceptGroupInvitation(op.param1)
                    else:
                        kr5.acceptGroupInvitation(op.param1)
                        kr5.kickoutFromGroup(op.param1,[op.param2])
                        kr5.leaveGroup(op.param1)
#==========================[Kris]===========================
        if op.type == 19:
            if op.param3 in admin:
                if op.param2 not in admin:
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(AST).inviteIntoGroup(op.param1,admin)
                    random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
                    
            if op.param3 not in Bots:
                if op.param2 not in Bots:
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
                    
            if op.param3 in admin:
                if op.param2 in admin:
                    random.choice(AST).inviteIntoGroup(op.param1,admin)
                    random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
                    
        if op.type == 19:
            if op.param3 in Bots:
                if op.param2 not in Bots:
                    midd = (mid)
                    midd1 = (Amid)
                    midd2 = (Bmid)
                    midd3 = (Cmid)
                    midd4 = (Dmid)
                    midd5 = (Emid)
                    random.choice(KAC).findAndAddContactsByMid(midd)
                    random.choice(KAC).findAndAddContactsByMid(midd1)
                    random.choice(KAC).findAndAddContactsByMid(midd2)
                    random.choice(KAC).findAndAddContactsByMid(midd3)
                    random.choice(KAC).findAndAddContactsByMid(midd4)
                    random.choice(KAC).findAndAddContactsByMid(midd5)
                    random.choice(KAC).inviteIntoGroup(op.param1,[midd])
                    random.choice(KAC).inviteIntoGroup(op.param1,[midd1])
                    random.choice(KAC).inviteIntoGroup(op.param1,[midd2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[midd3])
                    random.choice(KAC).inviteIntoGroup(op.param1,[midd4])
                    random.choice(KAC).inviteIntoGroup(op.param1,[midd5])
                    kr.acceptGroupInvitation(op.param1)
                    kr1.acceptGroupInvitation(op.param1)
                    kr2.acceptGroupInvitation(op.param1)
                    kr3.acceptGroupInvitation(op.param1)
                    kr4.acceptGroupInvitation(op.param1)
                    kr5.acceptGroupInvitation(op.param1)
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                    
            if op.param3 in induk:
                if op.param2 not in Bots:
                    midd = (mid)
                    random.choice(AST).findAndAddContactsByMid(midd)
                    random.choice(AST).inviteIntoGroup(op.param1,[midd])
                    kr.acceptGroupInvitation(op.param1)
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#==========================[Kris]===========================
        if op.type == 19:
            if wait["autoKick"] == True:
                if op.param2 in admin or Bots:
                    pass
                else:
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                if op.param2 in wait["blacklist"]:
                    pass
                else:
                    if op.param2 in admin or Bots:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if op.param2 in wait["blacklist"]:
                    pass
                else:
                    if op.param2 in admin or Bots:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#==========================[Kris]===========================
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                    #if msg.from_ in owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = random.choice(AST).getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                random.choice(AST).sendText(msg.to,"-> " + _name + " was here")
                                break
                            elif invite in wait["blacklist"]:
                                random.choice(AST).sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                random.choice(AST).sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    random.choice(AST).findAndAddContactsByMid(target)
                                    random.choice(AST).inviteIntoGroup(msg.to,[target])
                                    random.choice(AST).sendText(msg.to,"Done Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        random.choice(AST).findAndAddContactsByMid(invite)
                                        random.choice(AST).inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        random.choice(AST).sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break
#==========================[Kris]===========================
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    random.choice(AST).sendChatChecked(msg.from_,msg.id)
                else:
                    random.choice(AST).sendChatChecked(msg.to,msg.id)
#==========================[Kris]===========================
        if op.type == 22:
            if wait["leaveRoom"] == True:
                kr.leaveRoom(op.param1)
                kr1.leaveRoom(op.param1)
                kr2.leaveRoom(op.param1)
                kr3.leaveRoom(op.param1)
                kr4.leaveRoom(op.param1)
                kr5.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                kr.leaveRoom(op.param1)
                kr1.leaveRoom(op.param1)
                kr2.leaveRoom(op.param1)
                kr3.leaveRoom(op.param1)
                kr4.leaveRoom(op.param1)
                kr5.leaveRoom(op.param1)
#==========================[Kris]===========================
        if op.type == 25:
            msg = op.message
#==========================[Kris]===========================
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    kr.leaveRoom(msg.to)
                    kr1.leaveRoom(msg.to)
                    kr2.leaveRoom(msg.to)
                    kr3.leaveRoom(msg.to)
                    kr4.leaveRoom(msg.to)
                    kr5.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                random.choice(KAC).like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        random.choice(KAC).sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        random.choice(KAC).sendText(msg.to,"decided not to comment")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        kr1.sendText(msg.to,"deleted")
                        kr2.sendText(msg.to,"deleted")
                        kr3.sendText(msg.to,"deleted")
                        kr4.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        kr1.sendText(msg.to,"It is not in the black list")
                        kr2.sendText(msg.to,"It is not in the black list")
                        kr3.sendText(msg.to,"It is not in the black list")
                        kr4.sendText(msg.to,"It is not in the black list")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        kr1.sendText(msg.to,"already")
                        kr2.sendText(msg.to,"already")
                        kr3.sendText(msg.to,"already")
                        kr4.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        kr1.sendText(msg.to,"aded")
                        kr2.sendText(msg.to,"aded")
                        kr3.sendText(msg.to,"aded")
                        kr4.sendText(msg.to,"aded")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        kr1.sendText(msg.to,"deleted")
                        kr2.sendText(msg.to,"deleted")
                        kr3.sendText(msg.to,"deleted")
                        kr4.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        kr1.sendText(msg.to,"It is not in the black list")
                        kr2.sendText(msg.to,"It is not in the black list")
                        kr3.sendText(msg.to,"It is not in the black list")
                        kr4.sendText(msg.to,"It is not in the black list")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    kr1.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kr1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr1.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = kr1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr1.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�10��9�0�16�0�69�0�3�0�4\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(AST).sendText(msg.to,msg.text)
#==========================[Kris]===========================
            elif msg.text is None:
                return
            elif msg.text in ["help","Help"]:
					if wait["lang"] == "JP":
						kr1.sendText(msg.to,helpMessage)
						random.choice(AST).sendImageWithURL(msg.to, url123)
						random.choice(AST).sendText(msg.to,"↥↥↥↥↥↪ Owner Bots ↩↥↥↥↥↥")
					else:
						random.choice(AST).sendText(msg.to,helpMessage)
#==========================[Kris]===========================
            elif msg.text in ["Key1","key1"]:
					if wait["lang"] == "JP":
						kr1.sendText(msg.to,key1Message)
					else:
						random.choice(AST).sendText(msg.to,key1Message)
            elif msg.text in ["Key2","key2"]:
					if wait["lang"] == "JP":
						kr1.sendText(msg.to,key2Message)
					else:
						random.choice(AST).sendText(msg.to,key2Message)
            elif msg.text in ["Key3","key3"]:
					if wait["lang"] == "JP":
						kr1.sendText(msg.to,key3Message)
					else:
						random.choice(AST).sendText(msg.to,key3Message)
            elif msg.text in ["Key4","key4"]:
					if wait["lang"] == "JP":
						kr1.sendText(msg.to,key4Message)
					else:
						random.choice(AST).sendText(msg.to,key4Message)
#==========================[Kris]===========================
            elif ("Gn " in msg.text):
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						kr.updateGroup(X)
					else:
						kr.sendText(msg.to,"It can't be used besides the group.")
            elif ("Kr1 gn " in msg.text):
					if msg.toType == 2:
						X = kr1.getGroup(msg.to)
						X.name = msg.text.replace("Kr1 gn ","")
						kr1.updateGroup(X)
					else:
						kr1.sendText(msg.to,"It can't be used besides the group.")
            elif ("Kr2 gn " in msg.text):
					if msg.toType == 2:
						X = kr2.getGroup(msg.to)
						X.name = msg.text.replace("Kr2 gn ","")
						kr2.updateGroup(X)
					else:
						kr2.sendText(msg.to,"It can't be used besides the group.")
            elif ("Kr3 gn " in msg.text):
					if msg.toType == 2:
						X = kr3.getGroup(msg.to)
						X.name = msg.text.replace("Kr3 gn ","")
						kr3.updateGroup(X)
					else:
						kr3.sendText(msg.to,"It can't be used besides the group.")
#==========================[Kris]===========================
            elif "Kick " in msg.text:
					midd = msg.text.replace("Kick ","")
					kr.kickoutFromGroup(msg.to,[midd])
            elif "Kr1 kick " in msg.text:
					midd = msg.text.replace("Kr1 kick ","")
					kr1.kickoutFromGroup(msg.to,[midd])
            elif "Kr2 kick " in msg.text:
					midd = msg.text.replace("Kr2 kick ","")
					kr2.kickoutFromGroup(msg.to,[midd])
            elif "Kr3 kick " in msg.text:
					midd = msg.text.replace("Kr3 kick ","")
					kr3.kickoutFromGroup(msg.to,[midd])
#==========================[Kris]===========================
            elif "Invite " in msg.text:
					midd = msg.text.replace("Invite ","")
					kr.findAndAddContactsByMid(midd)
					kr.inviteIntoGroup(msg.to,[midd])
            elif "Kr1 invite " in msg.text:
					midd = msg.text.replace("Kr1 invite ","")
					kr1.findAndAddContactsByMid(midd)
					kr1.inviteIntoGroup(msg.to,[midd])
            elif "Kr2 invite " in msg.text:
					midd = msg.text.replace("Kr2 invite ","")
					kr2.findAndAddContactsByMid(midd)
					kr2.inviteIntoGroup(msg.to,[midd])
            elif "Kr3 invite " in msg.text:
					midd = msg.text.replace("Kr3 invite ","")
					kr3.findAndAddContactsByMid(midd)
					kr3.inviteIntoGroup(msg.to,[midd])
#==========================[Kris]===========================
            elif msg.text in ["Me","me"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': msg.from_}
                    kr.sendMessage(msg)
            elif msg.text in ["Kr1","kr1"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					kr1.sendMessage(msg)
            elif msg.text in ["Kr2","kr2"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kr2.sendMessage(msg)
            elif msg.text in ["Kr3","kr3"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Cmid}
					kr3.sendMessage(msg)
            elif msg.text in ["Kr4","kr4"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Dmid}
					kr4.sendMessage(msg)
            elif msg.text in ["Kr5","kr5"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Emid}
					kr5.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text in ["cancel","cancel"]:
					if msg.toType == 2:
						G = kr.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							kr.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								kr.sendText(msg.to,"No one is inviting")
							else:
								kr.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Can not be used outside the group")
						else:
							kr.sendText(msg.to,"Not for use less than group")
							
            elif msg.text in ["Kr cancel","kr cancel"]:
					if msg.toType == 2:
						G = kr1.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							kr1.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								kr1.sendText(msg.to,"No one is inviting")
							else:
								kr1.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Can not be used outside the group")
						else:
							kr1.sendText(msg.to,"Not for use less than group")
#==========================[Kris]===========================
            elif msg.text in ["Ourl","Link on","ourl","link on"]:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						X.preventJoinByTicket = False
						kr.updateGroup(X)
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Done")
						else:
							kr.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Can not be used outside the group")
						else:
							kr.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr1 ourl","Kr1 link on","kr1 ourl","kr1 link on"]:
					if msg.toType == 2:
						X = kr1.getGroup(msg.to)
						X.preventJoinByTicket = False
						kr1.updateGroup(X)
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Done")
						else:
							kr1.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Can not be used outside the group")
						else:
							kr1.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr2 ourl","Kr2 link on"]:
					if msg.toType == 2:
						X = kr2.getGroup(msg.to)
						X.preventJoinByTicket = False
						kr2.updateGroup(X)
						if wait["lang"] == "JP":
							kr2.sendText(msg.to,"Done")
						else:
							kr2.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kr2.sendText(msg.to,"Can not be used outside the group")
						else:
							kr2.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr3 ourl","Kr3 link on"]:
					if msg.toType == 2:
						X = kr3.getGroup(msg.to)
						X.preventJoinByTicket = False
						kr3.updateGroup(X)
						if wait["lang"] == "JP":
							kr3.sendText(msg.to,"Done")
						else:
							kr3.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kr3.sendText(msg.to,"Can not be used outside the group")
						else:
							kr3.sendText(msg.to,"Not for use less than group")
#==========================[Kris]===========================
            elif msg.text in ["Curl","Link off","curl","link off"]:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						X.preventJoinByTicket = True
						kr.updateGroup(X)
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Done")
						else:
							kr.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Can not be used outside the group")
						else:
							kr.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr1 curl","Kr1 link off"]:
					if msg.toType == 2:
						X = kr1.getGroup(msg.to)
						X.preventJoinByTicket = True
						kr1.updateGroup(X)
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Done")
						else:
							kr1.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Can not be used outside the group")
						else:
							kr1.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr2 curl","Kr2 link off"]:
					if msg.toType == 2:
						X = kr2.getGroup(msg.to)
						X.preventJoinByTicket = True
						kr2.updateGroup(X)
						if wait["lang"] == "JP":
							kr2.sendText(msg.to,"Done")
						else:
							kr2.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kr2.sendText(msg.to,"Can not be used outside the group")
						else:
							kr2.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr3 curl","Kr3 link off"]:
					if msg.toType == 2:
						X = kr3.getGroup(msg.to)
						X.preventJoinByTicket = True
						kr3.updateGroup(X)
						if wait["lang"] == "JP":
							kr3.sendText(msg.to,"Done")
						else:
							kr3.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kr3.sendText(msg.to,"Can not be used outside the group")
						else:
							kr3.sendText(msg.to,"Not for use less than group")
#==========================[Kris]===========================
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = kr.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        kr.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        kr.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
                        
            elif msg.text == "Kr ginfo":
                if msg.toType == 2:
                    ginfo = kr1.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        kr1.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        kr1.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kr1.sendText(msg.to,"Not for use less than group")
#==========================[Kris]===========================
            elif "All mid" == msg.text:
					kr.sendText(msg.to,mid)
					kr1.sendText(msg.to,Amid)
					kr2.sendText(msg.to,Bmid)
					kr3.sendText(msg.to,Cmid)
					kr4.sendText(msg.to,Dmid)
					kr5.sendText(msg.to,Emid)
            elif "Mid" == msg.text:
					kr.sendText(msg.to,mid)
            elif "Kr1 mid" == msg.text:
					kr1.sendText(msg.to,Amid)
            elif "Kr2 mid" == msg.text:
					kr2.sendText(msg.to,Bmid)
            elif "Kr3 mid" == msg.text:
					kr3.sendText(msg.to,Cmid)
            elif "Kr4 mid" == msg.text:
					kr4.sendText(msg.to,Cmid)
            elif "Kr5 mid" == msg.text:
					kr5.sendText(msg.to,Cmid)
#==========================[Kris]===========================
            elif msg.text in ["Wkwk"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["Galon"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["You"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["Please"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["Haaa"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["Lol"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
            elif msg.text in ["Come"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					kr2.sendMessage(msg)
					kr3.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text in ["TL "]:
					tl_text = msg.text.replace("TL ","")
					kr1.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr1.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==========================[Kris]===========================
            elif msg.text in ["Undang","undang"]:
                 wait["winvite"] = True
                 kr.sendText(msg.to,"send contact")
            elif msg.text in ["Jepit","jepit"]:
                 wait["winvite"] = True
                 kr1.sendText(msg.to,"send contact")
            elif msg.text in ["Tarik","tarik"]:
                 wait["winvite"] = True
                 kr2.sendText(msg.to,"send contact")
#==========================[Kris]===========================
            elif "Rename " in msg.text:
                    string = msg.text.replace("Rename ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr.getProfile()
                        profile.displayName = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Changed " + string + "")
#==========================[Kris]===========================
            elif "Rename1 " in msg.text:
                    string = msg.text.replace("Rename1 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr1.getProfile()
                        profile.displayName = string
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Changed " + string + "")
            elif "Rename2 " in msg.text:
                    string = msg.text.replace("Rename2 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr2.getProfile()
                        profile.displayName = string
                        kr2.updateProfile(profile)
                        kr2.sendText(msg.to,"Changed " + string + "")
            elif "Rename3 " in msg.text:
                    string = msg.text.replace("Rename3 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr3.getProfile()
                        profile.displayName = string
                        kr3.updateProfile(profile)
                        kr3.sendText(msg.to,"Changed " + string + "")
            elif "Rename4 " in msg.text:
                    string = msg.text.replace("Rename4 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr4.getProfile()
                        profile.displayName = string
                        kr4.updateProfile(profile)
                        kr4.sendText(msg.to,"Changed " + string + "")
            elif "Rename5 " in msg.text:
                    string = msg.text.replace("Rename5 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr5.getProfile()
                        profile.displayName = string
                        kr5.updateProfile(profile)
                        kr5.sendText(msg.to,"Changed " + string + "")
#==========================[Kris]===========================
            elif "Allrename " in msg.text:
                    string = msg.text.replace("Allrename ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr.getProfile()
                        profile.displayName = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Changed " + string + "")
                        profile = kr1.getProfile()
                        profile.displayName = string
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Changed " + string + "")
                        profile = kr2.getProfile()
                        profile.displayName = string
                        kr2.updateProfile(profile)
                        kr2.sendText(msg.to,"Changed " + string + "")
                        profile = kr3.getProfile()
                        profile.displayName = string
                        kr3.updateProfile(profile)
                        kr3.sendText(msg.to,"Changed " + string + "")
                        profile = kr4.getProfile()
                        profile.displayName = string
                        kr4.updateProfile(profile)
                        kr4.sendText(msg.to,"Changed " + string + "")
                        profile = kr5.getProfile()
                        profile.displayName = string
                        kr5.updateProfile(profile)
                        kr5.sendText(msg.to,"Changed " + string + "")
#==========================[Kris]===========================
            elif "Bio " in msg.text:
                    string = msg.text.replace("Bio ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr.getProfile()
                        profile.statusMessage = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Changed " + string)
#==========================[Kris]===========================
            elif "Allbio " in msg.text:
                    string = msg.text.replace("Allbio ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr.getProfile()
                        profile.statusMessage = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Changed " + string)
                        profile = kr1.getProfile()
                        profile.statusMessage = string
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Changed " + string)
                        profile = kr2.getProfile()
                        profile.statusMessage = string
                        kr2.updateProfile(profile)
                        kr2.sendText(msg.to,"Changed " + string)
                        profile = kr3.getProfile()
                        profile.statusMessage = string
                        kr3.updateProfile(profile)
                        kr3.sendText(msg.to,"Changed " + string)
                        profile = kr4.getProfile()
                        profile.statusMessage = string
                        kr4.updateProfile(profile)
                        kr4.sendText(msg.to,"Changed " + string)
                        profile = kr5.getProfile()
                        profile.statusMessage = string
                        kr5.updateProfile(profile)
                        kr5.sendText(msg.to,"Changed " + string)
#==========================[Kris]===========================
            elif msg.text in ["Guest On","guest on"]:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Guest Stranger On")
                    else:
                        kr1.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Guest Stranger On")
                    else:
                        kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Guest Off","guest off"]:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Guest Stranger Off")
                    else:
                        kr1.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Guest Stranger Off")
                    else:
                        kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Kontak on","kontak on"]:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already on")
						else:
							kr1.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already on")
						else:
							kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Kontak off","kontak off"]:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already off")
						else:
							kr1.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already off")
						else:
							kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Join on","join on"]:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already on")
						else:
							kr1.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already on")
						else:
							kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Join off","join off"]:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already off")
						else:
							kr1.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already off")
						else:
							kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Gcancel "]:
					try:
						strnum = msg.text.replace("Gcancel ","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								kr1.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								kr1.sendText(msg.to,"Done")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								kr1.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								kr1.sendText(msg.to,strnum + "Done")
					except:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Value is wrong")
						else:
							kr1.sendText(msg.to,"Bizarre ratings")
#==========================[Kris]===========================
            elif msg.text in ["Leave on","leave on"]:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already on")
						else:
							kr1.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"done")
						else:
							kr1.sendText(msg.to,"Already on")
#==========================[Kris]===========================
            elif msg.text in ["Leave off","leave off"]:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already off")
						else:
							kr1.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"done")
						else:
							kr1.sendText(msg.to,"already off")
#==========================[Kris]===========================
            elif msg.text in ["Share on","share on"]:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already on")
						else:
							kr1.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"done")
						else:
							kr1.sendText(msg.to,"Already on")
#==========================[Kris]===========================
            elif msg.text in ["Share off","share off"]:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"already off")
						else:
							kr1.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"done")
						else:
							kr1.sendText(msg.to,"Already off")
#==========================[Kris]===========================
            elif msg.text in ["Status","status"]:
					md = ""
					if wait["contact"] == True: md+="🌂  CONTACT : [✅]\n"
					else: md+="🌂  CONTACT : [❌]\n"
					if wait["autoJoin"] == True: md+="🌂  AUTOJOIN : [✅]\n"
					else: md +="🌂  AUTOJOIN : [❌]\n"
					if wait["autoCancel"]["on"] == True:md+="🌂  GROUP CANCEL :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+="🌂  GROUP CANCEL : [❌]\n"
					if wait["leaveRoom"] == True: md+="🌂  AUTOLEAVE : [✅]\n"
					else: md+="🌂  AUTOLEAVE : [❌]\n"
					if wait["timeline"] == True: md+="🌂  SHARE : [✅]\n"
					else:md+="🌂  SHARE : [❌]\n"
					if wait["autoAdd"] == True: md+="🌂  AUTOADD : [✅]\n"
					else:md+="🌂  AUTOADD : [❌]\n"
					if wait["commentOn"] == True: md+="🌂  COMMENT : [✅]\n"
					else:md+="🌂  COMMENT : [❌]\n"
					if wait["likeOn"] == True: md+="🌂  AUTOLIKE : [✅]\n"
					else:md+="🌂  AUTOLIKE : [❌]\n"
					if wait["QrProtect"] == True: md+="🌂  PROTECT QR : [✅]\n"
					else:md+="🌂  PROTECT QR : [❌]\n"
					if wait["MProtection"] == True:md+="🌂  PROTECT MEMBER : [✅]\n"
					else:md+="🌂  PROTECT MEMBER : [❌]\n"
					if wait["Protectguest"] == True:md+="🌂  PROTECT GUEST : [✅]\n"
					else:md+="🌂  PROTECT GUEST : [❌]\n"
					if wait["Protectcancel"] == True:md+="🌂  PROTECT CANCEL : [✅]\n"
					else:md+="🌂  PROTECT CANCEL : [❌]\n"
					if wait["autoKick"] == True:md+="🌂  PROTECT KICK : [✅]\n"
					else:md+="🌂  PROTECT KICK : [❌]\n"
					if wait["Wc"] == True: md+="🌂  SAMBUTAN : [✅]\n"
					else:md+="🌂  SAMBUTAN : [❌]\n"
					if wait["Wc2"] == True: md+="🌂  SAMBUTPOTO : [✅]\n"
					else:md+="🌂  SAMBUTPOTO : [❌]\n"
					if wait["Lv"] == True: md+="🌂  PERGI : [✅]\n"
					else:md+="🌂  PERGI : [❌]\n"
					if wait["tag"] == True: md+="🌂  TAG 1 : [✅]\n"
					else:md+="🌂  TAG 1 : [❌]\n"
					if wait["tag2"] == True: md+="🌂  TAG 2 KICK : [✅]\n"
					else:md+="🌂  TAG 2 KICK : [❌]\n"
					kr1.sendText(msg.to,md)
            elif msg.text in ["Set","set"]:
					md = ""
					if wait["contact"] == True: md+="🌂  CONTACT : [✅]\n"
					else: md+="🌂  CONTACT : [❌]\n"
					if wait["autoJoin"] == True: md+="🌂  AUTOJOIN : [✅]\n"
					else: md +="🌂  AUTOJOIN : [❌]\n"
					if wait["autoCancel"]["on"] == True:md+="🌂  GROUP CANCEL :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+="🌂  GROUP CANCEL : [❌]\n"
					if wait["leaveRoom"] == True: md+="🌂  AUTOLEAVE : [✅]\n"
					else: md+="🌂  AUTOLEAVE : [❌]\n"
					if wait["timeline"] == True: md+="🌂  SHARE : [✅]\n"
					else:md+="🌂  SHARE : [❌]\n"
					if wait["autoAdd"] == True: md+="🌂  AUTOADD : [✅]\n"
					else:md+="🌂  AUTOADD : [❌]\n"
					if wait["commentOn"] == True: md+="🌂  COMMENT : [✅]\n"
					else:md+="🌂  COMMENT : [❌]\n"
					if wait["likeOn"] == True: md+="🌂  AUTOLIKE : [✅]\n"
					else:md+="🌂  AUTOLIKE : [❌]\n"
					if wait["QrProtect"] == True: md+="🌂  PROTECT QR : [✅]\n"
					else:md+="🌂  PROTECT QR : [❌]\n"
					if wait["MProtection"] == True:md+="🌂  PROTECT MEMBER : [✅]\n"
					else:md+="🌂  PROTECT MEMBER : [❌]\n"
					if wait["Protectguest"] == True:md+="🌂  PROTECT GUEST : [✅]\n"
					else:md+="🌂  PROTECT GUEST : [❌]\n"
					if wait["Protectcancel"] == True:md+="🌂  PROTECT CANCEL : [✅]\n"
					else:md+="🌂  PROTECT CANCEL : [❌]\n"
					if wait["autoKick"] == True:md+="🌂  PROTECT KICK : [✅]\n"
					else:md+="🌂  PROTECT KICK : [❌]\n"
					if wait["Wc"] == True: md+="🌂  SAMBUTAN : [✅]\n"
					else:md+="🌂  SAMBUTAN : [❌]\n"
					if wait["Wc2"] == True: md+="🌂  SAMBUTPOTO : [✅]\n"
					else:md+="🌂  SAMBUTPOTO : [❌]\n"
					if wait["Lv"] == True: md+="🌂  PERGI : [✅]\n"
					else:md+="🌂  PERGI : [❌]\n"
					if wait["tag"] == True: md+="🌂  TAG 1 : [✅]\n"
					else:md+="🌂  TAG 1 : [❌]\n"
					if wait["tag2"] == True: md+="🌂  TAG 2 KICK : [✅]\n"
					else:md+="🌂  TAG 2 KICK : [❌]\n"
					kr.sendText(msg.to,md)
#==========================[Kris]===========================
            elif msg.text in ["Tolak","tolak"]:
					gid = kr.getGroupIdsInvited()
					gid = kr1.getGroupIdsInvited()
					gid = kr2.getGroupIdsInvited()
					gid = kr3.getGroupIdsInvited()
					gid = kr4.getGroupIdsInvited()
					gid = kr5.getGroupIdsInvited()
					for i in gid:
						kr.rejectGroupInvitation(i)
						kr1.rejectGroupInvitation(i)
						kr2.rejectGroupInvitation(i)
						kr3.rejectGroupInvitation(i)
						kr4.rejectGroupInvitation(i)
						kr5.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						kr1.sendText(msg.to,"All invitations have been refused")
					else:
						kr1.sendText(msg.to,"All invitations have been refused")
#==========================[Kris]===========================
            elif msg.text in ["Add on","add on"]:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Add already on")
						else:
							kr1.sendText(msg.to,"Add done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Add done")
						else:
							kr1.sendText(msg.to,"Add Already on")
#==========================[Kris]===========================
            elif msg.text in ["Add off","add off"]:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Add already off")
						else:
							kr1.sendText(msg.to,"Add done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Add done")
						else:
							kr1.sendText(msg.to,"Add Already off")
#==========================[Kris]===========================
            elif "Message change " in msg.text:
					wait["message"] = msg.text.replace("Message change ","")
					kr1.sendText(msg.to,"message changed")
					
            elif "Message add " in msg.text:
					wait["message"] = msg.text.replace("Message add ","")
					if wait["lang"] == "JP":
						kr1.sendText(msg.to,"message changed")
					else:
						kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Pesan","pesan"]:
					if wait["lang"] == "JP":
						kr1.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						kr1.sendText(msg.to,"The automatic appending information is set as follows\n\n" + wait["message"])
#==========================[Kris]===========================
            elif "Comment " in msg.text:
					c = msg.text.replace("Comment ","")
					if c in [""," ","\n",None]:
						kr1.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						kr1.sendText(msg.to,"changed\n\n" + c)
#==========================[Kris]===========================
            elif "Add comment " in msg.text:
					c = msg.text.replace("Add comment ","")
					if c in [""," ","\n",None]:
						kr1.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						kr1.sendText(msg.to,"changed\n\n" + c)
#==========================[Kris]===========================
            elif msg.text in ["Comment on","comment:on"]:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"done")
						else:
							kr1.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"done")
						else:
							kr1.sendText(msg.to,"Alredy on")
#==========================[Kris]===========================
            elif msg.text in ["Comment on","comment off"]:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"done")
						else:
							kr1.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"done")
						else:
							kr1.sendText(msg.to,"Already off")
#==========================[Kris]===========================
            elif msg.text in ["Gurl"]:
					if msg.toType == 2:
						x = kr.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kr.updateGroup(x)
						gurl = kr.reissueGroupTicket(msg.to)
						kr.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Can't be used outside the group")
						else:
							kr.sendText(msg.to,"Not for use less than group")
							
            elif msg.text in ["Kr1 gurl"]:
					if msg.toType == 2:
						x = kr1.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kr1.updateGroup(x)
						gurl = kr1.reissueGroupTicket(msg.to)
						kr1.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							kr1.sendText(msg.to,"Can't be used outside the group")
						else:
							kr1.sendText(msg.to,"Not for use less than group")
							
            elif msg.text in ["Kr2 gurl"]:
					if msg.toType == 2:
						x = kr2.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kr2.updateGroup(x)
						gurl = kr2.reissueGroupTicket(msg.to)
						kr2.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							kr2.sendText(msg.to,"Can't be used outside the group")
						else:
							kr2.sendText(msg.to,"Not for use less than group")
							
            elif msg.text in ["Kr3 gurl"]:
					if msg.toType == 2:
						x = kr3.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kr3.updateGroup(x)
						gurl = kr3.reissueGroupTicket(msg.to)
						kr3.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							kr3.sendText(msg.to,"Can't be used outside the group")
						else:
							kr3.sendText(msg.to,"Not for use less than group")
#==========================[Kris]===========================
            elif msg.text in ["Comment bl "]:
					wait["wblack"] = True
					kr1.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
					wait["dblack"] = True
					kr1.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Confirm","confirm"]:
					if wait["commentBlack"] == {}:
						kr1.sendText(msg.to,"confirmed")
					else:
						kr1.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +kr1.getContact(mi_d).displayName + "\n"
						kr1.sendText(msg.to,mc)
#==========================[Kris]===========================
            elif msg.text in ["Jam on"]:
					if wait["clock"] == True:
						kr1.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = kr1.getProfile()
						profile.displayName = wait["cName"] + nowT
						kr1.updateProfile(profile)
						kr1.sendText(msg.to,"done")
						
            elif msg.text in ["Jam off"]:
					if wait["clock"] == False:
						kr1.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						kr1.sendText(msg.to,"done")
						
            elif msg.text in ["Change clock "]:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						kr1.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						kr1.sendText(msg.to,"changed to\n\n" + n)
						
            elif msg.text in ["Up"]:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = kr1.getProfile()
						profile.displayName = wait["cName"] + nowT
						kr1.updateProfile(profile)
						kr1.sendText(msg.to,"Updated")
					else:
						kr1.sendText(msg.to,"Please turn on the name clock")
#==========================[Kris]===========================
            elif msg.text == "Cctv":
                    kr1.sendText(msg.to, "Check sider"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Toong":
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2['ROM'][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        kr1.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal \n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        kr1.sendText(msg.to, "An already read point has not been set.\n¡¸Cctv¡¹you can send  read point will be created ")
#==========================[Kris]===========================
            elif "Cctv" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         kr1.sendText(msg.to,"Cctv sudah menyala silahkan masukan command [Check]")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     kr1.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

            elif "Cctv off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    kr1.sendText(msg.to,"Set Reading point tidak di temukan")
                    kr1.sendText(msg.to,"Silahkan masukan Command [Cctv on] untuk set point")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    kr1.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                    
            elif "Check" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             kr1.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = kr1.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          kr1.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        kr1.sendText(msg.to, "cctv has not been set.")
#==========================[Kris]===========================
            elif msg.text == "Cctv":
                    kr1.sendText(msg.to, "Lurking Is Starting!! "+ datetime.today().strftime('%H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text in ["Intip"]:
                 if msg.toType == 2:
                    print "\nRead aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2['ROM'][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        kr1.sendText(msg.to, "Sider :\n  ===========================                     %s\n===========================\n\nReader :\n%s\n===========================\nIn the last seen point:\n[%s]\n===========================" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "lukers"
                        kr1.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                    else:
                        kr1.sendText(msg.to, "Ketik => [Cctv] untuk cek sider ketik => [Intip]")
#==========================[Kris]===========================
            elif msg.text in ["Crot"]:
                    group = kr1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range (0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range (100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200 and jml < 300:
                        for i in range (0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range (100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range (200, len(nama)-1):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                    if jml > 300 and jml < 400:
                        for i in range (0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range (100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range (200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range (300, len(nama)-1):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                    cnt = Message()
                    cnt.text = "Hasil Tag : "+str(jml)
                    cnt.to = msg.to
                    kr1.sendText(msg.to,"TAGALL SUCCESS")
                    kr1.sendMessage(cnt)
#==========================[Kris]===========================
            elif msg.text in ["Kr","kr"]:
					G = kr.getGroup(msg.to)
					ginfo = kr.getGroup(msg.to)
					G.preventJoinByTicket = True
					kr.updateGroup(G)
					invsend = 0
					Ticket = kr.reissueGroupTicket(msg.to)
					kr1.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.1)
					kr2.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.1)
					kr3.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.1)
					kr4.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.1)
					kr5.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.1)
					G = kr1.getGroup(msg.to)
					G.preventJoinByTicket = True
					kr1.updateGroup(G)
					print "Semua Udah Masuk"
					G.preventJoinByTicket(G)
					kr1.updateGroup(G)
#==========================[Kris]===========================
            elif msg.text in ["."]:
                midd1 = msg.text.replace(".",Amid)
                midd2 = msg.text.replace(".",Bmid)
                midd3 = msg.text.replace(".",Cmid)
                midd4 = msg.text.replace(".",Dmid)
                midd5 = msg.text.replace(".",Emid)
                kr.findAndAddContactsByMid(midd1)
                kr.findAndAddContactsByMid(midd2)
                kr.findAndAddContactsByMid(midd3)
                kr.findAndAddContactsByMid(midd4)
                kr.findAndAddContactsByMid(midd5)
                kr.inviteIntoGroup(msg.to,[midd1])
                kr.inviteIntoGroup(msg.to,[midd2])
                kr.inviteIntoGroup(msg.to,[midd3])
                kr.inviteIntoGroup(msg.to,[midd4])
                kr.inviteIntoGroup(msg.to,[midd5])
                kr1.acceptGroupInvitation(msg.to)
                kr2.acceptGroupInvitation(msg.to)
                kr3.acceptGroupInvitation(msg.to)
                kr4.acceptGroupInvitation(msg.to)
                kr5.acceptGroupInvitation(msg.to)
                
            elif msg.text in ["1"]:
                midd1 = msg.text.replace("1",Amid)
                kr.findAndAddContactsByMid(midd1)
                kr.inviteIntoGroup(msg.to,[midd1])
                kr1.acceptGroupInvitation(msg.to)
                
            elif msg.text in ["2"]:
                midd2 = msg.text.replace("2",Bmid)
                kr1.findAndAddContactsByMid(midd2)
                kr1.inviteIntoGroup(msg.to,[midd2])
                kr2.acceptGroupInvitation(msg.to)
                
            elif msg.text in ["3"]:
                midd3 = msg.text.replace("3",Cmid)
                kr2.findAndAddContactsByMid(midd3)
                kr2.inviteIntoGroup(msg.to,[midd3])
                kr3.acceptGroupInvitation(msg.to)
                
            elif msg.text in ["4"]:
                midd4 = msg.text.replace("4",Dmid)
                kr3.findAndAddContactsByMid(midd4)
                kr3.inviteIntoGroup(msg.to,[midd4])
                kr4.acceptGroupInvitation(msg.to)
                
            elif msg.text in ["5"]:
                midd5 = msg.text.replace("5",Emid)
                kr4.findAndAddContactsByMid(midd5)
                kr4.inviteIntoGroup(msg.to,[midd5])
                kr5.acceptGroupInvitation(msg.to)
#==========================[Kris]===========================
            elif "Kr bye" in msg.text:
                    if msg.toType == 2:
                        ginfo = kr.getGroup(msg.to)
                        ginfo = kr1.getGroup(msg.to)
                        ginfo = kr2.getGroup(msg.to)
                        ginfo = kr3.getGroup(msg.to)
                        ginfo = kr4.getGroup(msg.to)
                        ginfo = kr5.getGroup(msg.to)
                        try:
                            kr1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            kr5.leaveGroup(msg.to)
                            kr4.leaveGroup(msg.to)
                            kr3.leaveGroup(msg.to)
                            kr2.leaveGroup(msg.to)
                            kr1.leaveGroup(msg.to)
                        except:
                            pass
                        
            elif "x" in msg.text:
                    if msg.toType == 2:
                        ginfo = kr.getGroup(msg.to)
                        ginfo = kr1.getGroup(msg.to)
                        ginfo = kr2.getGroup(msg.to)
                        ginfo = kr3.getGroup(msg.to)
                        ginfo = kr4.getGroup(msg.to)
                        ginfo = kr5.getGroup(msg.to)
                        try:
                            kr2.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            kr5.leaveGroup(msg.to)
                            kr4.leaveGroup(msg.to)
                            kr3.leaveGroup(msg.to)
                            kr2.leaveGroup(msg.to)
                            #kr1.leaveGroup(msg.to)
                        except:
                            pass
#==========================[Kris]===========================
            elif "Glist" in msg.text:
                        gid = kr1.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "☄ %s  \n" % (kr1.getGroup(i).name + " 👥 ▄ [ " + str(len (kr1.getGroup(i).members))+" ]")
                        kr1.sendText(msg.to, "     ☄ [ ♡List Grup♄ ] ☜\n"+ h +"Total Group ▄" +"[ "+str(len(gid))+" ]")
            elif msg.text.lower() == 'Bot':
                kr.sendImageWithURL(msg.to, url123)
                kr.sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
#==========================[Kris]===========================
            elif "Dadas" in msg.text:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Dadas","")
                        gs = kr1.getGroup(msg.to)
                        gs = kr2.getGroup(msg.to)
                        gs = kr3.getGroup(msg.to)
                        gs = kr4.getGroup(msg.to)
                        gs = kr5.getGroup(msg.to)
                        kr1.sendText(msg.to,"Perintah DiLaksanakan Maaf Kan Ya :v Ã´")
                        targets = []
                        for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
                        if targets == []:
							kr1.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                if target not in Bots:
                                    try:
                                        klist=[kr1,kr2,kr3,kr4,kr5]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        kr1.sendText(msg.to,"Group Dibersihkan")
#==========================[Kris]===========================
            elif msg.text in ["Salam1"]:
                kr1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr1.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                kr1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr1.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam3" in msg.text:
                kr1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr1.sendText(msg.to,"Assalamu'alaikum")
                kr1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                kr1.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam3","")
                    gs = kr1.getGroup(msg.to)
                    gs = kr2.getGroup(msg.to)
                    gs = kr3.getGroup(msg.to)
                    gs = kr4.getGroup(msg.to)
                    gs = kr5.getGroup(msg.to)
                    kr1.sendText(msg.to,"maaf kalo gak sopan")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            if target not in Bots:
                                try:
                                    klist=[kr1,kr2,kr3,kr4,kr5]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kr1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                    kr1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                    kr1.sendText(msg.to,"Nah salamnya jawab sendiri dah")
#==========================[Kris]===========================
            elif "Kiss " in msg.text:
                    nk0 = msg.text.replace("Kiss ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = kr.getGroup(msg.to)
                    ginfo = kr.getGroup(msg.to)
                    midd2 = (Bmid)
                    gs.findAndAddContactsByMid(midd2)
                    kr.inviteIntoGroup(gs)
                    midd2 = kr.inviteIntoGroup(msg.to,[midd2])
                    kr2.acceptGroupInvitation(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                kr2.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kr2.leaveGroup(msg.to)
                                gs = kr.getGroup(msg.to)
#==========================[Kris]===========================
            elif "Tajong " in msg.text:
                    nk0 = msg.text.replace("Tajong ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = kr.getGroup(msg.to)
                    ginfo = kr.getGroup(msg.to)
                    gs.preventJoinByTicket = False
                    kr.updateGroup(gs)
                    invsend = 0
                    Ticket = kr.reissueGroupTicket(msg.to)
                    kr5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                kr5.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kr5.leaveGroup(msg.to)
                                gs = kr.getGroup(msg.to)
                                gs.preventJoinByTicket = True
                                kr.updateGroup(gs)
                                gs.preventJoinByTicket(gs)
                                kr.updateGroup(gs)
#==========================[Kris]===========================
            elif "Ban @" in msg.text:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = kr1.getGroup(msg.to)
						gs = kr1.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							kr1.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									kr1.sendText(msg.to,"Berhasil Memban")
								except:
									kr1.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = kr1.getGroup(msg.to)
						gs = kr1.getGroup(msg.to)
						gs = kr4.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							kr1.sendText(msg.to,"Tidak DiTemukan")
							kr1.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									kr1.sendText(msg.to,"Berhasil")
								except:
									kr1.sendText(msg.to,"Berhasil")
#==========================[Kris]===========================
            elif "Cium " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kr1.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
                  
            elif "z " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kr.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#==========================[Kris]===========================
            elif msg.text.lower() == 'crash':
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr2.sendMessage(msg)
                    kr2.sendMessage(msg)
                    
            elif msg.text.lower() == 'ah':
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr.sendMessage(msg)
                    kr.sendMessage(msg)
                    kr.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text in ["Mode On","mode on"]:
                    if wait["QrProtect"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect QR On")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect QR On")
                        else:
                            kr1.sendText(msg.to,"done")
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection On")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection On")
                        else:
                            kr1.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        kr1.sendText(msg.to,"TURN ON")
                    else:
                        kr1.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = kr1.getGroup(msg.to).name
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Already on")
                        else:
                            kr1.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Tag On")
                        else:
                            kr1.sendText(msg.to,"already on")
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Yang ngeTag Kick on")
                        else:
                            kr1.sendText(msg.to,"Yang ngeTag Kick on")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Yang ngeTag Kick on")
                        else:
                            kr1.sendText(msg.to,"Yang ngeTag Kick on")
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Guest Stranger On")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Guest Stranger On")
                        else:
                            kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Mode Off","mode off"]:
                    if wait["QrProtect"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect QR Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect QR Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        kr1.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        kr1.sendText(msg.to,"ALREADY OFF")
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Protect already oғғ")
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Nayapa yg gabung already oғғ")
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"noтιғ leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Nayapa yg left already oғғ")
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Kick already oғғ")
                    if wait["tag"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Already Tag off")
                        else:
                            kr1.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Tag Off")
                        else:
                            kr1.sendText(msg.to,"Already Tag off")
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Yang ngeTag Kick off")
                        else:
                            kr1.sendText(msg.to,"Yang ngeTag Kick off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Yang ngeTag Kick off")
                        else:
                            kr1.sendText(msg.to,"Yang ngeTag Kick off")
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Guest Stranger Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Guest Stranger Off")
                        else:
                            kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Qr On","qr on"]:
                if wait["QrProtect"] == True:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Protect QR On")
                    else:
                        kr1.sendText(msg.to,"done")
                else:
                    wait["QrProtect"] = True
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Protect QR On")
                    else:
                        kr1.sendText(msg.to,"done")
            elif msg.text in ["Qr Off","qr off"]:
                if wait["QrProtect"] == False:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Protect QR Off")
                    else:
                        kr1.sendText(msg.to,"done")
                else:
                    wait["QrProtect"] = False
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Protect QR Off")
                    else:
                        kr1.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Member On"]:
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection On")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection On")
                        else:
                            kr1.sendText(msg.to,"done")
            elif msg.text in ["Member Off"]:
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection Off")
                        else:
                            kr1.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Member Protection Off")
                        else:
                            kr1.sendText(msg.to,"done")
            elif msg.text in ["Respoto on","respoto on"]:
                    wait["detectMention"] = True
                    kr1.sendText(msg.to,"Auto respon tag Pict On")
                
            elif msg.text in ["Respoto off","respoto off"]:
                    wait["detectMention"] = False
                    kr1.sendText(msg.to,"Auto respon tag Pict Off")
#==========================[Kris]===========================
            elif msg.text in ["Creator","creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
					kr2.sendMessage(msg)
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u9cc2323f5b84f9df880c33aa9f9e3ae1"}
					kr2.sendMessage(msg)
					url = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")
					kr1.sendImageWithURL(msg.to, url)
					kr1.sendText(msg.to,"MyCreator\nyang bikin Bot ini...!!!")
#==========================[Kris]===========================
            elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                            for x in range(jmlh):
                                kr1.sendText(msg.to, teks)
                        else:
                            kr1.sendText(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            kr1.sendText(msg.to, tulisan)
                        else:
                            kr1.sendText(msg.to, "Out Of Range!")
#==========================[Kris]===========================
            elif "v " in msg.text.lower():
                say = msg.text.lower().replace("v ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr1.sendAudio(msg.to,"hasil.mp3")
#==========================[Kris]===========================
            elif 'wiki ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wiki ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    kr1.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            kr1.sendText(msg.to, pesan)
                        except Exception as e:
                            kr1.sendText(msg.to, str(e))
#==========================[Kris]===========================
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa Jadi","Mungkin")
                jawaban = random.choice(jawab)
                kr1.sendText(msg.to,jawaban)
                kr1.sendText(msg.to,jawaban)
                kr1.sendText(msg.to,jawaban)
                
            elif msg.text in ["Nah","nah"]:
                kr1.sendText(msg.to,"Kan")
                kr1.sendText(msg.to,"Kan")
                
            elif msg.text in ["Sepi","sepi"]:
                kr1.sendText(msg.to,"Ada yang manis disini kak, msh setia menemani..(*-*)")
                kr1.sendText(msg.to,"Ada yang manis disini kak, msh setia menemani..(*-*)")
#==========================[Kris]===========================
            elif "Berapa " in msg.text:
                tanya = msg.text.replace("Berapa ","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                kr1.sendText(msg.to,jawaban)
                kr1.sendText(msg.to,jawaban)
#==========================[Kris]===========================
            elif "Getname @" in msg.text:
                    _name = msg.text.replace("Getname @","")
                    _nametarget = _name.rstrip(" ")
                    gs = kr1.getGroup(msg.to)
                    for h in gs.members:
                        if _nametarget == h.displayName:
                            kr1.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                        else:
                            pass
#==========================[Kris]===========================
            elif "Getbio @" in msg.text:
                    _name = msg.text.replace("Getbio @","")
                    _nametarget = _name.rstrip(" ")
                    gs = kr1.getGroup(msg.to)
                    for h in gs.members:
                        if _nametarget == h.displayName:
                            kr1.sendText(msg.to,"[Status]:\n" + h.statusMessage )
                        else:
                            pass
#==========================[Kris]===========================
            elif "zodiak " in msg.text:
                tanggal = msg.text.replace("zodiak ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                kr1.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
#==========================[Kris]===========================
            elif msg.text in ["Invite creator"]:
                    ginfo = kr1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        kr1.findAndAddContactsByMid(gCreator)
                        kr1.inviteIntoGroup(msg.to,[gCreator])
                        print "success inv gCreator"
                    except:
                        pass
#==========================[Kris]===========================
            elif msg.text in ["Gcreator kick"]:
                    ginfo = kr1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        kr1.findAndAddContactsByMid(gCreator)
                        kr1.kickoutFromGroup(msg.to,[gCreator])
                        print "success inv gCreator"
                    except:
                        pass
#==========================[Kris]===========================
            elif "Stalk " in msg.text:
                    print "[Command]Stalk executing"
                    stalkID = msg.text.replace("Stalk ","")
                    subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])
                    files = glob.glob("tmp/*.jpg")
                    for file in files:
                        os.rename(file,"tmp/tmp.jpg")
                    fileTmp = glob.glob("tmp/tmp.jpg")
                    if not fileTmp:
                        kr1.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                        print "[Command]Stalk,executed - no image found"
                    else:
                        image = upload_tempimage(client)
                        kr1.sendText(msg.to, format(image['link']))
                        subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                        print "[Command]Stalk executed - succes"
#==========================[Kris]===========================
            elif "Gbc " in msg.text:
                    bctxt = msg.text.replace("Gbc ", "")
                    n = kr1.getGroupIdsJoined()
                    for manusia in n:
                        kr1.sendText(manusia, (bctxt) + "\n╠═════[BROADCAST]═════╣\n\n=>>line://ti/p/~krissthea\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")
            elif "Pm cast " in msg.text:
					bctxt = msg.text.replace("Pm cast ", "")
					t = kr1.getAllContactIds()
					for manusia in t:
						kr1.sendText(manusia,(bctxt))
            elif "Fbc " in msg.text:
                    bctxt = msg.text.replace("Fbc ", "")
                    t = kr1.getAllContactIds()
                    for manusia in t:
                        kr1.sendText(manusia, (bctxt))
#==========================[Kris]===========================
            elif "Asupka " in msg.text:
                if msg.from_ in owner:
                    gid = msg.text.replace("Asupka ","")
                    if gid == "":
                        kr1.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            kr1.findAndAddContactsByMid(msg.from_)
                            kr1.inviteIntoGroup(gid,[msg.from_])
                        except:
                            kr1.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#==========================[Kris]===========================
            elif "Getcover @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getcover @","")
                _nametarget = _name.rstrip('  ')
                gs = kr1.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr1.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr1.getContact(target)
                            cu = kr1.channel.getCover(target)
                            path = str(cu)
                            kr1.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#==========================[Kris]===========================
            elif "Getpp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpp @","")
                _nametarget = _name.rstrip('  ')
                gs = kr1.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr1.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr1.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            kr1.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#==========================[Kris]===========================
            elif msg.text in ["Autolike on"]:
                    if wait["likeOn"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Done。")
                    else:
                        wait["likeOn"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Already。")
            elif msg.text in ["Autolike off"]:
                    if wait["likeOn"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Done。")
                    else:
                        wait["likeOn"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Already")
#==========================[Kris]===========================
            elif "Group On" in msg.text:
                    if msg.to in wait['pname']:
                        kr1.sendText(msg.to,"TURN ON")
                    else:
                        kr1.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = kr1.getGroup(msg.to).name
                        
            elif "Group Off" in msg.text:
                    if msg.to in wait['pname']:
                        kr1.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        kr1.sendText(msg.to,"ALREADY OFF")
#==========================[Kris]===========================
            elif "Turn off" in msg.text:
                try:
                    import sys
                    sys.exit()
                    kr1.sendText(msg.to, "Bot is Turn Off")
                except:
                    pass
#==========================[Kris]===========================
            elif msg.text in ["Cancel On"]:
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
                            
            elif msg.text in ["Cancel Off"]:
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Sambut on"]:
                if wait["Wc"] == True:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"noтιғ joιn on")
                else:
                    wait["Wc"] = True
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"already on")
                        
            elif msg.text in ["Sambut off"]:
                if wait["Wc"] == False:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"noтιғ joιn oғғ")
                else:
                    wait["Wc"] = False
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Sambutpoto on"]:
                if wait["Wc2"] == True:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"noтιғ joιn on")
                else:
                    wait["Wc2"] = True
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"already on")
                        
            elif msg.text in ["Sambutpoto off"]:
                if wait["Wc2"] == False:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"noтιғ joιn oғғ")
                else:
                    wait["Wc2"] = False
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["pergi on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"noтιғ leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"already on")
                        
            elif msg.text in ["pergi off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"noтιғ leave oғғ")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Kick On"]:
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already on")
                            
            elif msg.text in ["Kick Off"]:
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif "music " in msg.text.lower():
                try:
                    songname = msg.text.lower().replace("music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        kr1.sendText(msg.to, hasil)
                        kr1.sendText(msg.to, "Please Wait for audio...")
                        kr1.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                    kr1.sendText(msg.to, str(njer))
#==========================[Kris]===========================
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        kr1.sendText(msg.to, hasil)
                except Exception as wak:
                        kr1.sendText(msg.to, str(wak))
#==========================[Kris]===========================
            elif "idline " in msg.text:
                id = msg.text.replace("idline ", "")
                find = kr1.findContactsByUserId(id)
                for findid in find:
                    try:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': findid.mid}
                        kr1.sendMessage(msg)
                    except Exception as error:
                        print error
#==========================[Kris]===========================
            elif "Getgroup" in msg.text:
                group = kr1.getGroup(msg.to)
                path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                kr1.sendImageWithURL(msg.to, path)
#==========================[Kris]===========================
            elif "reinvite" in msg.text.split():
                if msg.toType == 2:
                    group = kr1.getGroup(msg.to)
                    if group.invitee is not None:
                        try:
                            grCans = [contact.mid for contact in group.invitee]
                            kr1.findAndAddContactByMid(msg.to, grCans)
                            kr1.cancelGroupInvitation(msg.to, grCans)
                            kr1.inviteIntoGroup(msg.to, grCans)
                        except Exception as error:
                            print error
                    else:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"No Invited")
                        else:
                            kr1.sendText(msg.to,"Error")
                else:
                    pass
#==========================[Kris]===========================
            elif "Kaluarti " in msg.text.split():
                    ng = msg.text.split().replace("Kaluarti ","")
                    gid = kr1.getGroupIdsJoined()
                    gid = kr2.getGroupIdsJoined()
                    gid = kr3.getGroupIdsJoined()
                    gid = kr4.getGroupIdsJoined()
                    gid = kr5.getGroupIdsJoined()
                    for i in gid:
                            h = kr1.getGroup(i).name
                            h = kr2.getGroup(i).name
                            h = kr3.getGroup(i).name
                            h = kr4.getGroup(i).name
                            h = kr5.getGroup(i).name
                    if h == ng:
                        kr1.sendText(i,"Bot di paksa keluar oleh owner..!,, MKSH :D..!!!")
                        kr5.leaveGroup(i)
                        kr4.leaveGroup(i)
                        kr3.leaveGroup(i)
                        kr2.leaveGroup(i)
                        kr1.leaveGroup(i)
                        kr1.sendText(msg.to,"Success left ["+ h +"] group")
                #else:
                #    kr1.sendText(msg.to,"Khusus Creator/Admin")
#==========================[Kris]===========================
            elif msg.text in ["LG"]:
                    gids = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                        #####gn = kr1.getGroup(i).name
                        h += "[•]%s Member\n" % (kr1.getGroup(i).name   +"👉"+str(len(kr1.getGroup(i).members)))
                        kr1.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))

            elif msg.text in ["LG2"]:
                    gid = kr1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (kr1.getGroup(i).name,i)
                        kr1.sendText(msg.to,h)
#==========================[Kris]===========================
            elif "Asupka: " in msg.text:
                    gid = msg.text.replace("Asupka: ","")
                    if gid == "":
                        kr1.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            kr1.findAndAddContactsByMid(msg.from_)
                            kr2.findAndAddContactsByMid(msg.from_)
                            kr3.findAndAddContactsByMid(msg.from_)
                            kr4.findAndAddContactsByMid(msg.from_)
                            kr5.findAndAddContactsByMid(msg.from_)
                            kr1.inviteIntoGroup(gid,[msg.from_])
                            kr2.inviteIntoGroup(gid,[msg.from_])
                            kr3.inviteIntoGroup(gid,[msg.from_])
                            kr4.inviteIntoGroup(gid,[msg.from_])
                            kr5.inviteIntoGroup(gid,[msg.from_])
                        except:
                            kr1.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#==========================[Kris]===========================
            elif "Getcontact " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                mmid = kr1.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
            elif msg.text.lower() == 'Bot':
                kr.sendImageWithURL(msg.to, url123)
                kr.sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
#==========================[Kris]===========================
            elif "youtube " in msg.text.lower():
                 query = msg.text.lower().replace("youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                             kr1.sendText(msg.to,'Judul : ' + a['title'] + '\nLink : ' + 'http://www.youtube.com' + a['href'])
#==========================[Kris]===========================
            elif "Vidio " in msg.text:
                try:
                    textToSearch = (msg.text).replace("Vidio ", "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
                    kr1.sendVideoWithURL(msg.to,ght)
                except:
                    kr1.sendText(msg.to,"Could not find it")
#==========================[Kris]===========================
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                kr1.sendText(msg.to,van)
#==========================[Kris]===========================
            elif msg.text in ["Restart"]:
                    kr1.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"
#==========================[Kris]===========================
            elif "Copy @" in msg.text:
                    if msg.toType == 2:
                            print "[COPY] Ok"
                            _name = msg.text.replace("Copy @","")
                            _nametarget = _name.rstrip('  ')
                            gs = kr1.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                kr1.sendText(msg.to, "Not Found...")
                            else:
                                for target in targets:
                                    try:
                                        kr1.cloneContactProfile(target)
                                        kr1.sendText(msg.to, "Succes Copy profile")
                                    except Exception as e:
                                        print e
#==========================[Kris]===========================
            elif "Getinfo @" in msg.text:
                nama = msg.text.replace("Getinfo @","")
                target = nama.rstrip(' ')
                van = kr1.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        mid = kr1.getContact(linedev.mid)
                        #./linedev/ervan
                        try:
                            cover = kr1.channel.getCover(linedev.mid)
                        except:
                            cover = ""
                        kr1.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + linedev.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass

            elif "Getinfo2 " in msg.text:
                mid = msg.text.replace("Getinfo2 ","")
                anu = kr1.getContact(mid)
                try:
                    cover = kr1.channel.getCover(mid)
                except:
                    cover = ""
                kr1.sendText(msg.to,"[Display Name]:\n" + anu.displayName + "\n[Mid]:\n" + mid + "\n[BIO]:\n" + anu.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + anu.pictureStatus + "\n[Cover]:\n" + str(cover))
#==========================[Kris]===========================
            elif msg.text in ["Gcreator"]:
                if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = kr1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    kr1.sendText(msg.to, "Group Creator : " + gCreator1)
                    kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text in ["Baca on","Read on"]:
                    wait["alwayRead"] = True
                    kr1.sendText(msg.to,"Auto read On")
                
            elif msg.text in ["Baca off","Read off"]:
                    wait["alwayRead"] = False
                    kr1.sendText(msg.to,"Auto read Off")
#==========================[Kris]===========================
            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Already on")
                    else:
                        kr1.sendText(msg.to,"Tag On")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Tag On")
                    else:
                        kr1.sendText(msg.to,"already on")
                        
            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Already off")
                    else:
                        kr1.sendText(msg.to,"Tag Off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Tag Off")
                    else:
                        kr1.sendText(msg.to,"Already off")
#==========================[Kris]===========================
            elif msg.text in ["Tag2 on"]:
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Already on")
                        else:
                            kr1.sendText(msg.to,"Tag On")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Tag On")
                        else:
                            kr1.sendText(msg.to,"already on")
                            
            elif msg.text in ["Tag2 off"]:
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Already off")
                        else:
                            kr1.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Tag Off")
                        else:
                            kr1.sendText(msg.to,"Already off")
#==========================[Kris]===========================
            elif msg.text in ["Auto on"]:
                    if wait["auto"] == True:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Bot join on")
                        else:
                            kr1.sendText(msg.to,"Bot join On")
                    else:
                        wait["auto"] = True
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Bot join On")
                        else:
                            kr1.sendText(msg.to,"Bot join On")
                            
            elif msg.text in ["Auto off"]:
                    if wait["auto"] == False:
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Bot join off")
                        else:
                            kr1.sendText(msg.to,"Bot join off")
                    else:
                        wait["auto"] = False
                        if wait["lang"] == "JP":
                            kr1.sendText(msg.to,"Bot join off")
                        else:
                            kr1.sendText(msg.to,"Bot join off")
#==========================[Kris]===========================
            elif "Tambah admin @" in msg.text:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Tambah admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    gs = kr2.getGroup(msg.to)
                    gs = kr3.getGroup(msg.to)
                    gs = kr4.getGroup(msg.to)
                    gs = kr5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                kr1.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                #else:
                #    kr1.sendText(msg.to,"Command Di Tolak Jangan Sedih")
                #    kr1.sendText(msg.to,"Sudah Menjadi Admin Maka Tidak Bisa Menjadi Admin Lagi")
#==========================[Kris]===========================
            elif "Hapus admin @" in msg.text:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Hapus admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    gs = kr2.getGroup(msg.to)
                    gs = kr3.getGroup(msg.to)
                    gs = kr4.getGroup(msg.to)
                    gs = kr5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                kr1.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                #else:
                #    kr1.sendText(msg.to,"Command DiTolak")
                #    kr1.sendText(msg.to,"Admin Tidak Bisa Menggunakan")
#==========================[Kris]===========================
            elif msg.text in ["Adminlist","admlist"]:
                if admin == []:
                    kr1.sendText(msg.to,"The adminlist is empty")
                else:
                    kr1.sendText(msg.to,"Sabar Dikit Mamang.....")
                    mc = ""
                    for mi_d in admin:
                        mc += "☄ " +kr1.getContact(mi_d).displayName + "\n"
                    kr1.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#==========================[Kris]===========================
            elif "Setimage " in msg.text:
                    wait["Pap"] = msg.text.replace("Setimage ","")
                    kr1.sendText(msg.to,"Image Has Ben Set To")

            elif msg.text in ["Papimage","/Papim"]:
                    kr1.sendImageWithURL(msg.to,wait["Pap"])
            elif "Setvideo " in msg.text:
                    wait["Vid"] = msg.text.replace("Setvideo ","")
                    kr1.sendText(msg.to,"Video Has Ben Set To")

            elif msg.text in ["Papvideo","/Papvid"]:
                    kr1.sendVideoWithURL(msg.to,wait["Vid"])
#==========================[Kris]===========================
            elif ("Ban " in msg.text):
              if msg.from_ in owner:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      kr1.sendText(msg.to,"Succes Banned")
                   except:
                      pass
#==========================[Kris]===========================
            elif "Kapan " in msg.text:
                tanya = msg.text.replace("Kapan ","")
                jawab = ("Besok","Tahun Depan","Minggu Depan","Satu Abad")
                jawaban = random.choice(jawab)
                kr1.sendText(msg.to,jawaban)
#==========================[Kris]===========================
            elif "Mycopy @" in msg.text:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        if msg.from_ in owner:
                            print "[COPY] Ok"
                            _name = msg.text.replace("Mycopy @","")
                            _nametarget = _name.rstrip('  ')
                            gs = kr1.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                kr1.sendText(msg.to, "Not Found...")
                            else:
                                for target in targets:
                                    try:
                                        kr1.CloneContactProfile(target)
                                        kr1.sendText(msg.to, "Succes Copy profile")
                                    except Exception as e:
                                        print e
#==========================[Kris]===========================
            elif msg.text in ["Mybackup"]:
                if msg.from_ in owner:
                    try:
                        kr1.updateDisplayPicture(backup.pictureStatus)
                        kr1.updateProfile(backup)
                        kr1.sendText(msg.to, "backup done")
                    except Exception as e:
                        kr1.sendText(msg.to, str (e))
#==========================[Kris]===========================
            elif msg.text in ["Time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%B')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                kr1.sendText(msg.to, rst)
                #client.sendText(msg.to, rst)
#==========================[Kris]===========================
            elif "image " in msg.text:
                search = msg.text.replace("image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    kr1.sendImageWithURL(msg.to,path)
                except:
                    pass
#==========================[Kris]===========================
            elif msg.text in ["cab","Cab"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab1","Cab1"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab2","Cab2"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
                kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab3","Cab3"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
                kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab4","Cab4"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
                kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab5","Cab5"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
                kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab6","Cab6"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                kr1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab7","Cab7"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                kr1.sendImageWithURL(msg.to, url)
#==========================[Kris]===========================
            elif msg.text in ["Team","Logo"]:
                if msg.from_ in owner:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    url2 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
                    url3 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
                    url4 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
                    url5 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    kr1.sendImageWithURL(msg.to, url)
                    kr1.sendImageWithURL(msg.to, url1)
                    kr1.sendImageWithURL(msg.to, url2)
                    kr1.sendImageWithURL(msg.to, url3)
                    kr1.sendImageWithURL(msg.to, url4)
                    kr1.sendImageWithURL(msg.to, url5)
                    kr1.sendImageWithURL(msg.to, url6)
                    kr1.sendImageWithURL(msg.to, url7)
#==========================[Kris]===========================
            elif msg.text in ["Kibar","kibar"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                kr1.sendImageWithURL(msg.to, url)
                kr1.sendImageWithURL(msg.to, url1)
                kr1.sendImageWithURL(msg.to, url6)
                kr1.sendImageWithURL(msg.to, url7)
#==========================[Kris]===========================
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    kr1.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    kr1.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	kr1.sendText(msg.to, str(njer))
#==========================[Kris]===========================
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-ja " in msg.text:
                nk0 = msg.text.replace("Tr-ja ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ja')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-en " in msg.text:
                nk0 = msg.text.replace("Tr-en ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'en')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-ms " in msg.text:
                nk0 = msg.text.replace("Tr-ms ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ms')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-it " in msg.text:
                nk0 = msg.text.replace("Tr-it ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'it')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-tr " in msg.text:
                nk0 = msg.text.replace("Tr-tr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'tr')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-my " in msg.text:
                nk0 = msg.text.replace("Tr-my ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'my')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-af " in msg.text:
                nk0 = msg.text.replace("Tr-af ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'af')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-sq " in msg.text:
                nk0 = msg.text.replace("Tr-sq ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'sq')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-am " in msg.text:
                nk0 = msg.text.replace("Tr-am ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'am')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-ar " in msg.text:
                nk0 = msg.text.replace("Tr-ar ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ar')
                kr1.sendText(msg.to,str(trans))
            elif "Tr-hy " in msg.text:
                nk0 = msg.text.replace("Tr-hy ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'hy')
                kr1.sendText(msg.to,str(trans))
#==========================[Kris]===========================
            elif "Cpp" in msg.text:
                    path = "syn.jpg"
                    kr1.sendText(msg.to,"Update PP :")
                    kr1.sendImage(msg.to,path)
                    kr1.updateProfilePicture(path)
#==========================[Kris]===========================
            elif "Steal @" in msg.text:
                    _name = msg.text.replace("Steal @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = kr1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                kr1.sendImageWithURL(msg.to, path)
                            except:
                                pass
#==========================[Kris]===========================
            elif "Steal " in msg.text:
                    salsa = msg.text.replace("Steal ","")
                    Manis = kr1.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = kr1.channel.getCover(Manis)
                    except:
                        cover = ""
                    kr1.sendText(msg.to,"Gambar Foto Profilenya")
                    kr1.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        kr1.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        kr1.sendText(msg.to,"Gambar Covernya")
                        kr1.sendImageWithURL(msg.to,cover)
#==========================[Kris]===========================
            elif "setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                kr1.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "viewseen" in msg.text:
                lurkGroup = ""
                dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = kr1.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        kr1.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        kr1.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#==========================[Kris]===========================
            elif ("Micadd " in msg.text):
                if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            kr1.sendText(msg.to,"Target ditambahkan!")
                            break
                        except:
                            kr1.sendText(msg.to,"Fail !")
                            break
                    
            elif ("Micdel " in msg.text):
                if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            kr1.sendText(msg.to,"Target dihapuskan!")
                            break
                        except:
                            kr1.sendText(msg.to,"Fail !")
                            break
                    
            elif msg.text in ["Miclist"]:
                if msg.from_ in owner:
                        if mimic["target"] == {}:
                            kr1.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+kr1.getContact(mi_d).displayName + "\n"
                            kr1.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                if msg.from_ in owner:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                kr1.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                kr1.sendText(msg.to,"Mimic change to target")
                            else:
                                kr1.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                if msg.from_ in owner:
                    cmd = msg.text.replace("Mimic ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            kr1.sendText(msg.to,"Reply Message on")
                        else:
                            kr1.sendText(msg.to,"Sudah on")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            kr1.sendText(msg.to,"Reply Message off")
                        else:
                            kr1.sendText(msg.to,"Sudah off")
#==========================[Kris]===========================
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                kr1.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kr1.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                kr1.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kr1.sendMessage(msg)
#==========================[Kris]===========================
            elif "botadd @" in msg.text:
                if msg.toType == 2:
                      print "[Command]Add executing"
                      _name = msg.text.replace("botadd @","")
                      _nametarget = _name.rstrip('  ')
                      gs = kr1.getGroup(msg.to)
                      gs = kr2.getGroup(msg.to)
                      gs = kr3.getGroup(msg.to)
                      gs = kr4.getGroup(msg.to)
                      targets = []
                      for g in gs.members:
                        if _nametarget == g.displayName:
                          targets.append(g.mid)
                      if targets == []:
                        kr1.sendText(msg.to,"Contact not found")
                      else:
                        for target in targets:
                          try:
                            kr1.findAndAddContactsByMid(target)
                            kr2.findAndAddContactsByMid(target)
                            kr3.findAndAddContactsByMid(target)
                            kr4.findAndAddContactsByMid(target)
                            kr1.senText(msg.to, "Berhasil Menambah Kan Teman")
                          except:
                            kr1.sendText(msg.to,"Error")
                #  else:
                #    kr1.sendText(msg.to,"Perintah Ditolak")
                #    kr1.sendText(msg.to,"Perintah ini Hanya Untuk Admin")
#==========================[Kris]===========================
            elif msg.text in ["Respon"]:
					kr1.sendText(msg.to,"Iya Mbebz...")
					kr1.sendText(msg.to,"Kenapa..??")
					kr1.sendText(msg.to,"Kangen kah...(^_^)")
            elif msg.text in ["Absen"]:
                    kr1.sendText(msg.to,"👉★★★")
                    kr2.sendText(msg.to,"👉★★★★")
                    kr3.sendText(msg.to,"👉★★★★★")
                    kr4.sendText(msg.to,"👉★★★★★★")
                    kr5.sendText(msg.to,"👉★★★★★★★")
                    kr1.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
#==========================[Kris]===========================
            elif "Getmid @" in msg.text:
                  _name = msg.text.replace("Getmid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = kr1.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          kr1.sendText(msg.to, g.mid)
                      else:
                          pass
#==========================[Kris]===========================
            elif msg.text in ["Kr kadieu","kr kadieu"]:
                    gid = kr1.getGroupIdsJoined()
                    gid = kr2.getGroupIdsJoined()
                    gid = kr3.getGroupIdsJoined()
                    gid = kr4.getGroupIdsJoined()
                    gid = kr5.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i,"Bye~Bye\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nuntuk konfirmasi => line://ti/p/~krissthea\nMakasih...!!!")
                        #kr1.sendImageWithURL(msg.to, url123)
                        kr1.leaveGroup(i)
                        kr2.leaveGroup(i)
                        kr3.leaveGroup(i)
                        kr4.leaveGroup(i)
                        kr5.leaveGroup(i)
                    if wait["lang"] == "JP":
                        kr1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        kr1.sendText(msg.to,"He declined all invitations")
#==========================[Kris]===========================
            elif "Bcgrup: " in msg.text:
                    bc = msg.text.replace("Bcgrup: ","")
                    gid = kr1.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i,"╠═════[BROADCAST]═════╣\n\n"+bc+"\n\nMAAF BROADCAST!!\n\n=>>line://ti/p/~krissthea\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")
                        kr1.sendText(msg.to, "Brodcastgrup sukses")
#==========================[Kris]===========================
            elif msg.text in ["Sp","sp"]:
					start = time.time()
					kr1.sendText(msg.to, "🐰🐰")
					kr1.sendText(msg.to, "🔥🔥🔥")
					kr1.sendText(msg.to, "💪💪💪💪")
					elapsed_time = time.time() - start
					kr1.sendText(msg.to, "%s/Detik" % (elapsed_time))
					
            elif msg.text in ["Speed","speed"]:
					start = time.time()
					kr.sendText(msg.to, "🐰🐰")
					kr.sendText(msg.to, "🔥🔥🔥")
					kr.sendText(msg.to, "💪💪💪💪")
					elapsed_time = time.time() - start
					kr.sendText(msg.to, "%s/Detik" % (elapsed_time))
	    elif msg.text.lower() == 'Bot':
                kr.sendImageWithURL(msg.to, url123)
                kr.sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
#==========================[Kris]===========================
            elif msg.text in ["Clearban"]:
                wait["blacklist"] = {}
                kr1.sendText(msg.to,"clear")
                
            elif msg.text in ["Ban"]:
					wait["wblacklist"] = True
					kr1.sendText(msg.to,"Kirim Kontak")
					
            elif msg.text in ["Unban"]:
					wait["dblacklist"] = True
					kr1.sendText(msg.to,"Kirim Kontak")
					
            elif msg.text in ["Banlist"]:
					if wait["blacklist"] == {}:
						kr1.sendText(msg.to,"Tidak Ada")
					else:
						kr1.sendText(msg.to,"Tunggu Sebentar Memuat Data")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "☄1�7 " +kr1.getContact(mi_d).displayName + "\n"
						kr1.sendText(msg.to,mc)
						
            elif msg.text in ["Cek ban"]:
					if msg.toType == 2:
						group = kr1.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						kr1.sendText(msg.to,cocoa + "")
						
            elif msg.text in ["Kill ban"]:
					if msg.toType == 2:
						group = kr1.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kr1.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							kr1.kickoutFromGroup(msg.to,[jj])
						kr1.sendText(msg.to,"Bye...")
#==========================[Kris]===========================
            elif "Batal" in msg.text:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							kr.cancelGroupInvitation(msg.to, gInviMids)
#==========================[Kris]===========================
            elif "Kr cium " in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            kr1.kickoutFromGroup(msg.to,[target])
                        except:
                            kr1.sendText(msg.to,"Error")
#==========================[Kris]===========================
            elif "Kr megs " in msg.text:
                    gName = msg.text.replace("Kr megs ","")
                    ap = kr1.getGroups([msg.to])
                    semua = [contact.mid for contact in ap[0].members]
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
            elif "#rmegs " in msg.text:
                    gName = msg.text.replace("#rmegs ","")
                    ap = kr1.getGroups([msg.to])
                    semua = findAndAddContactsByMid(Mi_d)
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        klis=[cl]
                        team=random.choice(klis)
                        kr1.findAndAddContactsByMid(Mi_d)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        kr1.createGroup(gName, semua)
                        team.findAndAddContactsByMid(Mi_d)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
            elif "Rrecover" in msg.text:
                    thisgroup = kr1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr1.createGroup("Rrecover", mi_d)
                    kr1.sendText(msg.to,"Success recover")
            elif "Kr spin" in msg.text:
                    thisgroup = kr1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.createGroup("Nah kan", mi_d)
                    kr1.sendText(msg.to,"Success...!!!!")
#==========================[Kris]===========================
            elif msg.text in ["Remove all chat"]:
                    kr1.removeAllMessages(op.param2)
                    kr2.removeAllMessages(op.param2)
                    kr3.removeAllMessages(op.param2)
                    kr4.removeAllMessages(op.param2)
                    kr5.removeAllMessages(op.param2)
                    kr1.sendText(msg.to,"Removed all chat Finish")
#==========================[Kris]===========================
            elif msg.text in ["Kr muach"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr1.sendMessage(msg)
                    
            elif msg.text in ["Muach"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr.sendMessage(msg)
#==========================[Kris]===========================
            elif "Kr spamtag @" in msg.text:
                    _name = msg.text.replace("Kr spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                            kr1.sendMessage(msg)
                        else:
                            pass
                        
            elif "Spamtag @" in msg.text:
                    _name = msg.text.replace("Spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                        else:
                            pass
#==========================[Kris]===========================
            elif "Kr spamkontak @" in msg.text:
                    _name = msg.text.replace("Kr spamkontak @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            kr1.sendText(msg.to, "║╠❂➣ Spam sedang di Proses...!!!")
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(g.mid,'spam')
                            kr1.sendText(msg.to, "║╠❂➣ Done.. Selesai di Spam...!!!")
                            print " Spammed !"
                            
            elif "Spamkontak @" in msg.text:
                    _name = msg.text.replace("Spamkontak @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            kr.sendText(msg.to, "║╠❂➣ Spam sedang di Proses...!!!")
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(msg.to, "║╠❂➣ Done.. Selesai di Spam...!!!")
                            print " Spammed !"
#==========================[Kris]===========================

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in kr.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait['likeOn'] == True:
                   kr.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          kr.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = kr.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          kr.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kr.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n���º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««")
          print "Like"
        except:
          pass
      else:
          print "Already Liked Om"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = kr.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    kr.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kr.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Om"


while True:
    try:
        Ops = kr.fetchOps(kr.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kr.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kr.Poll.rev = max(kr.Poll.rev, Op.revision)
            bot(Op)
