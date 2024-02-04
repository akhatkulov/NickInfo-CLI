import requests as r
import typer


def check_username(a):
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
    
    for i in range(len(s_n)):
        try:
            t = {}

            res = ""
            x = r.get(links[s_n[i]])
            if x.status_code == 200:
                res+=f"{s_n[i]} -- ✅"
            else:
                res+=f"{s_n[i]} -- ❌"
            typer.secho(res,fg=typer.colors.CYAN)
        except:
            pass


