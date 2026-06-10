import json
from urllib.request import urlopen

from django.conf import settings

from django_vite.core.asset_loader import DjangoViteAppClient, ManifestClient


class IsimipDataManifestClient(ManifestClient):
    def load_manifest(self):
        with urlopen(settings.ISIMIP_DATA_MANIFEST_URL, timeout=2) as response:
            return json.loads(response.read())


class IsimipDataViteAppClient(DjangoViteAppClient):
    ManifestClient = IsimipDataManifestClient

    def get_production_server_url(self, path: str) -> str:
        return f'{settings.ISIMIP_DATA_STATIC_URL}{path}'
