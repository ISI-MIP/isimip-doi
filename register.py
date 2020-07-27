import argparse
import os
from pathlib import Path

from dotenv import load_dotenv

import requests

load_dotenv(Path().cwd() / '.env')

ISIMIP_DATA_URL = os.getenv('ISIMIP_DATA_URL')

DATACITE_METADATA_URL = os.getenv('DATACITE_METADATA_URL')
DATACITE_DOI_URL = os.getenv('DATACITE_DOI_URL')
DATACITE_USERNAME = os.getenv('DATACITE_USERNAME')
DATACITE_PASSWORD = os.getenv('DATACITE_PASSWORD')

parser = argparse.ArgumentParser()
parser.add_argument('doi', help='DOI to register')

args = parser.parse_args()

xml_url = '{base}/{doi}.datacite.xml'.format(base=ISIMIP_DATA_URL, doi=args.doi)
xml_response = requests.get(xml_url)
xml_response.raise_for_status()
xml = xml_response.content

metadata_url = '{base}/{doi}'.format(base=DATACITE_METADATA_URL, doi=args.doi)
metadata_response = requests.put(metadata_url, xml, auth=(DATACITE_USERNAME, DATACITE_PASSWORD))
metadata_response.raise_for_status()

print(metadata_response.content.decode())

doi_string = 'doi={doi}\nurl={base}/{doi}'.format(base=ISIMIP_DATA_URL, doi=args.doi)
doi_url = '{base}/{doi}'.format(base=DATACITE_DOI_URL, doi=args.doi)
doi_response = requests.put(doi_url, doi_string, auth=(DATACITE_USERNAME, DATACITE_PASSWORD))
doi_response.raise_for_status()

print(metadata_response.content.decode())
