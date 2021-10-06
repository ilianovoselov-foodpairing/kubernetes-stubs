import datetime
import typing

from kubernetes.client.models.v1_key_to_path import (V1KeyToPath,
                                                     V1KeyToPathDict)

class V1SecretVolumeSource:
    default_mode: typing.Optional[int]
    items: typing.Optional[typing.List[V1KeyToPath]]
    optional: typing.Optional[bool]
    secret_name: typing.Optional[str]
    def __init__(
        self,
        *,
        default_mode: typing.Optional[int] = ...,
        items: typing.Optional[typing.List[V1KeyToPath]] = ...,
        optional: typing.Optional[bool] = ...,
        secret_name: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1SecretVolumeSourceDict: ...

class V1SecretVolumeSourceDict(typing.TypedDict, total=False):
    defaultMode: typing.Optional[int]
    items: typing.Optional[typing.List[V1KeyToPathDict]]
    optional: typing.Optional[bool]
    secretName: typing.Optional[str]
