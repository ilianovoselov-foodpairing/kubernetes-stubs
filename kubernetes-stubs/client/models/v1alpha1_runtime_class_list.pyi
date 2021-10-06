import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1alpha1_runtime_class import (
    V1alpha1RuntimeClass, V1alpha1RuntimeClassDict)

class V1alpha1RuntimeClassList:
    api_version: typing.Optional[str]
    items: typing.List[V1alpha1RuntimeClass]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1alpha1RuntimeClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1RuntimeClassListDict: ...

class V1alpha1RuntimeClassListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1alpha1RuntimeClassDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
