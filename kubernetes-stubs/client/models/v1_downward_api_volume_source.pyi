import datetime
import typing

from kubernetes.client.models.v1_downward_api_volume_file import (
    V1DownwardAPIVolumeFile, V1DownwardAPIVolumeFileDict)

class V1DownwardAPIVolumeSource:
    default_mode: typing.Optional[int]
    items: typing.Optional[typing.List[V1DownwardAPIVolumeFile]]
    def __init__(
        self,
        *,
        default_mode: typing.Optional[int] = ...,
        items: typing.Optional[typing.List[V1DownwardAPIVolumeFile]] = ...
    ) -> None: ...
    def to_dict(self) -> V1DownwardAPIVolumeSourceDict: ...

class V1DownwardAPIVolumeSourceDict(typing.TypedDict, total=False):
    defaultMode: typing.Optional[int]
    items: typing.Optional[typing.List[V1DownwardAPIVolumeFileDict]]
