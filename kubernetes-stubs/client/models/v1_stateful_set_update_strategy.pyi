import datetime
import typing

from kubernetes.client.models.v1_rolling_update_stateful_set_strategy import (
    V1RollingUpdateStatefulSetStrategy, V1RollingUpdateStatefulSetStrategyDict)

class V1StatefulSetUpdateStrategy:
    rolling_update: typing.Optional[V1RollingUpdateStatefulSetStrategy]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[V1RollingUpdateStatefulSetStrategy] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1StatefulSetUpdateStrategyDict: ...

class V1StatefulSetUpdateStrategyDict(typing.TypedDict, total=False):
    rollingUpdate: typing.Optional[V1RollingUpdateStatefulSetStrategyDict]
    type: typing.Optional[str]
