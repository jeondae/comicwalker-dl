import argparse
import coloredlogs
import json
import logging
import os
import requests
import sys

from binascii import unhexlify

os.system('cls||clear')

print('COMICWALKER-DL\n')

coloredlogs.install(fmt='%(asctime)s,%(msecs)03d - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser()
parser.add_argument('-cid', help='content id, &cid={...}. see url when reading a chapter')
parser.add_argument('-nolog', help='no progressive download logs on terminal', action="store_true")
args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

if args.cid == None:
    parser.print_help()
    sys.exit()

def start(url, headers):
    meta = json.loads(requests.get(url=url, headers=headers).content)
    img_url = f'{url}/frames?enable_webp=true'

    try:
        cid_info = {
            "TITLE": meta['data']['extra']['content']['title'],
            "CHAPTER": meta['data']['result']['title']
        }

    except KeyError:
        logging.error("Metadata malformed, check CID's validity")
        sys.exit()

    else:
        print('{} - {}'.format(cid_info['TITLE'], cid_info['CHAPTER']))

        undrm(img_url, headers, cid_info)

def undrm(url, headers, cid_info):
    meta = json.loads(requests.get(url=url, headers=headers).content)

    print('Page count: {}\n'.format(len(meta['data']['result'])))

    save_path = os.path.join('downloaded_chapters\\{}\\{}'.format(cid_info['TITLE'], cid_info['CHAPTER']))

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    print(f'Saving chapter to {save_path}\n')

    for page in range(1, len(meta['data']['result']) + 1):

        if args.nolog:
            if page == 1:
                logging.info('DL in progress...')
        else:
            logging.info('Progress: page ' + str(page))

        key = unhexlify(meta['data']['result'][page-1]['meta']['drm_hash'][:16])
        enc = requests.get(meta['data']['result'][page-1]['meta']['source_url'], headers=headers).content
        pagination = str(page) + '.webp'

        with open(f'{save_path}\\{pagination}', 'wb') as f:
            f.write(xor(enc, key))
    
    logging.info('Done.')

def xor(bin, key):
    retval = []
    
    for i in range(len(bin)):
        retval.append(bin[i] ^ key[i % len(key)])
    
    return bytes(retval)

def main():

    headers = {
        'authority': 'comicwalker-api.nicomanga.jp',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://comic-walker.com',
        'pragma': 'no-cache',
        'referer': 'https://comic-walker.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-Blowfisht': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    }

    content_url = f'https://comicwalker-api.nicomanga.jp/api/v1/comicwalker/episodes/{args.cid}'
    
    start(content_url, headers)

if __name__ == "__main__":
    main()