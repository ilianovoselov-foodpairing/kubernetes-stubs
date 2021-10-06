import datetime
import typing

from kubernetes.client.models.v1_local_object_reference import (
    V1LocalObjectReference, V1LocalObjectReferenceDict)

class V1FlexVolumeSource:
    driver: str
    fs_type: typing.Optional[str]
    options: typing.Optional[typing.Dict[str, str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[V1LocalObjectReference]
    def __init__(
        self,
        *,
        driver: str,
        fs_type: typing.Optional[str] = ...,
        options: typing.Optional[typing.Dict[str, str]] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[V1LocalObjectReference] = ...
    ) -> None: ...
    def to_dict(self) -> V1FlexVolumeSourceDict: ...

class V1FlexVolumeSourceDict(typing.TypedDict, total=False):
    driver: str
    fsType: typing.Optional[str]
    options: typing.Optional[typing.Dict[str, str]]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[V1LocalObjectReferenceDict]
