import datetime
import typing

from kubernetes.client.models.v1_secret_reference import (
    V1SecretReference, V1SecretReferenceDict)

class V1RBDPersistentVolumeSource:
    fs_type: typing.Optional[str]
    image: str
    keyring: typing.Optional[str]
    monitors: typing.List[str]
    pool: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[V1SecretReference]
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
        secret_ref: typing.Optional[V1SecretReference] = ...,
        user: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1RBDPersistentVolumeSourceDict: ...

class V1RBDPersistentVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    image: str
    keyring: typing.Optional[str]
    monitors: typing.List[str]
    pool: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[V1SecretReferenceDict]
    user: typing.Optional[str]
