import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_priority_class import (
    V1alpha1PriorityClass, V1alpha1PriorityClassDict)

class V1alpha1PriorityClassList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1PriorityClass]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1PriorityClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PriorityClassListDict: ...

class V1alpha1PriorityClassListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1PriorityClassDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
