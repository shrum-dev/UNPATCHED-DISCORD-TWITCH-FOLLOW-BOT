import disnake
from disnake.ext import commands
import time
import threading
import requests
import random
import socks


botchannel = 1099431588057587722
logschannel =  1099431588057587722
moderators = [5418189181651561651651]

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
discord = disnake

x1 = "Bronze"
x2 = "Gold"
x5 = "Diamond"
x6 = "Silver"
x3 = "Premium"
x4 = "Premium +"

def get_username(channel_name):chat

    json= disnake
from disnake.ext import commands
import time
import threading
import requests
import random
import socks
            "variables": {
                "login": chat
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe"
                }
            }
        }

    headers = {
        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }
    try:
        r = requests.post('https://gql.twitch.tv/gql', json=json, headers=headers)
        return r.json()['data']['userOrError']['id']
    except:
        return None

def follower(target_id):
    try:
        global followsent
        i1 = open('tokens.txt', 'r').read().splitlines()
        i2 = random.choice(i1)
        headers = {
                'Accept': 'application/vnd.twitchtv.v3+json',
                'Accept-Language': 'en-us',
                'api-consumer-type': 'mobile; Android/1404000',
                'authorization': f'OAuth {i2}',
                'client-id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
                'client-session-id': '7f4b1045-f52b-49da-bcef-a81394610476',
                'connection': 'Keep-Alive',
                'content-type': 'application/json',
                'host': 'gql.twitch.tv',

                'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000',
                'x-apollo-operation-id': 'cd112d9483ede85fa0da514a5657141c24396efbc7bac0ea3623e839206573b8',
                'x-apollo-operation-name': 'FollowUserMutation',
                'x-app-version': '14.4.0',
                'x-device-id': 'e5c5e81ebfca405784e1da77aacca842'
            }
        data =   {
                    "operationName": "FollowUserMutation",
                    "variables": {
                    "targetId": target_id,
                    "disableNotifications": False
                    },
                    "extensions": {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": "cd112d9483ede85fa0da514a5657141c24396efbc7bac0ea3623e839206573b8"
                    }
                    }
                }
        response = requests.post('https://gql.twitch.tv/gql', json=data, headers=headers)
        followsent += 1
    except Exception as e:
        None

def followerraid(channel):
                            
                            token = open('tokens.txt', 'r').read().splitlines()
                            tokens = random.choice(token)
                            headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",'Authorization':f'OAuth {tokens}'}
                            response = requests.get("https://id.twitch.tv/oauth2/validate",headers=headers).json()
                            token_name = response['login']
                            guser = get_username(token_name)
                            
                            
                            headers = {
                                'Accept': 'application/vnd.twitchtv.v3+json',
                                'Accept-Language': 'en-us',
                                'api-consumer-type': 'mobile; Android/1404000',
                                'authorization': f'OAuth {tokens}',
                                'client-id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
                                'client-session-id': '7f4b1045-f52b-49da-bcef-a81394610476',
                                'connection': 'Keep-Alive',
                                'content-type': 'application/json',
                                'host': 'gql.twitch.tv',

                                'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000',
                                'x-apollo-operation-id': '412f0fd1876b9fe3426cd726b00b4e4fff9ea3e027e03407de89b6dd0c8674e7',
                                'x-apollo-operation-name': 'CreateRaidMutation',
                                'x-app-version': '14.4.0',
                                'x-device-id': '6c2a973b192849fea684773a218e34f4'
                            }
                            data =   {
                                        "operationName": "CreateRaidMutation",
                                        "variables": {
                                        "input": {
                                            "sourceID": guser,
                                            "targetID": get_username(channel)
                                        }
                                        },
                                        "extensions": {
                                        "persistedQuery": {
                                            "version": 1,
                                            "sha256Hash": "412f0fd1876b9fe3426cd726b00b4e4fff9ea3e027e03407de89b6dd0c8674e7"
                                        }
                                        }
                                    }
                            r = requests.post('https://gql.twitch.tv/gql', headers=headers, json=data)
                            print(r.text)
                            time.sleep(20)
                            headersf = {
                                'Accept': 'application/vnd.twitchtv.v3+json',
                                'Accept-Language': 'en-us',
                                'api-consumer-type': 'mobile; Android/1404000',
                                'authorization': f'OAuth {tokens}',
                                'client-id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
                                'client-session-id': '7f4b1045-f52b-49da-bcef-a81394610476',
                                'connection': 'Keep-Alive',
                                'content-type': 'application/json',
                                'host': 'gql.twitch.tv',

                                'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000',
                                'x-apollo-operation-id': '54268306ec0b1e37d0cad4079ed4a0a057f3ff1dbc901580b6e09fa0fb8709c1',
                                'x-apollo-operation-name': 'GoRaidMutation',
                                'x-app-version': '14.4.0',
                                'x-device-id': '6c2a973b192849fea684773a218e34f4'
                            }
                            datag =   {
                                "operationName": "GoRaidMutation",
                                "variables": {
                                "channelId": guser
                                },
                                "extensions": {
                                "persistedQuery": {
                                    "version": 1,
                                    "sha256Hash": "54268306ec0b1e37d0cad4079ed4a0a057f3ff1dbc901580b6e09fa0fb8709c1"
                                }
                                }
                            }
                            r = requests.post('https://gql.twitch.tv/gql', headers=headersf, json=datag)
                            print(r.text)

