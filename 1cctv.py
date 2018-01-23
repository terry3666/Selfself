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
kr.login(token='')#cctv 
kr.loginResult()

kr1 = kr2 = kr3 = kr4 = kr5 = kr

print "╔═════════════════════════╗\n║╔═══════════════════════╗║\n║╠❂➣KRIS BERHASIL LOGIN ║║\n║╚═══════════════════════╝║\n╚═════════════════════════╝"
reload(sys)
sys.setdefaultencoding('utf-8')


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
║╠❂➣Cctv
║╠❂➣Toong
║╠❂➣cctv on/off
║╠❂➣Check
║╠❂➣Sider
║╠❂➣Intip
║╠❂➣Setview
║╠❂➣Viewseen
║╠❂➣Intip on/off
║╚════════════
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
"""

KAC=[kr,kr1,kr2,kr3,kr4,kr5]
AST=[kr1,kr2,kr3,kr4,kr5]
mid1 = kr.getProfile().mid
Amid = kr1.getProfile().mid
Bmid = kr2.getProfile().mid
Cmid = kr3.getProfile().mid
Dmid = kr4.getProfile().mid
Emid = kr5.getProfile().mid

Bots=[mid1,Amid,Bmid,Cmid,Dmid,Emid]
induk=[mid1]
asist=[Amid,Bmid,Cmid,Dmid,Emid]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1","ud55745480bb2c5665e6a21df2a68155e","u6908b4803bf3e267cf659ddda91d5fa4","u60335d94c7a3ca3a3c3685f515724145","uc92d7e39d7259174dba7d8028c7ef4b2","uc1ba312554b4ee025039f54ff44c7c7f","uc70b2f7f85d13c96e0f28ded3b3b13d6","u9d4b18194ce5b48d86fa27e5fac1d606","ud3065a5bd9cf0d6961d9c046a124761c",mid1,Amid]#kr/kris/6botProtect/media/agatha/hajir
owner=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
wait = {
    "contact":False,
    "autoJoin":True,
    "autoCancel":{"on":True,"members":1},
    "leaveRoom":False,
    "timeline":False,
    "autoAdd":False,
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
    "auto":False,
    "tag":False,
    "tag2":False,
    "likeOn":False,
    "winvite":False,
    'invite':{},
    "Wc":False,
    "Wc2":False,
    "Lv":False,
    "Sider":{},
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

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
    }


setTime = {}
setTime = wait2['setTime']

contact = kr.getProfile()
mybackup = kr.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
backup = kr.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
profile = kr.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

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


def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)


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

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in cctv['point']:
            Name = kr.getContact(op.param2).displayName
            if Name in cctv['sidermem'][op.param1]:
                pass
            else:
                cctv['sidermem'][op.param1] += "\n• " + Name
                cctv['cyduk'][op.param1][op.param2] = "\n• " + Name
        else:
            pass
    except:
        pass

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    print nm
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
    print msg
    try:
         kr.sendMessage(msg)
    except Exception as error:
        print error

def removeAllMessages(self, lastMessageId):
     return self._kr.removeAllMessages(0, lastMessageId)

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
url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False


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
                    kr.sendText(msg.to,jawaban)
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
                                  kr.sendImageWithURL(msg.to,ret_)
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
                    kr.sendText(msg.to,jawaban)
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
                kr.sendMessage(gm)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc2"] == True:
                if op.param2 in Bots:
                    return
                G = kr.getGroup(op.param1)
                h = kr.getContact(op.param2)
                kr.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                kr.sendText(op.param1, "╔═════════════" + "\n║" + kr.getContact(op.param2).displayName  +  "\n╠═════════════\n║Nah Baper Dia :v \n╠═════════════\n║Belum di Anu Kayanya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#==========================[Kris]===========================
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
                                        kr.sendText(op.param1,"please do not change group name-_-")
#==========================[Kris]===========================
        if op.type == 13:
            print op.param3
            if op.param3 in mid1:
                if op.param2 in owner or Bots or admin:
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
            if op.param3 in mid1:
                if op.param2 in Amid:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Bmid:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Cmid:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Dmid:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Emid:
                    kr.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Amid:
                if op.param2 in mid1:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Bmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Cmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Dmid:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Emid:
                    kr1.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Bmid:
                if op.param2 in mid1:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Amid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Dmid:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Emid:
                    kr2.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Cmid:
                if op.param2 in mid1:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Amid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Emid:
                    kr3.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Dmid:
                if op.param2 in mid1:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Amid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Bmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    kr4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Emid:
                    kr4.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
            if op.param3 in Emid:
                if op.param2 in mid1:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Amid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Bmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Cmid:
                    kr5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    kr5.acceptGroupInvitation(op.param1)
#==========================[Kris]===========================
        if op.type == 13:
            if mid1 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots or admin or owner:
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
                    
            if op.param3 in admin:
                if op.param2 in admin:
                    random.choice(AST).inviteIntoGroup(op.param1,admin)
                    random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
                    
#            if op.param3 in induk:
#                if op.param2 not in Bots:
#                    midd = (mid1)
#                    random.choice(AST).findAndAddContactsByMid(midd)
#                    random.choice(AST).inviteIntoGroup(op.param1,[midd])
#                    kr.acceptGroupInvitation(op.param1)
#                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#==========================[Kris]===========================
#        if op.type == 19:
#            if wait["autoKick"] == True:
#                if op.param2 in admin or Bots:
#                    pass
#                else:
#                    try:
#                        kr1.kickoutFromGroup(op.param1,[op.param2])
#                        kr1.inviteIntoGroup(op.param1,[op.param3])
#                    except:
#                        try:
#                            random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#                            random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
#                        except:
#                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
#                if op.param2 in wait["blacklist"]:
#                    pass
#                else:
#                    if op.param2 in admin or Bots:
#                        pass
#                    else:
#                        wait["blacklist"][op.param2] = True
#                if op.param2 in wait["blacklist"]:
#                    pass
#                else:
#                    if op.param2 in admin or Bots:
#                        pass
#                    else:
#                        wait["blacklist"][op.param2] = True
#==========================[Kris]===========================
#                if mid1 in op.param3:
#                    if op.param2 in Bots or admin:
#                        pass
#                    else:
#                        try:
#                            kr1.kickoutFromGroup(op.param1,[op.param2])
#                            kr2.kickoutFromGroup(op.param1,[op.param2])
#                        except:
#                            try:
#                                random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#                            except:
#                                print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
#                            if op.param2 in wait["blacklist"]:
#                                pass
#                            else:
#                                if op.param2 in Bots:
#                                    pass
#                                else:
#                                    wait["blacklist"][op.param2] = True
#                                    G = kr1.getGroup(op.param1)
#                                    G.preventJoinByTicket = False
#                                    kr1.updateGroup(G)
#                                    Ti = kr1.reissueGroupTicket(op.param1)
#                                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    kr1.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    kr2.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    kr3.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    kr4.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    kr5.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    X = kr.getGroup(op.param1)
#                                    X.preventJoinByTicket = True
#                                    kr.updateGroup(X)
#                                    if op.param2 in wait["blacklist"]:
#                                        pass
#                                    else:
#                                        if op.param2 in Bots:
#                                            pass
#                                        else:
#                                            wait["blacklist"][op.param2] = True
#

#==========================[Kris]===========================
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = kr1.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             kr1.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 kr1.findAndAddContactsByMid(target)
                                 kr1.inviteIntoGroup(msg.to,[target])
                                 kr1.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      kr1.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                    if msg.from_ in admin or owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = kr1.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                kr1.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                kr1.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                kr1.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    kr1.findAndAddContactsByMid(target)
                                    kr1.inviteIntoGroup(msg.to,[target])
                                    kr1.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        kr1.findAndAddContactsByMid(invite)
                                        kr1.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        kr1.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break

                    if msg.from_ in admin or owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = kr2.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                kr2.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                kr2.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                kr2.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    kr2.findAndAddContactsByMid(target)
                                    kr2.inviteIntoGroup(msg.to,[target])
                                    kr2.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        kr2.findAndAddContactsByMid(invite)
                                        kr2.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        kr2.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break
#==========================[Kris]===========================
        if op.type == 26:
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
        if op.type == 26:
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
        if op.type == 26:
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
                        kr.sendText(msg.to,"deleted")
                        kr2.sendText(msg.to,"deleted")
                        kr3.sendText(msg.to,"deleted")
                        kr4.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        kr.sendText(msg.to,"It is not in the black list")
                        kr2.sendText(msg.to,"It is not in the black list")
                        kr3.sendText(msg.to,"It is not in the black list")
                        kr4.sendText(msg.to,"It is not in the black list")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        kr.sendText(msg.to,"already")
                        kr2.sendText(msg.to,"already")
                        kr3.sendText(msg.to,"already")
                        kr4.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        kr.sendText(msg.to,"aded")
                        kr2.sendText(msg.to,"aded")
                        kr3.sendText(msg.to,"aded")
                        kr4.sendText(msg.to,"aded")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        kr.sendText(msg.to,"deleted")
                        kr2.sendText(msg.to,"deleted")
                        kr3.sendText(msg.to,"deleted")
                        kr4.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        kr.sendText(msg.to,"It is not in the black list")
                        kr2.sendText(msg.to,"It is not in the black list")
                        kr3.sendText(msg.to,"It is not in the black list")
                        kr4.sendText(msg.to,"It is not in the black list")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    kr.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�10��9�0�16�0�69�0�3�0�4\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)
#==========================[Kris]===========================
            elif msg.text is None:
                return
            elif msg.text in ["help","Help"]:
                if msg.from_ in admin:
					if wait["lang"] == "JP":
						kr.sendText(msg.to,helpMessage)
						random.choice(AST).sendImageWithURL(msg.to, url123)
						random.choice(AST).sendText(msg.to,"↥↥↥↥↥↪ Owner Bots ↩↥↥↥↥↥")
					else:
						random.choice(AST).sendText(msg.to,helpMessage)
#==========================[Kris]===========================
            elif msg.text in ["Key1","key1"]:
                if msg.from_ in admin:
					if wait["lang"] == "JP":
						kr.sendText(msg.to,key1Message)
					else:
						random.choice(AST).sendText(msg.to,key1Message)
#==========================[Kris]===========================
            elif ("Gn " in msg.text):
                if msg.from_ in admin:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						kr.updateGroup(X)
					else:
						kr.sendText(msg.to,"It can't be used besides the group.")
            elif ("Kr1 gn " in msg.text):
                if msg.from_ in admin:
					if msg.toType == 2:
						X = kr1.getGroup(msg.to)
						X.name = msg.text.replace("Kr1 gn ","")
						kr1.updateGroup(X)
					else:
						kr.sendText(msg.to,"It can't be used besides the group.")
            elif ("Kr2 gn " in msg.text):
                if msg.from_ in admin:
					if msg.toType == 2:
						X = kr2.getGroup(msg.to)
						X.name = msg.text.replace("Kr2 gn ","")
						kr2.updateGroup(X)
					else:
						kr2.sendText(msg.to,"It can't be used besides the group.")
            elif ("Kr3 gn " in msg.text):
                if msg.from_ in admin:
					if msg.toType == 2:
						X = kr3.getGroup(msg.to)
						X.name = msg.text.replace("Kr3 gn ","")
						kr3.updateGroup(X)
					else:
						kr3.sendText(msg.to,"It can't be used besides the group.")
#==========================[Kris]===========================
            elif "Kick " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					kr.kickoutFromGroup(msg.to,[midd])
            elif "Kr1 kick " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("Kr1 kick ","")
					kr1.kickoutFromGroup(msg.to,[midd])
            elif "Kr2 kick " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("Kr2 kick ","")
					kr2.kickoutFromGroup(msg.to,[midd])
            elif "Kr3 kick " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("Kr3 kick ","")
					kr3.kickoutFromGroup(msg.to,[midd])
#==========================[Kris]===========================
            elif "Invite " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					kr.findAndAddContactsByMid(midd)
					kr.inviteIntoGroup(msg.to,[midd])
            elif "Kr1 invite " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("Kr1 invite ","")
					kr1.findAndAddContactsByMid(midd)
					kr1.inviteIntoGroup(msg.to,[midd])
            elif "Kr2 invite " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("Kr2 invite ","")
					kr2.findAndAddContactsByMid(midd)
					kr2.inviteIntoGroup(msg.to,[midd])
            elif "Kr3 invite " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("Kr3 invite ","")
					kr3.findAndAddContactsByMid(midd)
					kr3.inviteIntoGroup(msg.to,[midd])
#==========================[Kris]===========================
            elif msg.text in ["Me","me"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': msg.from_}
                    kr.sendMessage(msg)
            elif msg.text in ["Kr1","kr1"]:
                if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					kr1.sendMessage(msg)
            elif msg.text in ["Kr2","kr2"]:
                if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kr2.sendMessage(msg)
            elif msg.text in ["Kr3","kr3"]:
                if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Cmid}
					kr3.sendMessage(msg)
            elif msg.text in ["Kr4","kr4"]:
                if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Dmid}
					kr4.sendMessage(msg)
            elif msg.text in ["Kr5","kr5"]:
                if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Emid}
					kr5.sendMessage(msg)
            elif msg.text.lower() == 'Bot':
                kr.sendImageWithURL(msg.to, url123)
                kr.sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
#==========================[Kris]===========================
            elif msg.text in ["cancel","Cancel"]:
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                        
            elif msg.text == "Cctv ginfo":
                if msg.from_ in admin:
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
                if msg.from_ in admin:
					kr.sendText(msg.to,mid1)
					kr1.sendText(msg.to,Amid)
					kr2.sendText(msg.to,Bmid)
					kr3.sendText(msg.to,Cmid)
					kr4.sendText(msg.to,Dmid)
					kr5.sendText(msg.to,Emid)
            elif "Mid" == msg.text:
                if msg.from_ in admin:
					kr.sendText(msg.to,mid1)
            elif "Kr1 mid" == msg.text:
                if msg.from_ in admin:
					kr1.sendText(msg.to,Amid)
            elif "Kr2 mid" == msg.text:
                if msg.from_ in admin:
					kr2.sendText(msg.to,Bmid)
            elif "Kr3 mid" == msg.text:
                if msg.from_ in admin:
					kr3.sendText(msg.to,Cmid)
            elif "Kr4 mid" == msg.text:
                if msg.from_ in admin:
					kr4.sendText(msg.to,Cmid)
            elif "Kr5 mid" == msg.text:
                if msg.from_ in admin:
					kr5.sendText(msg.to,Cmid)
#==========================[Kris]===========================
            elif msg.text in ["Undang","undang"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    kr.sendText(msg.to,"send contact")
            elif msg.text in ["Jepit","jepit"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    kr1.sendText(msg.to,"send contact")
            elif msg.text in ["Tarik","tarik"]:
                if msg.from_ in admin:
                    wait['invite'] = True
                    kr2.sendText(msg.to,"send contact")
#==========================[Kris]===========================
            elif "Rename " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Rename ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr.getProfile()
                        profile.displayName = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Changed " + string + "")
#==========================[Kris]===========================
            elif "Rename1 " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Rename1 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr1.getProfile()
                        profile.displayName = string
                        kr1.updateProfile(profile)
                        kr1.sendText(msg.to,"Changed " + string + "")
            elif "Rename2 " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Rename2 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr2.getProfile()
                        profile.displayName = string
                        kr2.updateProfile(profile)
                        kr2.sendText(msg.to,"Changed " + string + "")
            elif "Rename3 " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Rename3 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr3.getProfile()
                        profile.displayName = string
                        kr3.updateProfile(profile)
                        kr3.sendText(msg.to,"Changed " + string + "")
            elif "Rename4 " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Rename4 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr4.getProfile()
                        profile.displayName = string
                        kr4.updateProfile(profile)
                        kr4.sendText(msg.to,"Changed " + string + "")
            elif "Rename5 " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Rename5 ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr5.getProfile()
                        profile.displayName = string
                        kr5.updateProfile(profile)
                        kr5.sendText(msg.to,"Changed " + string + "")
#==========================[Kris]===========================
            elif "Allrename " in msg.text:
                if msg.from_ in owner:
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
                if msg.from_ in owner:
                    string = msg.text.replace("Bio ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = kr.getProfile()
                        profile.statusMessage = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Changed " + string)
            elif msg.text.lower() == 'Bot':
                kr.sendImageWithURL(msg.to, url123)
                kr.sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
#==========================[Kris]===========================
            elif "Allbio " in msg.text:
                if msg.from_ in owner:
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
            elif msg.text in ["Guest on","guest on"]:
                if msg.from_ in admin:
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Guest Stranger On")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Guest Stranger On")
                        else:
                            kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Guest off","guest off"]:
                if msg.from_ in admin:
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Guest Stranger Off")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Guest Stranger Off")
                        else:
                            kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Kontak on","kontak on"]:
                if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Kontak off","kontak off"]:
                if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Join on","join on"]:
                if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Join off","join off"]:
                if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Gcancel "]:
                if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel ","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								kr.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								kr.sendText(msg.to,"Done")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								kr.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								kr.sendText(msg.to,strnum + "Done")
					except:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Value is wrong")
						else:
							kr.sendText(msg.to,"Bizarre ratings")
#==========================[Kris]===========================
            elif msg.text in ["Leave on","leave on"]:
                if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Already on")
#==========================[Kris]===========================
            elif msg.text in ["Leave off","leave off"]:
                if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"already off")
#==========================[Kris]===========================
            elif msg.text in ["Share on","share on"]:
                if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Already on")
#==========================[Kris]===========================
            elif msg.text in ["Share off","share off"]:
                if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Already off")
#==========================[Kris]===========================
            elif msg.text in ["Status","status"]:
                if msg.from_ in admin:
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

#==========================[Kris]===========================
            elif msg.text in ["Tolak","tolak"]:
                if msg.from_ in admin:
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
						kr.sendText(msg.to,"All invitations have been refused")
					else:
						kr.sendText(msg.to,"All invitations have been refused")
#==========================[Kris]===========================
            elif msg.text in ["Add on","add on"]:
                if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Add already on")
						else:
							kr.sendText(msg.to,"Add done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Add done")
						else:
							kr.sendText(msg.to,"Add Already on")
#==========================[Kris]===========================
            elif msg.text in ["Add off","add off"]:
                if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Add already off")
						else:
							kr.sendText(msg.to,"Add done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Add done")
						else:
							kr.sendText(msg.to,"Add Already off")
#==========================[Kris]===========================
            elif "Message change " in msg.text:
                if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change ","")
					kr.sendText(msg.to,"message changed")
					
            elif "Message add " in msg.text:
                if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add ","")
					if wait["lang"] == "JP":
						kr.sendText(msg.to,"message changed")
					else:
						kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Pesan","pesan"]:
                if msg.from_ in admin:
					if wait["lang"] == "JP":
						kr.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						kr.sendText(msg.to,"The automatic appending information is set as follows\n\n" + wait["message"])
#==========================[Kris]===========================
            elif "Comment " in msg.text:
                if msg.from_ in admin:
					c = msg.text.replace("Comment ","")
					if c in [""," ","\n",None]:
						kr.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						kr.sendText(msg.to,"changed\n\n" + c)
#==========================[Kris]===========================
            elif "Add comment " in msg.text:
                if msg.from_ in admin:
					c = msg.text.replace("Add comment ","")
					if c in [""," ","\n",None]:
						kr.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						kr.sendText(msg.to,"changed\n\n" + c)
#==========================[Kris]===========================
            elif msg.text in ["Comment on","comment on"]:
                if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Alredy on")
#==========================[Kris]===========================
            elif msg.text in ["Comment off","comment off"]:
                if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Already off")
#==========================[Kris]===========================
            elif msg.text in ["Gurl"]:
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
					wait["wblack"] = True
					kr.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                if msg.from_ in admin:
					wait["dblack"] = True
					kr.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Confirm","confirm"]:
                if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						kr.sendText(msg.to,"confirmed")
					else:
						kr.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +kr1.getContact(mi_d).displayName + "\n"
						kr.sendText(msg.to,mc)
#==========================[Kris]===========================
            elif msg.text in ["Jam on"]:
                if msg.from_ in admin:
					if wait["clock"] == True:
						kr.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = kr.getProfile()
						profile.displayName = wait["cName"] + nowT
						kr.updateProfile(profile)
						kr.sendText(msg.to,"done")
						
            elif msg.text in ["Jam off"]:
                if msg.from_ in admin:
					if wait["clock"] == False:
						kr.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						kr.sendText(msg.to,"done")
						
            elif msg.text in ["Change clock "]:
                if msg.from_ in admin:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						kr.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						kr.sendText(msg.to,"changed to\n\n" + n)
						
            elif msg.text in ["Up"]:
                if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = kr.getProfile()
						profile.displayName = wait["cName"] + nowT
						kr.updateProfile(profile)
						kr.sendText(msg.to,"Updated")
					else:
						kr.sendText(msg.to,"Please turn on the name clock")
#==========================[Kris]===========================
            elif msg.text in ["Cctv","cctv"]:
                if msg.from_ in admin:
                    kr.sendText(msg.to, "Check sider"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
                    
            elif msg.text in ["Toong","toong"]:
                if msg.from_ in admin:
                        if msg.to in wait2['readPoint']:
                            if wait2['ROM'][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2['ROM'][msg.to].items():
                                    print rom
                                    chiya += rom[1] + "\n"
                            kr.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal \n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        else:
                            kr.sendText(msg.to, "An already read point has not been set.\n¡¸Cctv¡¹you can send  read point will be created ")

#==========================[Kris]===========================
            elif msg.text.lower() == 'cctv on':
                if msg.from_ in admin:
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
                            with open('intip.json', 'w') as fp:
                             json.dump(wait2, fp, sort_keys=True, indent=4)
                             kr.sendText(msg.to,"Cctv sudah menyala silahkan masukan command [Check]")
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
                        with open('intip.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         kr.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                         print wait2

            elif msg.text.lower() == 'cctv off':
                if msg.from_ in admin:
                    if msg.to not in wait2['readPoint']:
                        kr.sendText(msg.to,"Set Reading point tidak di temukan")
                        kr.sendText(msg.to,"Silahkan masukan Command [Cctv on] untuk set point")
                    else:
                        try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                        except:
                              pass
                        kr.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                    
            elif msg.text.lower() == 'check':
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             kr.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = kr.getContacts(chiya)
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
                          kr.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        kr.sendText(msg.to, "cctv has not been set.")
#==========================[Kris]===========================
            elif msg.text == "Sider":
                if msg.from_ in admin:
                    kr.sendText(msg.to, "Lurking Is Starting!! "+ datetime.today().strftime('%H:%M:%S'))
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

            elif msg.text in ["Intip","intip"]:
                if msg.from_ in admin:
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
                            kr.sendText(msg.to, "╔═════════════\n║Sider :\n╠═════════════\n║%s\n╠═════════════\n║Reader :\n╠═════════════\n║%s\n╠═════════════\n║In the last seen point:\n║[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
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
                            kr.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                        else:
                            kr.sendText(msg.to, "Ketik => [Cctv] untuk cek sider ketik => [Intip]")
#==========================[Kris]===========================

            elif msg.text in ["Cctv bye","cctv bye"]:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = kr.getGroup(msg.to)
                        ginfo = kr1.getGroup(msg.to)
                        ginfo = kr2.getGroup(msg.to)
                        ginfo = kr3.getGroup(msg.to)
                        ginfo = kr4.getGroup(msg.to)
                        ginfo = kr5.getGroup(msg.to)
                        try:
                            kr.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            kr5.leaveGroup(msg.to)
                            kr4.leaveGroup(msg.to)
                            kr3.leaveGroup(msg.to)
                            kr2.leaveGroup(msg.to)
                            kr1.leaveGroup(msg.to)
                        except:
                            pass
                        
            elif msg.text in ["x","X"]:
                if msg.from_ in owner:
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
                            #kr.leaveGroup(msg.to)
                        except:
                            pass
#==========================[Kris]===========================
            elif msg.text in ["Glist","glist"]:
                if msg.from_ in owner:
                    gid = kr.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "☄ %s  \n" % (kr.getGroup(i).name + " 👥 ▄ [ " + str(len (kr.getGroup(i).members))+" ]")
                    kr.sendText(msg.to, "     ☄ [ ♡List Grup♄ ] ☜\n"+ h +"Total Group ▄" +"[ "+str(len(gid))+" ]")
#==========================[Kris]===========================
            elif msg.text in ["Dadas","dadas"]:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Dadas","")
                        gs = kr.getGroup(msg.to)
                        gs = kr1.getGroup(msg.to)
                        gs = kr2.getGroup(msg.to)
                        gs = kr3.getGroup(msg.to)
                        gs = kr4.getGroup(msg.to)
                        gs = kr5.getGroup(msg.to)
                        kr.sendText(msg.to,"Perintah DiLaksanakan Maaf Kan Ya :v Ã´")
                        targets = []
                        for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
                        if targets == []:
							kr.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                if target not in Bots:
                                    try:
                                        klist=[kr1,kr2,kr3,kr4,kr5]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        kr.sendText(msg.to,"Group Dibersihkan")
#==========================[Kris]===========================
            elif msg.text in ["Salam1"]:
                kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif msg.text in ["Salam3"]:
                if msg.from_ in owner:
                    kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                    kr.sendText(msg.to,"Assalamu'alaikum")
                    kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                    kr.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Salam3","")
                        gs = kr.getGroup(msg.to)
                        gs = kr1.getGroup(msg.to)
                        gs = kr2.getGroup(msg.to)
                        gs = kr3.getGroup(msg.to)
                        gs = kr4.getGroup(msg.to)
                        gs = kr5.getGroup(msg.to)
                        kr.sendText(msg.to,"maaf kalo gak sopan")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            kr.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                if target not in Bots:
                                    try:
                                        klist=[kr1,kr2,kr3,kr4,kr5]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                        kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                        kr.sendText(msg.to,"Nah salamnya jawab sendiri dah")
#==========================[Kris]===========================
            elif "Kiss " in msg.text:
                if msg.from_ in admin:
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

            elif "Cium " in msg.text:
                if msg.from_ in admin:
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
                  
            elif "zzz " in msg.text:
                if msg.from_ in admin:
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
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr1.sendMessage(msg)
                    kr1.sendMessage(msg)
                    kr2.sendMessage(msg)
                    kr2.sendMessage(msg)
                    
            elif msg.text.lower() == 'ah':
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr.sendMessage(msg)
                    kr.sendMessage(msg)
                    kr.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text in ["Mode on","mode on"]:
                if msg.from_ in admin:
                    if wait["QrProtect"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect QR On")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect QR On")
                        else:
                            kr.sendText(msg.to,"done")
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Member Protection On")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Member Protection On")
                        else:
                            kr.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        kr.sendText(msg.to,"TURN ON")
                    else:
                        kr.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = kr.getGroup(msg.to).name
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already on")
                        else:
                            kr.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag On")
                        else:
                            kr.sendText(msg.to,"already on")
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Yang ngeTag Kick on")
                        else:
                            kr.sendText(msg.to,"Yang ngeTag Kick on")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Yang ngeTag Kick on")
                        else:
                            kr.sendText(msg.to,"Yang ngeTag Kick on")
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Guest Stranger On")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Guest Stranger On")
                        else:
                            kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Mode off","mode off"]:
                if msg.from_ in admin:
                    if wait["QrProtect"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect QR Off")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect QR Off")
                        else:
                            kr.sendText(msg.to,"done")
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Member Protection Off")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Member Protection Off")
                        else:
                            kr.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        kr.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        kr.sendText(msg.to,"ALREADY OFF")
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect already oғғ")
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Nayapa yg gabung already oғғ")
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Nayapa yg left already oғғ")
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Kick already oғғ")
                    if wait["tag"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already Tag off")
                        else:
                            kr.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag Off")
                        else:
                            kr.sendText(msg.to,"Already Tag off")
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Yang ngeTag Kick off")
                        else:
                            kr.sendText(msg.to,"Yang ngeTag Kick off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Yang ngeTag Kick off")
                        else:
                            kr.sendText(msg.to,"Yang ngeTag Kick off")
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Guest Stranger Off")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Guest Stranger Off")
                        else:
                            kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Intip on","intip on"]:
                if msg.from_ in admin:
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True
                    wait["Sider"] == True
                    kr.sendText(msg.to,"Cek yang ngintip on..!!!")
                
            elif msg.text in ["Intip off","intip off"]:
                if msg.from_ in admin:
                    if msg.to in cctv['point']:
                        cctv['cyduk'][msg.to]=False
                        wait["Sider"] = False
                        kr.sendText(msg.to,"Cek yang ngintip off")
                    else:
                        kr.sendText(msg.to,"Belum Di Set Boss")
                        
#==========================[Kris]===========================
            elif msg.text in ["Qr on","qr on"]:
                if msg.from_ in admin:
                    if wait["QrProtect"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect QR On")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect QR On")
                        else:
                            kr.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
                if msg.from_ in admin:
                    if wait["QrProtect"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect QR Off")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Protect QR Off")
                        else:
                            kr.sendText(msg.to,"done")
#==========================[Kris]===========================
            elif msg.text in ["Member on","member on"]:
                if msg.from_ in admin:
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Member Protection On")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Member Protection On")
                        else:
                            kr.sendText(msg.to,"done")
            elif msg.text in ["Member off","member off"]:
                if msg.from_ in admin:
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Member Protection Off")
                        else:
                            kr.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Member Protection Off")
                        else:
                            kr.sendText(msg.to,"done")
            elif msg.text in ["Respoto on","respoto on"]:
                if msg.from_ in admin:
                    wait["detectMention"] = True
                    kr.sendText(msg.to,"Auto respon tag Pict On")
                
            elif msg.text in ["Respoto off","respoto off"]:
                if msg.from_ in admin:
                    wait["detectMention"] = False
                    kr.sendText(msg.to,"Auto respon tag Pict Off")
#==========================[Kris]===========================
            elif msg.text in ["Creator","creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
					kr.sendMessage(msg)
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u9cc2323f5b84f9df880c33aa9f9e3ae1"}
					kr.sendMessage(msg)
					url = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")
					kr.sendImageWithURL(msg.to, url)
					kr.sendText(msg.to,"MyCreator\nyang bikin Bot ini...!!!")
#==========================[Kris]===========================
            elif msg.text in ["Invite creator"]:
                if msg.from_ in admin:
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
                if msg.from_ in admin:
                    ginfo = kr1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        kr1.findAndAddContactsByMid(gCreator)
                        kr1.kickoutFromGroup(msg.to,[gCreator])
                        print "success inv gCreator"
                    except:
                        pass
#==========================[Kris]===========================
            elif "Gbc " in msg.text:
                if msg.from_ in owner:
                    bctxt = msg.text.replace("Gbc ", "")
                    n = kr.getGroupIdsJoined()
                    for manusia in n:
                        kr.sendText(manusia, (bctxt) + "\n╠═════[BROADCAST]═════╣\n\n=>>line://ti/p/~krissthea\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")
            elif "Pm cast " in msg.text:
                if msg.from_ in owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = kr.getAllContactIds()
					for manusia in t:
						kr.sendText(manusia,(bctxt))
            elif "Fbc " in msg.text:
                if msg.from_ in owner:
                    bctxt = msg.text.replace("Fbc ", "")
                    t = kr.getAllContactIds()
                    for manusia in t:
                        kr.sendText(manusia, (bctxt))
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

            elif msg.text in ["Group on","grup on","Grup on"]:
                if msg.from_ in admin:
                    if msg.to in wait['pname']:
                        kr.sendText(msg.to,"TURN ON")
                    else:
                        kr.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = kr.getGroup(msg.to).name
                        
            elif msg.text in ["Group off","Grup off","grup off"]:
                if msg.from_ in admin:
                    if msg.to in wait['pname']:
                        kr.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        kr.sendText(msg.to,"ALREADY OFF")
#==========================[Kris]===========================
            elif msg.text in ["Turn off","turn off"]:
                if msg.from_ in owner:
                    try:
                        import sys
                        sys.exit()
                        kr.sendText(msg.to, "Bot is Turn Off")
                    except:
                        pass
#==========================[Kris]===========================
            elif msg.text in ["Cancel on","cancel on"]:
                if msg.from_ in admin:
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                            
            elif msg.text in ["Cancel off","cancel off"]:
                if msg.from_ in admin:
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Sambut on","sambut on"]:
                if msg.from_ in admin:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                            
            elif msg.text in ["Sambut off","sambut off"]:
                if msg.from_ in admin:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Sambutpoto on","sambutpoto on"]:
                if msg.from_ in admin:
                    if wait["Wc2"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc2"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                            
            elif msg.text in ["Sambutpoto off","sambutpoto off"]:
                if msg.from_ in admin:
                    if wait["Wc2"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc2"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Pergi on","pergi on"]:
                if msg.from_ in admin:
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                            
            elif msg.text in ["Pergi off","pergi off"]:
                if msg.from_ in admin:
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif msg.text in ["Kick on","kick on"]:
                if msg.from_ in admin:
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                            
            elif msg.text in ["Kick off","kick off"]:
                if msg.from_ in admin:
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already oғғ")
#==========================[Kris]===========================
            elif "getGroup" in msg.text:
                if msg.from_ in owner:
                    group = kr.getGroup(msg.to)
                    path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                    kr.sendImageWithURL(msg.to, path)
#==========================[Kris]===========================
            elif "Kaluarti " in msg.text.split():
                if msg.from_ in owner:
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
                        kr.sendText(msg.to,"Success left ["+ h +"] group")
                else:
                    kr.sendText(msg.to,"Khusus Creator/owner")
#==========================[Kris]===========================
            elif msg.text in ["LG"]:
                if msg.from_ in owner:
                    gids = kr.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                        #####gn = kr.getGroup(i).name
                        h += "[•]%s Member\n" % (kr.getGroup(i).name   +"👉"+str(len(kr.getGroup(i).members)))
                        kr.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))

            elif msg.text in ["LG2"]:
                if msg.from_ in owner:
                    gid = kr.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (kr.getGroup(i).name,i)
                        kr.sendText(msg.to,h)
#==========================[Kris]===========================
            elif "Asupka: " in msg.text:
                if msg.from_ in owner:
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
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Bot sudah berjalan selama "+waktu(eltime)
                    kr.sendText(msg.to,van)
#==========================[Kris]===========================
            elif msg.text in ["Cctv restart","cctv restart"]:
                if msg.from_ in admin:
                    kr.sendText(msg.to, "Bot Cctv has been restarted")
                    restart_program()
                    print "@Restart"
#==========================[Kris]===========================
            elif msg.text in ["Gcreator"]:
                if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = kr.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    kr.sendText(msg.to, "Group Creator : " + gCreator1)
                    kr.sendMessage(msg)
#==========================[Kris]===========================
            elif msg.text in ["Tag on","tag on"]:
                if msg.from_ in admin:
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already on")
                        else:
                            kr.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag On")
                        else:
                            kr.sendText(msg.to,"already on")
                        
            elif msg.text in ["Tag off","tag off"]:
                if msg.from_ in admin:
                    if wait["tag"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already off")
                        else:
                            kr.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag Off")
                        else:
                            kr.sendText(msg.to,"Already off")
#==========================[Kris]===========================
            elif msg.text in ["Tag2 on","tag2 off"]:
                if msg.from_ in admin:
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already on")
                        else:
                            kr.sendText(msg.to,"Tag On")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag On")
                        else:
                            kr.sendText(msg.to,"already on")
                            
            elif msg.text in ["Tag2 off","tag2 off"]:
                if msg.from_ in admin:
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already off")
                        else:
                            kr.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag Off")
                        else:
                            kr.sendText(msg.to,"Already off")
#==========================[Kris]===========================
            elif msg.text in ["Auto on","auto on"]:
                if msg.from_ in admin:
                    if wait["auto"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Bot join on")
                        else:
                            kr.sendText(msg.to,"Bot join On")
                    else:
                        wait["auto"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Bot join On")
                        else:
                            kr.sendText(msg.to,"Bot join On")
                            
            elif msg.text in ["Auto off","auto off"]:
                if msg.from_ in admin:
                    if wait["auto"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Bot join off")
                        else:
                            kr.sendText(msg.to,"Bot join off")
                    else:
                        wait["auto"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Bot join off")
                        else:
                            kr.sendText(msg.to,"Bot join off")
#==========================[Kris]===========================
            elif "Tambah admin @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Tambah admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
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
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                kr.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    kr.sendText(msg.to,"Command Di Tolak Jangan Sedih")
                    kr.sendText(msg.to,"Sudah Menjadi Admin Maka Tidak Bisa Menjadi Admin Lagi")
#==========================[Kris]===========================
            elif "Hapus admin @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Hapus admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
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
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                kr.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    kr.sendText(msg.to,"Command DiTolak")
                    kr.sendText(msg.to,"Admin Tidak Bisa Menggunakan")
#==========================[Kris]===========================
            elif msg.text in ["Adminlist","admlist"]:
                if msg.from_ in admin:
                    if admin == []:
                        kr.sendText(msg.to,"The adminlist is empty")
                    else:
                        kr.sendText(msg.to,"Sabar Dikit Boss Kris.....")
                        mc = ""
                        for mi_d in admin:
                            mc += "☄ " +kr.getContact(mi_d).displayName + "\n"
                        kr.sendText(msg.to,mc)
                        print "[Command]Stafflist executed"

#==========================[Kris]===========================
            elif ("Ban " in msg.text):
                if msg.from_ in admin:
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
                          kr.sendText(msg.to,"Succes Banned")
                       except:
                          pass

#==========================[Kris]===========================
            elif msg.text in ["Time"]:
                if msg.from_ in admin:
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
                    kr.sendText(msg.to, rst)
                    #client.sendText(msg.to, rst)

#==========================[Kris]===========================
            elif msg.text in ["cab","Cab"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    kr.sendImageWithURL(msg.to, url)
                
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
                    kr.sendImageWithURL(msg.to, url)
                    kr.sendImageWithURL(msg.to, url1)
                    kr.sendImageWithURL(msg.to, url2)
                    kr.sendImageWithURL(msg.to, url3)
                    kr.sendImageWithURL(msg.to, url4)
                    kr.sendImageWithURL(msg.to, url5)
                    kr.sendImageWithURL(msg.to, url6)
                    kr.sendImageWithURL(msg.to, url7)
#==========================[Kris]===========================
            elif msg.text in ["Kibar","kibar"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    kr.sendImageWithURL(msg.to, url)
                    kr.sendImageWithURL(msg.to, url1)
                    kr.sendImageWithURL(msg.to, url6)
                    kr.sendImageWithURL(msg.to, url7)
#==========================[Kris]===========================
            elif msg.text in ["setview","Setview"]:
                if msg.from_ in admin:
                    subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                    kr.sendText(msg.to, "Checkpoint checked!")
                    print "@setview"

            elif msg.text in ["viewseen","Viewseen"]:
                if msg.from_ in admin:
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
                                cName.append('nones')
                                pass
                        contactId = kr.getContacts(recheckData)
                        for v in range(len(recheckData)):
                            dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                            pass
                        if len(dataResult) > 0:
                            tukang = "List Viewer\n*"
                            grp = '\n* '.join(str(f) for f in dataResult)
                            total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                            kr.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        else:
                            kr.sendText(msg.to, "Belum ada viewers")
                        print "@viewseen"

#==========================[Kris]===========================
            elif msg.text in ["Respon","respon"]:
                if msg.from_ in admin:
					kr.sendText(msg.to,"Bot Cctv Aktif...(^_^)")
            elif msg.text in ["Absen","absen"]:
                if msg.from_ in admin:
                    kr1.sendText(msg.to,"💡💡💡👉 Bot Cctv Hadir..!!!")
#==========================[Kris]===========================
            elif msg.text in ["Cctv kadieu","cctv kadieu"]:
                if msg.from_ in owner:
                    gid = kr1.getGroupIdsJoined()
                    gid = kr2.getGroupIdsJoined()
                    gid = kr3.getGroupIdsJoined()
                    gid = kr4.getGroupIdsJoined()
                    gid = kr5.getGroupIdsJoined()
                    for i in gid:
                        kr1.sendText(i,"Bye~Bye\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nuntuk konfirmasi => line://ti/p/~krissthea\nMakasih...!!!")
                        kr.sendImageWithURL(i, url123)
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
            elif msg.text.lower() == 'Bot':
                kr.sendImageWithURL(msg.to, url123)
                kr.sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif "Bcgrup: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Bcgrup: ","")
                    gid = kr.getGroupIdsJoined()
                    for i in gid:
                        kr.sendText(i,"╠═════[BROADCAST]═════╣\n\n"+bc+"\n\nMAAF BROADCAST!!\n\n=>>line://ti/p/~krissthea\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")
                        kr.sendText(msg.to, "Brodcastgrup sukses")
#==========================[Kris]===========================
            elif msg.text in ["Sp","sp"]:
                if msg.from_ in admin:
					start = time.time()
					kr1.sendText(msg.to, "Proses..🔥🔥🔥")
					elapsed_time = time.time() - start
					kr1.sendText(msg.to, "%s/Detik" % (elapsed_time))
					
            elif msg.text in ["Speed","speed"]:
                if msg.from_ in admin:
					start = time.time()
					kr.sendText(msg.to, "Proses..🔥🔥🔥")
					elapsed_time = time.time() - start
					kr.sendText(msg.to, "%s/Detik" % (elapsed_time))
#==========================[Kris]===========================
            elif msg.text in ["Clearban"]:
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    kr.sendText(msg.to,"clear")
                    
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
					wait["wblacklist"] = True
					kr.sendText(msg.to,"Kirim Kontak")
					
            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
					wait["dblacklist"] = True
					kr.sendText(msg.to,"Kirim Kontak")
					
            elif msg.text in ["Banlist"]:
                if msg.from_ in admin:
					if wait["blacklist"] == {}:
						kr.sendText(msg.to,"Tidak Ada")
					else:
						kr.sendText(msg.to,"Tunggu Sebentar Memuat Data")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "☄" +kr.getContact(mi_d).displayName + "\n"
						kr.sendText(msg.to,mc)
						
            elif msg.text in ["Cek ban"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						group = kr.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						kr.sendText(msg.to,cocoa + "")
						
            elif msg.text in ["Kill ban"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						group = kr.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kr.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
						    kr.kickoutFromGroup(msg.to,[jj])
						    kr1.kickoutFromGroup(msg.to,[jj])
						kr.sendText(msg.to,"Bye...")
#==========================[Kris]===========================
            elif msg.text in ["Batal","batal"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							kr.cancelGroupInvitation(msg.to, gInviMids)
#==========================[Kris]===========================
            elif "Cctv cium " in msg.text:
                if msg.from_ in admin:
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
            elif "Cctv megs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("Cctv megs ","")
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
                if msg.from_ in owner:
                    gName = msg.text.replace("#rmegs ","")
                    ap = kr1.getGroups([msg.to])
                    semua = findAndAddContactsByMid(Mi_d)
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        klis=[kr,kr1]
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
                if msg.from_ in owner:
                    thisgroup = kr.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr.createGroup("Rrecover", mi_d)
                    kr.sendText(msg.to,"Success recover")
            elif msg.text in ["Cctv spin"]:
                if msg.from_ in owner:
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
                if msg.from_ in owner:
                    kr1.removeAllMessages(msg.to)
                    kr2.removeAllMessages(msg.to)
                    kr3.removeAllMessages(msg.to)
                    kr4.removeAllMessages(msg.to)
                    kr5.removeAllMessages(msg.to)
                    kr.sendText(msg.to,"Removed all chat Finish")
#==========================[Kris]===========================
            elif msg.text in ["Cctv muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr1.sendMessage(msg)
                    
            elif msg.text in ["Muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr.sendMessage(msg)
#==========================[Kris]===========================
            elif "Cctv spamtag @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Cctv spamtag @","")
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
                if msg.from_ in owner:
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
            elif "Cctv spamkontak @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Cctv spamkontak @","")
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
                if msg.from_ in owner:
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
            
        
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = kr.getContact(op.param2).displayName
                            Name = kr.getContact(op.param2).displayName
                            Name = kr.getContact(op.param2).displayName
                            Name = kr.getContact(op.param2).displayName
                            Name = kr.getContact(op.param2).displayName
                            Np = kr.getContact(op.param2).pictureStatus
                            Np = kr.getContact(op.param2).pictureStatus
                            Np = kr.getContact(op.param2).pictureStatus
                            Np = kr.getContact(op.param2).pictureStatus
                            Np = kr.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        kr.sendText(op.param1, "Hallo.. " + "☞ " + nick[0] + " ☜" + "\nNah jangan ngintip mulu 😁. . .\nGabung Chat yux 😉")
                                        kr.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        kr.sendText(op.param1, "Hallo.. " + "☞ " + nick[1] + " ☜" + "\nJangan ngintip.. 😏. . .\nMasuk  ayox... 😆😂😛")
                                        kr.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    kr.sendText(op.param1, "hallo.. " + "☞ " + Name + " ☜" + "\nJangan ngintip aja\nMasuk gabung chat ya...😋 😝")
                                    kr.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
        
        if op.type == 59:
            print op
            
    
    except Exception as error:
        print error

while True:
    try:
        Ops = kr.fetchOps(kr.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kr.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kr.Poll.rev = max(kr.Poll.rev, Op.revision)
            bot(Op)
