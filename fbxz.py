import requests
from bs4 import BeautifulSoup

def getFbxz(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'pt-BR,pt;q=0.9',
        # 'cookie': 'S=spreadsheet_forms=fupw6KcOpdBwVUE-cdZ4HsH13sCkbHMib7Zidu8MLyk; COMPASS=spreadsheet_forms=CjIACWuJV1RIKB_yPf9CO5vZ7UB6R-9sHcXmrxVhkpMH_NoDa7TRM3RQYwWN__qyzMnnxRC0zPuvBhpDAAlriVdFibwagi8kBxYA54UHD_smAfwRddsq3Co1n5L5PyyEM6qxnSVBu9r8d7tGVIZIPgJeh86WawAlkzu0AwMuUA==; NID=512=IMRV5M88ADGbgBGmdr_liuvKOD8bFr2xwXTY08hMEFzndXE-phO-7alFpa1qxqloXKMOJGT4mgy3CGdMxvcbmmbRVX3VpSLgqBgYyF0ssJzlcjZy6JjIaf_r3Gw42qh9zgKy-Z60XWjQTDPZCNc_kyUm5G0B_JEvd9nDq96fpwk',
        'dnt': '1',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    response = requests.get(
        url+'/viewform',
        headers=headers,
    )

    html_response = response.content

    # Parse the HTML
    soup = BeautifulSoup(html_response, 'html.parser')

    # Encontre o elemento input
    input_element = soup.find('input', {'name': 'fbzx'})

    # Verifique se o elemento foi encontrado e obtenha o valor
    if input_element:
        value = input_element.get('value')
        print("Valor do atributo 'value':", value)
        return value
    else:
        print("Elemento não encontrado.")
        return False