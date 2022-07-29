import requests
import time 

#SITES QUE SEMPRE RETORNAM POSITIVO
#WORDPRESS
#INSTAGRAM
#GOOGLE+
#PINTEREST
#STEAM
#TWITTER
# verificar sempre esses para que possa ter ou nao um perfil valido

print("      SOCHER         ")
print("───▄▄─▄████▄▐▄▄▄▌")
print("──▐──████▀███▄█▄▌")
print("▐─▌──█▀▌──▐▀▌▀█▀")
print("─▀───▌─▌──▐─▌")
print("─────█─█──▐▌█")
print("Lembrando que as vezes o site pode retornar que o user nao existe e assim dizendo que a rede social existe..")
inp = input("Digite o nome que deseja buscar\n -> ")

instagram = f'https://www.instagram.com/{inp}'
facebook = f'https://www.facebook.com/{inp}'
twitter = f'https://www.twitter.com/{inp}'
youtube = f'https://www.youtube.com/{inp}'
blogger = f'https://{inp}.blogspot.com'
google_plus = f'https://plus.google.com/s/{inp}/top'
reddit = f'https://www.reddit.com/user/{inp}'
wordpress = f'https://{inp}.wordpress.com'
pinterest = f'https://www.pinterest.com/{inp}'
github = f'https://www.github.com/{inp}'
tumblr = f'https://{inp}.tumblr.com'
flickr = f'https://www.flickr.com/people/{inp}'
steam = f'https://steamcommunity.com/id/{inp}'
vimeo = f'https://vimeo.com/{inp}'
soundcloud = f'https://soundcloud.com/{inp}'
disqus = f'https://disqus.com/by/{inp}'
medium = f'https://medium.com/@{inp}'
deviantart = f'https://{inp}.deviantart.com'
vk = f'https://vk.com/{inp}'
aboutme = f'https://about.me/{inp}'
flipboard = f'https://flipboard.com/@{inp}'
slideshare = f'https://slideshare.net/{inp}'
fotolog = f'https://fotolog.com/{inp}'
spotify = f'https://open.spotify.com/user/{inp}'
mixcloud = f'https://www.mixcloud.com/{inp}'
scribd = f'https://www.scribd.com/{inp}'
badoo = f'https://www.badoo.com/en/{inp}'
patreon = f'https://www.patreon.com/{inp}'
bitbucket = f'https://bitbucket.org/{inp}'
dailymotion = f'https://www.dailymotion.com/{inp}'
etsy = f'https://www.etsy.com/shop/{inp}'
cashme = f'https://cash.me/{inp}'
behance = f'https://www.behance.net/{inp}'
goodreads = f'https://www.goodreads.com/{inp}'
instructables = f'https://www.instructables.com/member/{inp}'
keybase = f'https://keybase.io/{inp}'
kongregate = f'https://kongregate.com/accounts/{inp}'
livejournal = f'https://{inp}.livejournal.com'
angellist = f'https://angel.co/{inp}'
last_fm = f'https://last.fm/user/{inp}'
dribbble = f'https://dribbble.com/{inp}'
codecademy = f'https://www.codecademy.com/{inp}'
gravatar = f'https://en.gravatar.com/{inp}'
pastebin = f'https://pastebin.com/u/{inp}'
foursquare = f'https://foursquare.com/{inp}'
gumroad = f'https://www.gumroad.com/{inp}'
newsground = f'https://{inp}.newgrounds.com'
wattpad = f'https://www.wattpad.com/user/{inp}'


SITES = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, gumroad, newsground,
wattpad ]

count = 0
match = True
list = []
GREEN = "\033[0;32m"
RED   = "\033[1;31m"

for url in SITES:
    try:
        r = requests.get(url)
        if r.status_code == 200:
            if match == True:
                print('[USERNAME] {} ENCONTRADO! '.format(inp))
                time.sleep(2)
                print("Iniciando buscas...")
                match = False
            if inp in r.text:
                #print(GREEN,'REDE ENCONTRADA: [{}] ...'.format(inp))
                print(GREEN,f'\n{url} - FOUND')
                print("\033[0;0m")
                list.append(url)
            else:
                continue
            count += 1
    except:
        print("error encontrado..")

total = len(SITES)
print(f'{list}\n')
print(f'FINALIZANDO... foram encontradas {count} redes em {total} websites.\n')
print("OBS: Lembrando que alguns usuarios utilizam nomes difrentes em suas redes sociais, voce pode buscar novamente com alguma variacao do nome...\n")

logs_list = str(list)

with open("logs.txt", "w") as logs:
    logs.write(logs_list)
    print("Sites encontrados foram incluidos nas logs...")