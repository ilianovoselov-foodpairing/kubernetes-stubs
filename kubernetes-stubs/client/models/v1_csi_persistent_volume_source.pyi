import datetime
import typing

from kubernetes.client.models.v1_secret_reference import (
    V1SecretReference, V1SecretReferenceDict)

class V1CSIPersistentVolumeSource:
    controller_expand_secret_ref: typing.Optional[V1SecretReference]
    controller_publish_secret_ref: typing.Optional[V1SecretReference]
    driver: str
    fs_type: typing.Optional[str]
    node_publish_secret_ref: typing.Optional[V1SecretReference]
    node_stage_secret_ref: typing.Optional[V1SecretReference]
    read_only: typing.Optional[bool]
    volume_attributes: typing.Optional[typing.Dict[str, str]]
    volume_handle: str
    def __init__(
        self,
        *,
        controller_expand_secret_ref: typing.Optional[V1SecretReference] = ...,
        controller_publish_secret_ref: typing.Optional[V1SecretReference] = ...,
        driver: str,
        fs_type: typing.Optional[str] = ...,
        node_publish_secret_ref: typing.Optional[V1SecretReference] = ...,
        node_stage_secret_ref: typing.Optional[V1SecretReference] = ...,
        read_only: typing.Optional[bool] = ...,
        volume_attributes: typing.Optional[typing.Dict[str, str]] = ...,
        volume_handle: str
    ) -> None: ...
    def to_dict(self) -> V1CSIPersistentVolumeSourceDict: ...

class V1CSIPersistentVolumeSourceDict(typing.TypedDict, total=False):
    controllerExpandSecretRef: typing.Optional[V1SecretReferenceDict]
    controllerPublishSecretRef: typing.Optional[V1SecretReferenceDict]
    driver: str
    fsType: typing.Optional[str]
    nodePublishSecretRef: typing.Optional[V1SecretReferenceDict]
    nodeStageSecretRef: typing.Optional[V1SecretReferenceDict]
    readOnly: typing.Optional[bool]
    volumeAttributes: typing.Optional[typing.Dict[str, str]]
    volumeHandle: str
