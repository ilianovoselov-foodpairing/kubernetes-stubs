import datetime
import typing

from kubernetes.client.models.v1_secret_reference import (
    V1SecretReference, V1SecretReferenceDict)

class V1CephFSPersistentVolumeSource:
    monitors: typing.List[str]
    path: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_file: typing.Optional[str]
    secret_ref: typing.Optional[V1SecretReference]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        monitors: typing.List[str],
        path: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_file: typing.Optional[str] = ...,
        secret_ref: typing.Optional[V1SecretReference] = ...,
        user: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1CephFSPersistentVolumeSourceDict: ...

class V1CephFSPersistentVolumeSourceDict(typing.TypedDict, total=False):
    monitors: typing.List[str]
    path: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretFile: typing.Optional[str]
    secretRef: typing.Optional[V1SecretReferenceDict]
    user: typing.Optional[str]
