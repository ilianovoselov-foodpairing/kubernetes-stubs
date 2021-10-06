import datetime
import typing

from kubernetes.client.models.v1_api_group import V1APIGroup, V1APIGroupDict

class V1APIGroupList:
    api_version: typing.Optional[str]
    groups: typing.List[V1APIGroup]
    kind: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        groups: typing.List[V1APIGroup],
        kind: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1APIGroupListDict: ...

class V1APIGroupListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    groups: typing.List[V1APIGroupDict]
    kind: typing.Optional[str]
