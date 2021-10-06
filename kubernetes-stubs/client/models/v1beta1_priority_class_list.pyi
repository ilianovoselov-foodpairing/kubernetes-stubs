import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_priority_class import (
    V1beta1PriorityClass, V1beta1PriorityClassDict)

class V1beta1PriorityClassList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1PriorityClass]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1PriorityClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PriorityClassListDict: ...

class V1beta1PriorityClassListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1PriorityClassDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
