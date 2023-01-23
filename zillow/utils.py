from http.cookies import SimpleCookie
from urllib.parse import urlparse,parse_qs,urlencode
import json


URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.548696%2C%22east%22%3A-80.139157%2C%22south%22%3A25.550068%2C%22north%22%3A25.855773%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22],%22cat2%22:[%22total%22]}&requestId=2'
COOKIE = 'x-amz-continuous-deployment-state=AYABeFwICvukmGmOI+e+KjrhdcgAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3NjA0OTUxU1JKRU1BTUNBQVQzAAEAAkNEABpDb29raWUAAACAAAAADMYl6P4dISQMYQSrdgAwVWJeyjrGu3Xqg2yfRKi1uJmuNigkxYLjr9V0NUJ32zx0sQixEdbF3635ybrRnDlXAgAAAAAMAAQAAAAAAAAAAAAAAAAAAER+HN%2FNI+tEbI+W%2FtTtXtf%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAw8UeSj4zSLcvkKtyyYxjDYSuUi4k34iXvmeRQo; zguid=24|%24b3cbb4b3-4b0c-4d22-8636-54941d90a59c; _ga=GA1.2.1518914420.1671687713; zjs_user_id=null; zg_anonymous_id=%22ca6ad1f8-2f79-4358-9b8f-83176de26327%22; zjs_anonymous_id=%22b3cbb4b3-4b0c-4d22-8636-54941d90a59c%22; _pxvid=57a0f5e2-81bb-11ed-a1a3-64496a4c744e; _gcl_au=1.1.1135167756.1671687723; __pdst=4bbc1d8f74f54defb606e0e7336bb335; _pin_unauth=dWlkPVpHVTVNRE16T1dRdE1UbGxNaTAwTXpCbExUa3dZV1l0T1RsaU5XRmpPVFl6Wm1OaQ; _cs_c=0; _gid=GA1.2.1756334712.1673992614; _cs_id=9c6068a8-ae4a-a779-c87e-a802435b6636.1673997971.3.1674021706.1674021695.1.1708161971229; G_ENABLED_IDPS=google; _hp2_id.1215457233=%7B%22userId%22%3A%227628230594122341%22%2C%22pageviewId%22%3A%225916150826828886%22%2C%22sessionId%22%3A%221653095882037896%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; JSESSIONID=150A70EABD29C0567990C4D3E1B84A90; zgsession=1|07a9491b-4715-49fe-8825-7d512e793029; _gat=1; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; pxcts=55728e28-97a4-11ed-91fe-665146585968; _pxff_bsco=1; _px3=f3960c2dc9e2653f5ef76a9379797cec97e2a3ab2177b145ef39af161c62493b:zb9Q6z90fAGMCO6Q/hAQfXN4ulyBSWKghcPLnWicP1JsWGyC3974rj2X1y+YoQwotjo8EcwOmpJlSi+vbFjqPw==:1000:T9Osa6CEjiHQIK9/Vg1u8c9cygS0v0zm6MRymW7X0lHKuKUeeQEcmqt42iZWXYs03Z7gpeKaeOPZK6yalNmWGvuDG52RRtPl3ujQ3M72N0q3W1n1pH6BBv0bchCF6nwuZr8acajqpWdQ45YDztAkMUu1+qRJSCblFoTMLusNC2aE17HHsz2LI/BpngO/vy6ags5zP/9mqlWGGqukcWFOTg==; DoubleClickSession=true; AWSALB=mu2oQbPmxvQXPLqNoWDcZOICl5HoF7wFXvLmPJ4Ci8DPumZQbFM8kuCLEZiVZ654s5v3xX7fKFX6Wnd/TibIyYO01H2r+LyaGHccnHfj41YioGELfXICaDQcM2iW; AWSALBCORS=mu2oQbPmxvQXPLqNoWDcZOICl5HoF7wFXvLmPJ4Ci8DPumZQbFM8kuCLEZiVZ654s5v3xX7fKFX6Wnd/TibIyYO01H2r+LyaGHccnHfj41YioGELfXICaDQcM2iW; search=6|1676688768837%7Crect%3D26.02554310763584%252C-79.9209528671875%252C25.379617924545528%252C-80.7669001328125%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0912700%09%09%09%09%09%09; _uetsid=ea4c7a8096b111edbf1397425b5e4c18; _uetvid=5d48af8081bb11edbd4fc772c9401b79; g_state={"i_p":1674701575065,"i_l":3}; _clck=alaekx|1|f8e|0; _clsk=1q31x76|1674096776405|1|0|d.clarity.ms/collect'

def cookie_parser(string_text):
    cookie_string = string_text
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}
    for key,morsel in cookie.items():
        cookies[key] = morsel.value
    
    # print(cookies)
    return cookies

def parse_new_url(url,next_page_number):
    url_parsed = urlparse(url=url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination']= {"currentPage":next_page_number} # this for change the value
    
    # this for access current and update the current seaarchQueryState
    query_string.get('searchQueryState')[0] = search_query_state 
    encoded_qs=urlencode(query_string,doseq=1)
    new_url = f'https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}'
    return new_url
