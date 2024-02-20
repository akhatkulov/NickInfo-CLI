import threading
import requests
import requests as r
import typer
import time
def main(a):
    s_n = ['instagram','facebook','twitter','youtube','blogger','reddit','pinterest','github','tumblr','flickr','vimeo','soundcloud',
'disqus','medium','devianart','vk','about.me','imgur','slideshare','spotify','scribd','badoo','patreon','bitbucket','dailymotion','etsy','cashme',
'behance','goodreads','instructables','keybase','kongregate','livejournal','angellist','last.fm','dribbble','codeacademy','gravatar','foursquare','gumroad',
'newgrounds','wattpad','canva','creativemarket','trakt','tripadvisor','hubpages','contently','houzz','blip.fm','wikipedia' ,'codementor',
'reverbnation','designspiration65','bandcamp','colourlovers','ifttt','slack','okcupid','trip','ello','hackerone','freelancer']
    links = {
    'instagram' :f'https://www.instagram.com/{a}',
    'facebook'  :f'https://www.facebook.com/{a}',
    'twitter'   :f'https://www.twitter.com/{a}',
    'youtube'   :f'https://www.youtube.com/{a}',
    'blogger'   :f'https://{a}.blogspot.com',
    'reddit'    :f'https://www.reddit.com/user/{a}',
    'pinterest' :f'https://www.pinterest.com/{a}',
    'github'    :f'https://www.github.com/{a}',
    'tumblr'    :f'https://{a}.tumblr.com',
    'flickr'    :f'https://www.flickr.com/people/{a}',
    'vimeo'     :f'https://vimeo.com/{a}',
    'soundcloud':f'https://soundcloud.com/{a}',
    'disqus'    :f'https://disqus.com/{a}',
    'medium'    :f'https://medium.com/@{a}',
    'devianart' :f'https://{a}.deviantart.com',
    'vk'        :f'https://vk.com/{a}',
    'about.me'  :f'https://about.me/{a}',
    'imgur'     :f'https://imgur.com/user/{a}',
    'slideshare':f'https://slideshare.net/{a}',
    'spotify'   :f'https://open.spotify.com/user/{a}',
    'scribd'    :f'https://www.scribd.com/{a}',
    'badoo'     :f'https://www.badoo.com/en/{a}',
    'patreon'   :f'https://www.patreon.com/{a}',
    'bitbucket' :f'https://bitbucket.org/{a}',
    'dailymotion':f'https://www.dailymotion.com/{a}',
    'etsy'      :f'https://www.etsy.com/shop/{a}',
    'cashme'    :f'https://cash.me/{a}',
    'behance'   :f'https://www.behance.net/{a}',
    'goodreads' :f'https://www.goodreads.com/{a}',
    'instructables':f'https://www.instructables.com/member/{a}',
    'keybase'   :f'https://keybase.io/{a}',
    'kongregate':f'https://kongregate.com/accounts/{a}',
    'livejournal':f'https://{a}.livejournal.com',
    'angellist' :f'https://angel.co/{a}',
    'last.fm'   :f'https://last.fm/user/{a}',
    'dribbble'  :f'https://dribbble.com/{a}',
    'codeacademy':f'https://www.codecademy.com/{a}',
    'gravatar'  :f'https://en.gravatar.com/{a}',
    'foursquare':f'https://foursquare.com/{a}',
    'gumroad'   :f'https://www.gumroad.com/{a}',
    'newgrounds':f'https://{a}.newgrounds.com',
    'wattpad'   :f'https://www.wattpad.com/user/{a}',
    'canva'     :f'https://www.canva.com/{a}',
    'creativemarket':f'https://creativemarket.com/{a}',
    'trakt'     :f'https://www.trakt.tv/users/{a}',
    'tripadvisor':f'https://tripadvisor.com/members/{a}',
    'hubpages'  :f'https://{a}.hubpages.com',
    'contently' :f'https://{a}.contently.com',
    'houzz'     :f'https://houzz.com/user/{a}',
    'blip.fm'   :f'https://blip.fm/{a}',
    'wikipedia' :f'https://www.wikipedia.org/wiki/User:{a}',
    'codementor':f'https://www.codementor.io/{a}',
    'reverbnation':f'https://www.reverbnation.com/{a}',
    'designspiration65':f'https://www.designspiration.net/{a}',
    'bandcamp'  :f'https://www.bandcamp.com/{a}',
    'colourlovers':f'https://www.colourlovers.com/love/{a}',
    'ifttt'     :f'https://www.ifttt.com/p/{a}',
    'slack'     :f'https://{a}.slack.com',
    'okcupid'   :f'https://www.okcupid.com/profile/{a}',
    'trip'      :f'https://www.trip.skyscanner.com/user/{a}',
    'ello'      :f'https://ello.co/{a}',
    'hackerone' :f'https://hackerone.com/{a}',
    'freelancer':f'https://www.freelancer.com/u/{a}'
}   
    
    def check_username_1():

        for i in range(0,5):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy"
                else:
                    res+=f"{s_n[i]} -- empty"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))

    def check_username_2():
        
        for i in range(5,10):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 2"
                else:
                    res+=f"{s_n[i]} -- empty 2"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))


    def check_username_3():
    
    
        for i in range(10,15):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_4():
        
        
            for i in range(15,20):
                try:
                    t = {}

                    res = ""
                    try:
                        x = r.get(links[s_n[i]], timeout=5)
                    except r.exceptions.Timeout:
                        typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                        continue
                    if x.status_code == 200:
                        res+=f"{s_n[i]} -- busy 3"
                    else:
                        res+=f"{s_n[i]} -- empty 3"
                    typer.secho(res,fg=typer.colors.CYAN)
                except Exception as e:
                    print(repr(e))
    def check_username_5():
    
    
        for i in range(20,25):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))

    def check_username_5():
    
    
        for i in range(20,25):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))                
    def check_username_5():
    
    
        for i in range(20,25):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_5():
    
    
        for i in range(20,25):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_5():
    
    
        for i in range(20,25):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_5():
    
    
        for i in range(20,25):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_6():
    
    
        for i in range(25,30):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_7():
    
    
        for i in range(30,35):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))

    def check_username_8():
    
    
        for i in range(35,40):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_9():
    
    
        for i in range(40,45):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_10():
        for i in range(45,50):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_11():
    
    
        for i in range(50,55):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
    def check_username_12():
    
    
        for i in range(60,63):
            try:
                t = {}

                res = ""
                try:
                    x = r.get(links[s_n[i]], timeout=5)
                except r.exceptions.Timeout:
                    typer.secho(f"Server timed out => {s_n[i]}", fg=typer.colors.RED)
                    continue
                if x.status_code == 200:
                    res+=f"{s_n[i]} -- busy 3"
                else:
                    res+=f"{s_n[i]} -- empty 3"
                typer.secho(res,fg=typer.colors.CYAN)
            except Exception as e:
                print(repr(e))
# check_username_1('sr_red')
# check_username_2('mexroj')

    thread_1 = threading.Thread(target=check_username_1)
    thread_2 = threading.Thread(target=check_username_2)
    thread_3 = threading.Thread(target=check_username_3)
    thread_4 = threading.Thread(target=check_username_4)
    thread_5 = threading.Thread(target=check_username_5)
    thread_6 = threading.Thread(target=check_username_6)
    thread_7 = threading.Thread(target=check_username_7)
    thread_8 = threading.Thread(target=check_username_8)
    thread_9 = threading.Thread(target=check_username_9)
    thread_10 = threading.Thread(target=check_username_10)
    thread_11 = threading.Thread(target=check_username_11)
    thread_12 = threading.Thread(target=check_username_12)

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()
    thread_5.start()
    thread_7.start()
    thread_8.start()
    thread_9.start()
    thread_10.start()
    thread_11.start()
    thread_12.start()


    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    thread_5.join()
    thread_5.join()
    thread_7.join()
    thread_8.join()
    thread_9.join()
    thread_10.join()
    thread_11.join()
    thread_12.join()

main("sr_red")
print("bajarildi")