def joinraidd(raidid):
                            t = open('tokens.txt', 'r').read().splitlines()
                            t1 = random.choice(t)
                            headers = {
                                'Accept': 'application/vnd.twitchtv.v3+json',
                                'Accept-Language': 'en-us',
                                'api-consumer-type': 'mobile; Android/1404000',
                                'authorization': f'OAuth {t1}',
                                'client-id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
                                'client-session-id': '7f4b1045-f52b-49da-bcef-a81394610476',
                                'connection': 'Keep-Alive',
                                'content-type': 'application/json',
                                'host': 'gql.twitch.tv',

                                'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) tv.twitch.android.app/14.4.0/1404000',
                                'x-apollo-operation-id': '412f0fd1876b9fe3426cd726b00b4e4fff9ea3e027e03407de89b6dd0c8674e7',
                                'x-apollo-operation-name': 'CreateRaidMutation',
                                'x-app-version': '14.4.0',
                                'x-device-id': '6c2a973b192849fea684773a218e34f4'
                            }
                            data =   {
                                "operationName": "JoinRaidMutation",
                                "variables": {
                                "input": raidid
                                },
                                "extensions": {
                                "persistedQuery": {
                                    "version": 1,
                                    "sha256Hash": "7b56131e1c45db978b59d29e966280b1e32f43e5d1e2b2840f96109063826c49"
                                }
                                }
                            }
                            r = requests.post('https://gql.twitch.tv/gql', json=data, headers=headers)

def viewstart(channel):
                lines = open("proxy.txt", "r").read().splitlines()
                proxy = random.choice(lines)
                proxies = {"http": "http://"+proxy, "https": "http://"+proxy}  

                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US',
                    'Authorization': 'undefined',
                    'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    'Connection': 'keep-alive',
                    'Content-Type': 'text/plain; charset=UTF-8',
                    'Device-ID': '6GsDKc6Jagdhp140DfRs7IjMgInpV5Iw',
                    'Origin': 'https://www.twitch.tv',
                    'Prefer': 'safe',
                    'Referer': 'https://www.twitch.tv/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                data = '{"operationName":"PlaybackAccessToken_Template","query":"query PlaybackAccessToken_Template($login: String!, $isLive: Boolean!, $vodID: ID!, $isVod: Boolean!, $playerType: String!) {  streamPlaybackAccessToken(channelName: $login, params: {platform: \\"web\\", playerBackend: \\"mediaplayer\\", playerType: $playerType}) @include(if: $isLive) {    value    signature    __typename  }  videoPlaybackAccessToken(id: $vodID, params: {platform: \\"web\\", playerBackend: \\"mediaplayer\\", playerType: $playerType}) @include(if: $isVod) {    value    signature    __typename  }}","variables":{"isLive":true,"login":"'+channel+'","isVod":false,"vodID":"","playerType":"site"}}'
                try:
                    r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data, proxies=proxies)
                    #print(response.text)
                    start = r.text.find('"value":"') + 9
                    end = r.text.find('","signature')
                    xtoken = r.text[start:end]
                    token = xtoken.replace('\\', '')
                    start = r.text.find('signature":"') + 12
                    end = r.text.find('","__typename')
                    sig = r.text[start:end]
                    linktoken = token.replace('{', '%7B').replace('}', '%7D').replace('"', "%22").replace(':', '%3A').replace(',', '%2C')
                except:
                    None

                headers = {
                    'Accept': 'application/x-mpegURL, application/vnd.apple.mpegurl, application/json, text/plain',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
                }

                params = {
                    'allow_source': 'true',
                    'fast_bread': 'true',
                    'p': '3839592',
                    'play_session_id': '587e61679bcc5503d760eda271c30dc0',
                    'player_backend': 'mediaplayer',
                    'playlist_include_framerate': 'true',
                    'reassignments_supported': 'true',
                    'sig': sig,
                    'supported_codecs': 'avc1',
                    'token': token,
                    'cdm': 'wv',
                    'player_version': '1.10.0',
                }
                try:
                    response = requests.get(f'https://usher.ttvnw.net/api/channel/hls/{channel}.m3u8?allow_source=true&fast_bread=true&p=5725800&play_session_id=df4348c5caad4f981aba7aab8df7759a&player_backend=mediaplayer&playlist_include_framerate=true&reassignments_supported=true&sig={sig}&supported_codecs=avc1&token={linktoken}&cdm=wv&player_version=1.10.0', params=params, headers=headers, proxies=proxies)
                    start = response.text.find('https://video-weaver')
                    end = response.text.find('.m3u8') + 5
                    link = response.text[start:end]
                except:
                    None
                #print(response.status_code)

                headers = {
                    'Accept': 'application/x-mpegURL, application/vnd.apple.mpegurl, application/json, text/plain',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
                }
                try:
                    response = requests.get(link, headers=headers, proxies=proxies)
                except Exception as e:
                    None

