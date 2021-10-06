import datetime
import typing

from kubernetes.client.models.v1_env_var_source import (V1EnvVarSource,
                                                        V1EnvVarSourceDict)

class V1EnvVar:
    name: str
    value: typing.Optional[str]
    value_from: typing.Optional[V1EnvVarSource]
    def __init__(
        self,
        *,
        name: str,
        value: typing.Optional[str] = ...,
        value_from: typing.Optional[V1EnvVarSource] = ...
    ) -> None: ...
    def to_dict(self) -> V1EnvVarDict: ...

class V1EnvVarDict(typing.TypedDict, total=False):
    name: str
    value: typing.Optional[str]
    valueFrom: typing.Optional[V1EnvVarSourceDict]
