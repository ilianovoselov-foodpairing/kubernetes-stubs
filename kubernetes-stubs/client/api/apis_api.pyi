import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_group_list import V1APIGroupList

class ApisApi:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_versions(self) -> V1APIGroupList: ...
