import datetime
import typing

import kubernetes.client

class V1LimitRangeSpec:
    limits: typing.List[kubernetes.client.V1LimitRangeItem]
    def __init__(
        self, *, limits: typing.List[kubernetes.client.V1LimitRangeItem]
    ) -> None: ...
    def to_dict(self) -> V1LimitRangeSpecDict: ...

class V1LimitRangeSpecDict(typing.TypedDict, total=False):
    limits: typing.List[kubernetes.client.V1LimitRangeItemDict]
