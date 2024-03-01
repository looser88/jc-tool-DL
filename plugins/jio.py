from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import aiohttp
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait
from bot import Bot
# from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from pathlib import Path
import subprocess
import requests
import jwt
import string
import re
import requests
import asyncio
import base64


import base64, requests, sys, base64, json
from pywidevi.L3.cdm import cdm, deviceconfig
from base64 import b64encode
from pywidevi.L3.getPSSH import get_pssh
from pywidevi.L3.decrypt.wvdecryptcustom import WvDecrypt
import time
import re 



m3u8DL_RE = 'N_m3u8DL-RE'


import re
@Bot.on_message(filters.private & filters.regex(pattern=".*http.*"))
async def echo(bot, update):
        imog = await update.reply_text("<b>Processing... ⏳</b>",)
        link = update.text
        link_id = link.split("/")[-1]
        # link_id = re.findall(r'.*/(.*)', link)[0].strip()
        access_token = get_accesstoken()[0]
        print(f"access_token is - {get_accesstoken()[0]}")
        header_data = jwt.get_unverified_header(access_token)
        decoded = jwt.decode(access_token, algorithms=["HS512", "HS256"], options={"verify_signature": False})
        deviceId = decoded['data']['deviceId']
        print(f"deviceId is - {deviceId}")
        uniqueid = decoded['data']['userId']
        print(f"uniqueid is - {uniqueid}")
        appName = decoded['data']['appName']
        print(f"appName is - {appName}")

        headers2 = {
            'authority': 'apis-jiovoot.voot.com',
            'accept': 'application/json, text/plain, */*',
            'accesstoken': access_token,
            'appname': "RJIL_JioCinema",
            'content-type': 'application/json',
            'deviceid': get_accesstoken()[1],
            'origin': 'https://www.jiocinema.com',
            'referer': 'https://www.jiocinema.com/',
            'uniqueid': uniqueid,
            'user-agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'versioncode': '2312070',
            'x-platform': 'androidweb',
            'x-platform-token': 'web',
        }

        json_data2 = {
            '4k': False,
            'ageGroup': '18+',
            'appVersion': '3.4.0',
            'bitrateProfile': 'xhdpi',
            'capability': {
                'drmCapability': {
                    'aesSupport': 'yes',
                    'fairPlayDrmSupport': 'yes',
                    'playreadyDrmSupport': 'none',
                    'widevineDRMSupport': 'yes',
                },
                'frameRateCapability': [
                    {
                        'frameRateSupport': '30fps',
                        'videoQuality': '1440p',
                    },
                ],
            },
            'continueWatchingRequired': True,
            'dolby': False,
            'downloadRequest': False,
            'hevc': False,
            'kidsSafe': False,
            'manufacturer': 'Windows',
            'model': 'Windows',
            'multiAudioRequired': True,
            'osVersion': '10',
            'parentalPinValid': True,
        }

        response2 = requests.post('https://apis-jiovoot.voot.com/playbackjv/v4/'+link_id+'', headers=headers2, json=json_data2, verify=False).json()

        contentType = response2['data']['contentType']
        
        if contentType == 'MOVIE':
            movie_name = response2['data']['name']
            title = f'{movie_name}'

        elif contentType == 'EPISODE':
            showName = response2['data']['show']['name']
            season_num = int(response2['data']['episode']['season'])
            episode_num = int(response2['data']['episode']['episodeNo'])
            episode_title = response2['data']['fullTitle']
            
            title = f'{showName} - S{season_num:02d}E{episode_num:02d} - {episode_title}'

        else:
            movie_name = response2['data']['name']
            title = f'{movie_name}'

        title = replace_invalid_chars(title)
        print(f'\n{title}\n')
        mpd = response2['data']['playbackUrls'][0]['url']
        print(mpd)
        lic_url = response2['data']['playbackUrls'][0]['licenseurl']
        await imog.edit(text=mpd)
        try:
            headers03 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            }
            
            response03 = requests.get(mpd, headers=headers03, verify=False).text
            
            pssh = re.findall(r'<cenc:pssh>(.{20,170})</cenc:pssh>', response03)[0].strip()
            print(f'{pssh}\n')


            headers = {
                'authority': 'prod.media.jio.com',
                'accesstoken': access_token,
                'appname': appName,
                'content-type': 'application/octet-stream',
                'deviceid': deviceId,
                'devicetype': 'Web',
                'isdownload': 'false',
                'origin': 'https://www.jiocinema.com',
                'os': 'android',
                'referer': 'https://www.jiocinema.com/',
                'uniqueid': uniqueid,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'versioncode': '570',
                'x-feature-code': 'ytvjywxwkn',
                'x-platform': 'Web',
                'x-playbackid': uniqueid,
            }
            
            def WV_Function(pssh, lic_url, cert_b64=None):
                wvdecrypt = WvDecrypt(init_data_b64=pssh, cert_data_b64=cert_b64, device=deviceconfig.device_android_generic)                   
                widevine_license = requests.post(url=lic_url, data=wvdecrypt.get_challenge(), headers=headers, verify=False)
                license_b64 = b64encode(widevine_license.content)
                wvdecrypt.update_license(license_b64)
                Correct, keyswvdecrypt = wvdecrypt.start_process()
                if Correct:
                    return Correct, keyswvdecrypt
            Correct, keys = WV_Function(pssh, lic_url)
            
            print(keys)
            for key in keys:
                print('--key ' + key)
            
            ke_ys = ' '.join([f'--key {key}' for key in keys]).split()
            
            print()
            subprocess.run([m3u8DL_RE,
                            '-M', 'format=mkv:muxer=ffmpeg',
                            '--concurrent-download',
                            '--log-level', 'INFO',
                            '--save-name', 'video', mpd, *ke_ys], shell=True)

        except IndexError: #DRM free
            print()
            subprocess.run([m3u8DL_RE,
                            '-M', 'format=mkv:muxer=ffmpeg',
                            '--concurrent-download',
                            '--log-level', 'INFO',
                            '--save-name', 'video', mpd])

        try:
            Path('video.mkv').rename(''+title+'.mkv')
            print(f'{title}.mkv \nall done!\n')
        except FileNotFoundError:
            print("[ERROR] no mkv file")
   

















