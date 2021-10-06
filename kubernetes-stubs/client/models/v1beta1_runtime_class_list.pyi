import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_runtime_class import (
    V1beta1RuntimeClass, V1beta1RuntimeClassDict)

class V1beta1RuntimeClassList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1RuntimeClass]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1RuntimeClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1RuntimeClassListDict: ...

class V1beta1RuntimeClassListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1RuntimeClassDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
