import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_group import V1APIGroup

class SettingsApi:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_group(self) -> V1APIGroup: ...
