import datetime
import typing

import kubernetes.client

class V1ContainerImage:
    names: typing.List[str]
    size_bytes: typing.Optional[int]
    def __init__(
        self, *, names: typing.List[str], size_bytes: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1ContainerImageDict: ...

class V1ContainerImageDict(typing.TypedDict, total=False):
    names: typing.List[str]
    sizeBytes: typing.Optional[int]
