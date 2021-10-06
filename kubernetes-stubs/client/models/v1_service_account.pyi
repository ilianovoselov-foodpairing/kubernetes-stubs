import datetime
import typing

from kubernetes.client.models.v1_local_object_reference import (
    V1LocalObjectReference, V1LocalObjectReferenceDict)
from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1_object_reference import (
    V1ObjectReference, V1ObjectReferenceDict)

class V1ServiceAccount:
    api_version: typing.Optional[str]
    automount_service_account_token: typing.Optional[bool]
    image_pull_secrets: typing.Optional[typing.List[V1LocalObjectReference]]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    secrets: typing.Optional[typing.List[V1ObjectReference]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        automount_service_account_token: typing.Optional[bool] = ...,
        image_pull_secrets: typing.Optional[typing.List[V1LocalObjectReference]] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        secrets: typing.Optional[typing.List[V1ObjectReference]] = ...
    ) -> None: ...
    def to_dict(self) -> V1ServiceAccountDict: ...

class V1ServiceAccountDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    automountServiceAccountToken: typing.Optional[bool]
    imagePullSecrets: typing.Optional[typing.List[V1LocalObjectReferenceDict]]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    secrets: typing.Optional[typing.List[V1ObjectReferenceDict]]
