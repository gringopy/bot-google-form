import time
from fbxz import *
import requests
from bs4 import BeautifulSoup

url= 'https://docs.google.com/forms/d/e/1FAIpQLSd6FZvuqy5l7kAlUzctjRYMgVpYW5DfE-S1gt0iAPZ2msQglg'
wallet = '0x22621Cd9eDe0De0d41Dbe4aaE0420CeAfbcb36f1'


fxbz = getFbxz(url)
epoch_timestamp_ms = str(int(time.time() * 1000))
print(epoch_timestamp_ms)

def submit(url, wallet):

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'pt-BR,pt;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'S=spreadsheet_forms=fupw6KcOpdBwVUE-cdZ4HsH13sCkbHMib7Zidu8MLyk; COMPASS=spreadsheet_forms=CjIACWuJV1RIKB_yPf9CO5vZ7UB6R-9sHcXmrxVhkpMH_NoDa7TRM3RQYwWN__qyzMnnxRCTy_uvBhpDAAlriVdFibwagi8kBxYA54UHD_smAfwRddsq3Co1n5L5PyyEM6qxnSVBu9r8d7tGVIZIPgJeh86WawAlkzu0AwMuUA==; NID=512=Sxm9eRvWZYxusx2xPmww5nDiCAgeoxbaOcEXCbt7W5i7eezGmtmssyuE6Zx5qxC-VYUWX9B5nffdnSiULp-hx4LfBn7J_Ebc91CdCvOynclhdRkyBmL_gcY9jIJz0pOJ1E-D43LXzHQq8IYAJ2JC4FNApu8Mqbvjrbj5EWGnw8U',
        'dnt': '1',
        'origin': 'https://docs.google.com',
        'referer': f'{url}?fbzx={fxbz}',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.58", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.58"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    data = {
        'entry.453185958': wallet,
        'entry.1519260996': '✔️',
        'entry.669185745': '✔️',
        'entry.555121015': '✔️',
        'entry.1519260996_sentinel': '',
        'entry.669185745_sentinel': '',
        'entry.555121015_sentinel': '',
        'fvv': '1',
        'partialResponse': f'[null,null,"{fxbz}"]',
        'pageHistory': '0',
        'fbzx': fxbz,
        'submissionTimestamp': epoch_timestamp_ms,
    }
    #print(data)
    response = requests.post(
        url+'/formResponse',
        headers=headers,
        data=data,
        allow_redirects=True
    )
    print(response.status_code)

    html_response = response.content

    soup = BeautifulSoup(html_response, 'html.parser')

    input_element = soup.find('div', {'class': 'vHW8K'})
    if input_element:
        content  = input_element.text
        print(content)
        return content
    else:
        print("Elemento não encontrado.")
        return False
submit(url, wallet)