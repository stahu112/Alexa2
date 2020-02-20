import requests
import re
import json
from bs4 import BeautifulSoup


headers_Get = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


def get_img_google(q):
    s = requests.Session()
    query = '+'
    for arg in q:
        query += arg + '+'
    url = 'https://www.google.com/search?q=' + query + '&ie=utf-8&oe=utf-8&tbm=isch'

    try:
        r = s.get(url, headers=headers_Get)
    except:
        print("except")
        return 'Google się zesrało'

    soup = BeautifulSoup(r.text, "html.parser")

    search_wrapper = None
    rules = [{'jsname': 'ik8THc'}, {'class': 'rg_meta notranslate'}]

    hack = False

    for rule in rules:
        search_wrapper = soup.findAll('div', rule)
        if len(search_wrapper) != 0:
            break

    if len(search_wrapper) == 0:
        hack = True
        search_wrapper = soup.findAll('script')
        json_text = re.sub("AF_initDataCallback.+{return", "", search_wrapper[-2].text).strip()[:-4]
        search_wrapper = json.loads(json_text)[31][0][12][2]

    url = None

    for result_img in search_wrapper:
        tmp = ""

        if hack:
            if result_img[0] == 2:
                continue
            tmp = result_img[1][3][0]
        else:
            tmp = json.loads(result_img.text.strip())["ou"]

        banned_terms = ["x-raw-image", "lookaside.fbsbx.com", ".svg"]

        if any(term in tmp for term in banned_terms):
            continue
        else:
            url = tmp
            break

    if not url:
        return 'Google się zesrało'

    if "wikimedia" in url and "thumb" in url:
        url = re.sub(r"(.+?)(thumb/)(.+)(/.+)", r"\1\3", url)
    elif "wpimg" in url:
        url = re.sub(r"(.+\/\d+x\d+\/)(.+)", r"https://\2", url)

    result = url

    print(result)

    return result


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
