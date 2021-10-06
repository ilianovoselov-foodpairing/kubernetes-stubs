import datetime
import typing

import kubernetes.client

class V1ResourceRequirements:
    limits: typing.Optional[typing.Dict[str, str]]
    requests: typing.Optional[typing.Dict[str, str]]
    def __init__(
        self,
        *,
        limits: typing.Optional[typing.Dict[str, str]] = ...,
        requests: typing.Optional[typing.Dict[str, str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1ResourceRequirementsDict: ...

class V1ResourceRequirementsDict(typing.TypedDict, total=False):
    limits: typing.Optional[typing.Dict[str, str]]
    requests: typing.Optional[typing.Dict[str, str]]