@bot.slash_command(description='Sends twitch followers to a channel.')
@commands.cooldown(1, 120, commands.BucketType.user)
async def tfollow(interaction: disnake.ApplicationCommandInteraction, channel):
    if interaction.channel_id == botchannel:
        amunt = 0
        if interaction.user.get_role(1098769651699302482):
            amunt = amunt + 1000
        elif interaction.user.get_role(1098769497327943680):
            amunt = amunt + 800
        elif interaction.user.get_role(1098769495801217114):
            amunt = amunt + 500
        elif interaction.user.get_role(1098769490189234288):
            amunt = amunt + 300
        elif interaction.user.get_role(1098769498607202396):
            amunt = amunt + 120
        elif interaction.user.get_role(1098769433532567663):
            amunt = amunt + 75
        else:
            amunt = 40
        await interaction.response.defer(with_message=True, ephemeral=True)
        embed = discord.Embed(
                    title='ID check',
                    description='Checking if twitch channel exists... Please wait.',
                    color=0x538ab1
        )
        await interaction.send(embed=embed)
        channel_id = get_username(channel)
        if channel_id == None:
                embed = discord.Embed(
                        title='Failed',
                        description='The username you have entered is wrong. Double check the spellings and try again.',
                        color=0x0b76b8
                )
                await interaction.edit_original_message(embed=embed)
        else:
                def start():
                      for i in range(amunt):
                            follower(channel_id)
                embed = discord.Embed(
                        title='Success',
                        description=f'Sending `{amunt}` followers to `{channel}`',
                        color=0x0b76b8
                )
                await interaction.edit_original_message(embed=embed)
                threading.Thread(target=start).start()
    else:
            embed = discord.Embed(
                    title='Wrong channel.',
                    description=f'You cannot use commands in this channel, go to <#{botchannel}>',
                    color=0x0b76b8
            )
            await interaction.send(embed=embed)

@bot.slash_command(description='Joins raid with raid id [GOLD OR DIAMOND ONLY]')
@commands.cooldown(1, 120, commands.BucketType.user)
async def joinraid(interaction: disnake.ApplicationCommandInteraction, channel, raidid):
    if interaction.channel_id == botchannel:
        await interaction.response.defer(with_message=True, ephemeral=True)
        amunt = 0
        if interaction.user.get_role(1098770200201003071):
            amunt = amunt + 15
        elif interaction.user.get_role(1098770210867118192):
            amunt = amunt + 30
        elif interaction.user.get_role(1098770210867118192):
            amunt = amunt + 45
        elif interaction.user.get_role(1098770217380888708):
            amunt = amunt + 50
        else:
              amunt = 0
        if amunt >= 1:
            embed = discord.Embed(
                        title='ID check',
                        description='Checking if channel exists... Please wait.',
                        color=0x538ab1
            )
            await interaction.send(embed=embed)
            channel_id = get_username(channel)
            if channel_id == None:
                    embed = discord.Embed(
                            title='Failed',
                            description='The username you have entered is wrong. Double check the spellings and try again.',
                            color=0x0b76b8
                    )
                    await interaction.edit_original_message(embed=embed)
            else:
                def start():
                        for i in range(amunt):
                            joinraidd(raidid)
                embed = discord.Embed(
                        title='Success',
                        description=f'Sending `{amunt}` joins to `{raidid}`',
                        color=0x0b76b8
                )
                await interaction.edit_original_message(embed=embed)
                threading.Thread(target=start).start()
        else:
            embed = discord.Embed(
                  title='Denied access.',
                  description='Missing roles. You must have Gold or above in order to use this command!'
            )
            await interaction.send(embed=embed)
    else:
          embed = discord.Embed(
                title='Wrong channel.',
                description=f'You cannot use commands in this channel, go to <#{botchannel}>',
                color=0x0b76b8
          )
          await interaction.send(embed=embed)

