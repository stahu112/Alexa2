import requests
import re


headers_Get = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


def get_yt(q):
    s = requests.Session()
    query = '+'
    for arg in q:
        query += arg + '+'

    query = query[:-1]
    url = 'https://www.youtube.com/results?search_query=' + query

    try:
        r = s.get(url, headers=headers_Get)
    except:
        return "Jutub się zesrał"

    regex = r'\\\"videoId\\\"\:\\\"(\S+?)\\\"'
    ret = re.search(regex, r.text)

    if ret is None:
        regex = r'\"videoId\"\:\"(\S+?)\"'
        ret = re.search(regex, r.text)

    if ret is not None:
        result = 'https://www.youtube.com/watch?v=' + ret.groups()[0]
    else:
        return "Brak wyników"

    return result
