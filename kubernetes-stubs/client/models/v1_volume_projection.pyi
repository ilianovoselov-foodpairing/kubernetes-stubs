import datetime
import typing

from kubernetes.client.models.v1_config_map_projection import (
    V1ConfigMapProjection, V1ConfigMapProjectionDict)
from kubernetes.client.models.v1_downward_api_projection import (
    V1DownwardAPIProjection, V1DownwardAPIProjectionDict)
from kubernetes.client.models.v1_secret_projection import (
    V1SecretProjection, V1SecretProjectionDict)
from kubernetes.client.models.v1_service_account_token_projection import (
    V1ServiceAccountTokenProjection, V1ServiceAccountTokenProjectionDict)

class V1VolumeProjection:
    config_map: typing.Optional[V1ConfigMapProjection]
    downward_api: typing.Optional[V1DownwardAPIProjection]
    secret: typing.Optional[V1SecretProjection]
    service_account_token: typing.Optional[V1ServiceAccountTokenProjection]
    def __init__(
        self,
        *,
        config_map: typing.Optional[V1ConfigMapProjection] = ...,
        downward_api: typing.Optional[V1DownwardAPIProjection] = ...,
        secret: typing.Optional[V1SecretProjection] = ...,
        service_account_token: typing.Optional[V1ServiceAccountTokenProjection] = ...
    ) -> None: ...
    def to_dict(self) -> V1VolumeProjectionDict: ...

class V1VolumeProjectionDict(typing.TypedDict, total=False):
    configMap: typing.Optional[V1ConfigMapProjectionDict]
    downwardAPI: typing.Optional[V1DownwardAPIProjectionDict]
    secret: typing.Optional[V1SecretProjectionDict]
    serviceAccountToken: typing.Optional[V1ServiceAccountTokenProjectionDict]