@bot.slash_command(description='Creates 5 raids in a channel [GOLD OR DIAMOND ONLY]')
@commands.cooldown(1, 120, commands.BucketType.user)
async def createraid(interaction: disnake.ApplicationCommandInteraction, channel):
    
    if interaction.channel_id == botchannel:
        await interaction.response.defer(with_message=True, ephemeral=True)
        amunt = 0
        if interaction.user.get_role(1068239463047757904):
            amunt = amunt + 15
        elif interaction.user.get_role(1068239342507675738):
            amunt = amunt + 30
        elif interaction.user.get_role(1068239236404359239):
            amunt = amunt + 45
        elif interaction.user.get_role(1068239080829227069):
            amunt = amunt + 50
        else:
              amunt = 0
        if amunt >= 1:
            embed = discord.Embed(
                        title='ID check',
                        description='Checking if channel exists... Please wait.',
                        color=0x538ab1
            )
            await interaction.send(embed=embed)
            channel_id = get_username(channel)
            if channel_id == None:
                    embed = discord.Embed(
                            title='Failed',
                            description='The username you have entered is wrong. Double check the spellings and try again.',
                            color=0x0b76b8
                    )
                    await interaction.edit_original_message(embed=embed)
            else:
                def start():
                        for i in range(amunt):
                            followerraid(channel)
                embed = discord.Embed(
                        title='Success',
                        description=f'Sending `{amunt}` raids to `{channel}`',
                        color=0x0b76b8
                )
                await interaction.edit_original_message(embed=embed)
                threading.Thread(target=start).start()
        else:
            embed = discord.Embed(
                  title='Denied access.',
                  description='Missing roles. You must have Gold or above in order to use this command!'
            )
            await interaction.send(embed=embed)
    else:
          embed = discord.Embed(
                title='Wrong channel.',
                description=f'You cannot use commands in this channel, go to <#{botchannel}>',
                color=0x0b76b8
          )
          await interaction.send(embed=embed)



@bot.slash_command(description='Sends viewers to twitch channel [PREMIUM OR PREMIUM + ONLY]')
@commands.cooldown(1, 120, commands.BucketType.user)
async def tview(interaction: disnake.ApplicationCommandInteraction, channel):
    await interaction.response.defer(with_message=True, ephemeral=True)
    if interaction.channel_id == botchannel:
        
        amunt = 0
        if interaction.user.get_role(1068393987536322610):
            amunt = amunt + 2000
        else:
              amunt = 0
        if amunt >= 1:
            embed = discord.Embed(
                        title='ID check',
                        description='Checking if channel exists... Please wait.',
                        color=0x538ab1
            )
            await interaction.send(embed=embed)
            channel_id = get_username(channel)
            if channel_id == None:
                    embed = discord.Embed(
                            title='Failed',
                            descriptbion='The username you have entered is wrong. Double check the spellings and try again.',
                            color=0x0b76b8
                    )
                    await interaction.edit_original_message(embed=embed)
            else:
                def start():
                            viewstart(channel)
                embed = discord.Embed(
                        title='Success',
                        description=f'Sending `{amunt}` viewers to `{channel}`',
                        color=0x0b76b8
                )
                await interaction.edit_original_message(embed=embed)
                
                for i in range(amunt):
                    threading.Thread(target=start).start()
        else:
            embed = discord.Embed(
                  title='Denied access.',
                  description='Missing roles. You must have view access in order to use this command!'
            )
            await interaction.send(embed=embed)
    else:
          embed = discord.Embed(
                title='Wrong channel.',
                description=f'You cannot use commands in this channel, go to <#{botchannel}>',
                color=0x0b76b8
          )
          await interaction.send(embed=embed)

@tfollow.error
async def tfollow_error(ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You are on cooldown. Please wait {error.retry_after:.2f} seconds before trying again.")

@createraid.error
async def createraid_error(ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You are on cooldown. Please wait {error.retry_after:.2f} seconds before trying again.")

@joinraid.error
async def joinraid_error(ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You are on cooldown. Please wait {error.retry_after:.2f} seconds before trying again.")

@tview.error
async def tview_error(ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You are on cooldown. Please wait {error.retry_after:.2f} seconds before trying again.")

@bot.slash_command(description='Sends a list of commands that you can use!')
async def help(interaction: disnake.ApplicationCommandInteraction):
      await interaction.response.defer(with_message=True)
      embed = discord.Embed(
            title='Twitch bot',
            description=f'__Commands__\n/tfollow (channel)\n/tview (channel)\n/createraid (channel)\n/joinraid (channel)\n\n__Miscellaneous Commands__\n/blockuser (userid)\n/Addspam (userid)'
      )
      embed.set_footer(text=f'Invoked by {interaction.user.name}', icon_url=interaction.user.avatar)
      await interaction.send(embed=embed)
bot.run('YOUR_TOKEN_HERE')
