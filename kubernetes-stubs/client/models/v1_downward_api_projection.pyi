import datetime
import typing

from kubernetes.client.models.v1_downward_api_volume_file import (
    V1DownwardAPIVolumeFile, V1DownwardAPIVolumeFileDict)

class V1DownwardAPIProjection:
    items: typing.Optional[typing.List[V1DownwardAPIVolumeFile]]
    def __init__(
        self, *, items: typing.Optional[typing.List[V1DownwardAPIVolumeFile]] = ...
    ) -> None: ...
    def to_dict(self) -> V1DownwardAPIProjectionDict: ...

class V1DownwardAPIProjectionDict(typing.TypedDict, total=False):
    items: typing.Optional[typing.List[V1DownwardAPIVolumeFileDict]]
