import datetime
import typing

from kubernetes.client.models.v1_secret_reference import (
    V1SecretReference, V1SecretReferenceDict)

class V1FlexPersistentVolumeSource:
    driver: str
    fs_type: typing.Optional[str]
    options: typing.Optional[typing.Dict[str, str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[V1SecretReference]
    def __init__(
        self,
        *,
        driver: str,
        fs_type: typing.Optional[str] = ...,
        options: typing.Optional[typing.Dict[str, str]] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[V1SecretReference] = ...
    ) -> None: ...
    def to_dict(self) -> V1FlexPersistentVolumeSourceDict: ...

class V1FlexPersistentVolumeSourceDict(typing.TypedDict, total=False):
    driver: str
    fsType: typing.Optional[str]
    options: typing.Optional[typing.Dict[str, str]]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[V1SecretReferenceDict]
