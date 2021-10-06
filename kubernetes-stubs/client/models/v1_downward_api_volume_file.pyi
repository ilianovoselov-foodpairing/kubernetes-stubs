import datetime
import typing

from kubernetes.client.models.v1_object_field_selector import (
    V1ObjectFieldSelector, V1ObjectFieldSelectorDict)
from kubernetes.client.models.v1_resource_field_selector import (
    V1ResourceFieldSelector, V1ResourceFieldSelectorDict)

class V1DownwardAPIVolumeFile:
    field_ref: typing.Optional[V1ObjectFieldSelector]
    mode: typing.Optional[int]
    path: str
    resource_field_ref: typing.Optional[V1ResourceFieldSelector]
    def __init__(
        self,
        *,
        field_ref: typing.Optional[V1ObjectFieldSelector] = ...,
        mode: typing.Optional[int] = ...,
        path: str,
        resource_field_ref: typing.Optional[V1ResourceFieldSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V1DownwardAPIVolumeFileDict: ...

class V1DownwardAPIVolumeFileDict(typing.TypedDict, total=False):
    fieldRef: typing.Optional[V1ObjectFieldSelectorDict]
    mode: typing.Optional[int]
    path: str
    resourceFieldRef: typing.Optional[V1ResourceFieldSelectorDict]
