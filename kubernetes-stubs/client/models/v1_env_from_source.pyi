import datetime
import typing

from kubernetes.client.models.v1_config_map_env_source import (
    V1ConfigMapEnvSource, V1ConfigMapEnvSourceDict)
from kubernetes.client.models.v1_secret_env_source import (
    V1SecretEnvSource, V1SecretEnvSourceDict)

class V1EnvFromSource:
    config_map_ref: typing.Optional[V1ConfigMapEnvSource]
    prefix: typing.Optional[str]
    secret_ref: typing.Optional[V1SecretEnvSource]
    def __init__(
        self,
        *,
        config_map_ref: typing.Optional[V1ConfigMapEnvSource] = ...,
        prefix: typing.Optional[str] = ...,
        secret_ref: typing.Optional[V1SecretEnvSource] = ...
    ) -> None: ...
    def to_dict(self) -> V1EnvFromSourceDict: ...

class V1EnvFromSourceDict(typing.TypedDict, total=False):
    configMapRef: typing.Optional[V1ConfigMapEnvSourceDict]
    prefix: typing.Optional[str]
    secretRef: typing.Optional[V1SecretEnvSourceDict]
