import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_network_policy import (V1NetworkPolicy,
                                                        V1NetworkPolicyDict)

class V1NetworkPolicyList:
    api_version: typing.Optional[str]
    items: typing.List[V1NetworkPolicy]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1NetworkPolicy],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyListDict: ...

class V1NetworkPolicyListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1NetworkPolicyDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
