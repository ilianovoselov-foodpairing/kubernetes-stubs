import datetime
import typing

from kubernetes.client.models.v1_local_object_reference import (
    V1LocalObjectReference, V1LocalObjectReferenceDict)

class V1CSIVolumeSource:
    driver: str
    fs_type: typing.Optional[str]
    node_publish_secret_ref: typing.Optional[V1LocalObjectReference]
    read_only: typing.Optional[bool]
    volume_attributes: typing.Optional[typing.Dict[str, str]]
    def __init__(
        self,
        *,
        driver: str,
        fs_type: typing.Optional[str] = ...,
        node_publish_secret_ref: typing.Optional[V1LocalObjectReference] = ...,
        read_only: typing.Optional[bool] = ...,
        volume_attributes: typing.Optional[typing.Dict[str, str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1CSIVolumeSourceDict: ...

class V1CSIVolumeSourceDict(typing.TypedDict, total=False):
    driver: str
    fsType: typing.Optional[str]
    nodePublishSecretRef: typing.Optional[V1LocalObjectReferenceDict]
    readOnly: typing.Optional[bool]
    volumeAttributes: typing.Optional[typing.Dict[str, str]]
