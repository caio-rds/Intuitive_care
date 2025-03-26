import requests
from bs4 import BeautifulSoup
import zipfile
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

target_url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

target_res = requests.get(target_url)
logging.info('Requesting the page...')
target_res.raise_for_status()
logging.info('Page requested successfully.')
soup = BeautifulSoup(target_res.content, 'html.parser')
logging.info('Page content parsed successfully.')
attachments = soup.find_all('a', string=['Anexo I.', 'Anexo II.'])
logging.info('Found the links to the attachments.')

with zipfile.ZipFile('../../media/attachments.zip', 'w') as zipf:
    for link in attachments:
        url = link['href']
        name = f'{link.string}pdf'
        file_response = requests.get(url)
        logging.info(f'Downloading {name}...')
        file_response.raise_for_status()
        logging.info(f'{name} downloaded successfully.')

        with open(name, 'wb') as file:
            file.write(file_response.content)

        zipf.write(name)
        os.remove(name)
        logging.info(f'{name} added to ZIP successfully')


    logging.info('All files downloaded and added to the ZIP successfully.')