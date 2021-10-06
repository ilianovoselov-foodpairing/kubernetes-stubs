import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.version_info import VersionInfo

class VersionApi:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_code(self) -> VersionInfo: ...
