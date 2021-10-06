import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_versions import V1APIVersions

class CoreApi:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_versions(self) -> V1APIVersions: ...
