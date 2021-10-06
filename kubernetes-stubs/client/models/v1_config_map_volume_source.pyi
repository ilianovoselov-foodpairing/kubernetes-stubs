import datetime
import typing

from kubernetes.client.models.v1_key_to_path import (V1KeyToPath,
                                                     V1KeyToPathDict)

class V1ConfigMapVolumeSource:
    default_mode: typing.Optional[int]
    items: typing.Optional[typing.List[V1KeyToPath]]
    name: typing.Optional[str]
    optional: typing.Optional[bool]
    def __init__(
        self,
        *,
        default_mode: typing.Optional[int] = ...,
        items: typing.Optional[typing.List[V1KeyToPath]] = ...,
        name: typing.Optional[str] = ...,
        optional: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> V1ConfigMapVolumeSourceDict: ...

class V1ConfigMapVolumeSourceDict(typing.TypedDict, total=False):
    defaultMode: typing.Optional[int]
    items: typing.Optional[typing.List[V1KeyToPathDict]]
    name: typing.Optional[str]
    optional: typing.Optional[bool]
