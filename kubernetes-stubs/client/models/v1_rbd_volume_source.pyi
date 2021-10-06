import datetime
import typing

from kubernetes.client.models.v1_local_object_reference import (
    V1LocalObjectReference, V1LocalObjectReferenceDict)

class V1RBDVolumeSource:
    fs_type: typing.Optional[str]
    image: str
    keyring: typing.Optional[str]
    monitors: typing.List[str]
    pool: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[V1LocalObjectReference]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        image: str,
        keyring: typing.Optional[str] = ...,
        monitors: typing.List[str],
        pool: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[V1LocalObjectReference] = ...,
        user: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1RBDVolumeSourceDict: ...

class V1RBDVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    image: str
    keyring: typing.Optional[str]
    monitors: typing.List[str]
    pool: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[V1LocalObjectReferenceDict]
    user: typing.Optional[str]
