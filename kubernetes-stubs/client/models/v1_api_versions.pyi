import datetime
import typing

from kubernetes.client.models.v1_server_address_by_client_cidr import (
    V1ServerAddressByClientCIDR, V1ServerAddressByClientCIDRDict)

class V1APIVersions:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    server_address_by_client_cid_rs: typing.List[V1ServerAddressByClientCIDR]
    versions: typing.List[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        server_address_by_client_cid_rs: typing.List[V1ServerAddressByClientCIDR],
        versions: typing.List[str]
    ) -> None: ...
    def to_dict(self) -> V1APIVersionsDict: ...

class V1APIVersionsDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    serverAddressByClientCIDRs: typing.List[V1ServerAddressByClientCIDRDict]
    versions: typing.List[str]
