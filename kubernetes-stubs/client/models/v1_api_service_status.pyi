import datetime
import typing

import kubernetes.client

class V1APIServiceStatus:
    conditions: typing.Optional[typing.List[kubernetes.client.V1APIServiceCondition]]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            typing.List[kubernetes.client.V1APIServiceCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1APIServiceStatusDict: ...

class V1APIServiceStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[
        typing.List[kubernetes.client.V1APIServiceConditionDict]
    ]
