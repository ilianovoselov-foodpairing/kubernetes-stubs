import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_persistent_volume import (
    V1PersistentVolume, V1PersistentVolumeDict)

class V1PersistentVolumeList:
    api_version: typing.Optional[str]
    items: typing.List[V1PersistentVolume]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1PersistentVolume],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeListDict: ...

class V1PersistentVolumeListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1PersistentVolumeDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
