import datetime
import typing

from kubernetes.client.models.v1_network_policy_spec import (
    V1NetworkPolicySpec, V1NetworkPolicySpecDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1NetworkPolicy:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1NetworkPolicySpec]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1NetworkPolicySpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyDict: ...

class V1NetworkPolicyDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1NetworkPolicySpecDict]
