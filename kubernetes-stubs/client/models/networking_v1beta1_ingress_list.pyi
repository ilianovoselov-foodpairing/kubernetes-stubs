import datetime
import typing

from kubernetes.client.models.networking_v1beta1_ingress import (
    NetworkingV1beta1Ingress, NetworkingV1beta1IngressDict)
from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict

class NetworkingV1beta1IngressList:
    api_version: typing.Optional[str]
    items: typing.List[NetworkingV1beta1Ingress]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[NetworkingV1beta1Ingress],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> NetworkingV1beta1IngressListDict: ...

class NetworkingV1beta1IngressListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[NetworkingV1beta1IngressDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
