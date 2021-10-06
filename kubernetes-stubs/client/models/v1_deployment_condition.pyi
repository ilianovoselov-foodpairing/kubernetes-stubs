import datetime
import typing

class V1DeploymentCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    last_update_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
    def __init__(
        self,
        *,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        last_update_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: str,
        type: str
    ) -> None: ...
    def to_dict(self) -> V1DeploymentConditionDict: ...

class V1DeploymentConditionDict(typing.TypedDict, total=False):
    lastTransitionTime: typing.Optional[datetime.datetime]
    lastUpdateTime: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
