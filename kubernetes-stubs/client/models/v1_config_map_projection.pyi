import datetime
import typing

from kubernetes.client.models.v1_key_to_path import (V1KeyToPath,
                                                     V1KeyToPathDict)

class V1ConfigMapProjection:
    items: typing.Optional[typing.List[V1KeyToPath]]
    name: typing.Optional[str]
    optional: typing.Optional[bool]
    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[V1KeyToPath]] = ...,
        name: typing.Optional[str] = ...,
        optional: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> V1ConfigMapProjectionDict: ...

class V1ConfigMapProjectionDict(typing.TypedDict, total=False):
    items: typing.Optional[typing.List[V1KeyToPathDict]]
    name: typing.Optional[str]
    optional: typing.Optional[bool]
