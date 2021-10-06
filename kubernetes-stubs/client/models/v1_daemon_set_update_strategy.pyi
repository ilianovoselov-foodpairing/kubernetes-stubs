import datetime
import typing

from kubernetes.client.models.v1_rolling_update_daemon_set import (
    V1RollingUpdateDaemonSet, V1RollingUpdateDaemonSetDict)

class V1DaemonSetUpdateStrategy:
    rolling_update: typing.Optional[V1RollingUpdateDaemonSet]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[V1RollingUpdateDaemonSet] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1DaemonSetUpdateStrategyDict: ...

class V1DaemonSetUpdateStrategyDict(typing.TypedDict, total=False):
    rollingUpdate: typing.Optional[V1RollingUpdateDaemonSetDict]
    type: typing.Optional[str]
