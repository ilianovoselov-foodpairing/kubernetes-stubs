import datetime
import typing

from kubernetes.client.models.v1_group_version_for_discovery import (
    V1GroupVersionForDiscovery, V1GroupVersionForDiscoveryDict)
from kubernetes.client.models.v1_server_address_by_client_cidr import (
    V1ServerAddressByClientCIDR, V1ServerAddressByClientCIDRDict)

class V1APIGroup:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    name: str
    preferred_version: typing.Optional[V1GroupVersionForDiscovery]
    server_address_by_client_cid_rs: typing.Optional[
        typing.List[V1ServerAddressByClientCIDR]
    ]
    versions: typing.List[V1GroupVersionForDiscovery]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        name: str,
        preferred_version: typing.Optional[V1GroupVersionForDiscovery] = ...,
        server_address_by_client_cid_rs: typing.Optional[
            typing.List[V1ServerAddressByClientCIDR]
        ] = ...,
        versions: typing.List[V1GroupVersionForDiscovery]
    ) -> None: ...
    def to_dict(self) -> V1APIGroupDict: ...

class V1APIGroupDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    name: str
    preferredVersion: typing.Optional[V1GroupVersionForDiscoveryDict]
    serverAddressByClientCIDRs: typing.Optional[
        typing.List[V1ServerAddressByClientCIDRDict]
    ]
    versions: typing.List[V1GroupVersionForDiscoveryDict]
