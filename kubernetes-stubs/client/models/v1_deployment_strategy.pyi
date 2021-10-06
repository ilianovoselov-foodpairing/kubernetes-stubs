import datetime
import typing

from kubernetes.client.models.v1_rolling_update_deployment import (
    V1RollingUpdateDeployment, V1RollingUpdateDeploymentDict)

class V1DeploymentStrategy:
    rolling_update: typing.Optional[V1RollingUpdateDeployment]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[V1RollingUpdateDeployment] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1DeploymentStrategyDict: ...

class V1DeploymentStrategyDict(typing.TypedDict, total=False):
    rollingUpdate: typing.Optional[V1RollingUpdateDeploymentDict]
    type: typing.Optional[str]
