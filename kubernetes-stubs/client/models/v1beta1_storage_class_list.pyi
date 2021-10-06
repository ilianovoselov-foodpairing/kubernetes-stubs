import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_storage_class import (
    V1beta1StorageClass, V1beta1StorageClassDict)

class V1beta1StorageClassList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1StorageClass]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1StorageClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1StorageClassListDict: ...

class V1beta1StorageClassListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1StorageClassDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
