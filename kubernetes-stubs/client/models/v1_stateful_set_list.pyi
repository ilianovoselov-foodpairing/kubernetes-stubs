import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_stateful_set import (V1StatefulSet,
                                                      V1StatefulSetDict)

class V1StatefulSetList:
    api_version: typing.Optional[str]
    items: typing.List[V1StatefulSet]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1StatefulSet],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1StatefulSetListDict: ...

class V1StatefulSetListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1StatefulSetDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
