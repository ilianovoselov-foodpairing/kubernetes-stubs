import datetime
import typing

from kubernetes.client.models.v1_local_object_reference import (
    V1LocalObjectReference, V1LocalObjectReferenceDict)

class V1CephFSVolumeSource:
    monitors: typing.List[str]
    path: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_file: typing.Optional[str]
    secret_ref: typing.Optional[V1LocalObjectReference]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        monitors: typing.List[str],
        path: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_file: typing.Optional[str] = ...,
        secret_ref: typing.Optional[V1LocalObjectReference] = ...,
        user: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1CephFSVolumeSourceDict: ...

class V1CephFSVolumeSourceDict(typing.TypedDict, total=False):
    monitors: typing.List[str]
    path: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretFile: typing.Optional[str]
    secretRef: typing.Optional[V1LocalObjectReferenceDict]
    user: typing.Optional[str]
