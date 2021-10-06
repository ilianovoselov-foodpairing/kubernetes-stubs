import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1_persistent_volume_claim import (
    V1PersistentVolumeClaim, V1PersistentVolumeClaimDict)

class V1PersistentVolumeClaimList:
    api_version: typing.Optional[str]
    items: typing.List[V1PersistentVolumeClaim]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1PersistentVolumeClaim],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeClaimListDict: ...

class V1PersistentVolumeClaimListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1PersistentVolumeClaimDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