def replace_invalid_chars(title: str) -> str:
    invalid_chars = {'<': '\u02c2', '>': '\u02c3',
    ':': '\u02d0', '"': '\u02ba', '/': '\u2044',
    '\\': '\u29f9', '|': '\u01c0', '?': '\u0294',
    '*': '\u2217'}
    
    return ''.join(invalid_chars.get(c, c) for c in title)
    

def get_accesstoken():
            IdURL = "https://cs-jv.voot.com/clickstream/v1/get-id"
            GuestURL = "https://auth-jiocinema.voot.com/tokenservice/apis/v4/guest"
            id = requests.get(url=IdURL).json()['id']
        
            token = requests.post(url=GuestURL, json={
                    'adId': id,
                    "appName": "RJIL_JioCinema",
                    "appVersion": "23.10.13.0-841c2bc7",
                    "deviceId": id,
                    "deviceType": "phone",
                    "freshLaunch": True,
                    "os": "ios"
                }, headers={
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
                }).json()
    
            return token["authToken"],token["deviceId"]
    
    
@Bot.on_message(filters.command('start') & filters.private )
async def start_command(client, message):
    await message.reply_text("hello buddy ......",quote=True)

@Bot.on_message(filters.command('token') & filters.private )
async def start_command(client: Client, message: Message):
    
    IdURL = "https://cs-jv.voot.com/clickstream/v1/get-id"
    GuestURL = "https://auth-jiocinema.voot.com/tokenservice/apis/v4/guest"
    id = requests.get(url=IdURL).json()['id']
    token = requests.post(url=GuestURL, json={
            'adId': id,
            "appName": "RJIL_JioCinema",
            "appVersion": "23.10.13.0-841c2bc7",
            "deviceId": id,
            "deviceType": "web",
            "freshLaunch": True,
            "os": "ios"
        }, headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }).json()

    tkn = token
    bot_msg = await message.reply_text(tkn, quote = True)
