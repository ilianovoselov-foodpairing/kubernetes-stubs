import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_policy_rule import (V1PolicyRule,
                                                     V1PolicyRuleDict)

class V1Role:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    rules: typing.Optional[typing.List[V1PolicyRule]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        rules: typing.Optional[typing.List[V1PolicyRule]] = ...
    ) -> None: ...
    def to_dict(self) -> V1RoleDict: ...

class V1RoleDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    rules: typing.Optional[typing.List[V1PolicyRuleDict]]
