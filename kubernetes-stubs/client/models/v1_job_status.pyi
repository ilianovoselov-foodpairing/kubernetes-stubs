import datetime
import typing

from kubernetes.client.models.v1_job_condition import (V1JobCondition,
                                                       V1JobConditionDict)

class V1JobStatus:
    active: typing.Optional[int]
    completion_time: typing.Optional[datetime.datetime]
    conditions: typing.Optional[typing.List[V1JobCondition]]
    failed: typing.Optional[int]
    start_time: typing.Optional[datetime.datetime]
    succeeded: typing.Optional[int]
    def __init__(
        self,
        *,
        active: typing.Optional[int] = ...,
        completion_time: typing.Optional[datetime.datetime] = ...,
        conditions: typing.Optional[typing.List[V1JobCondition]] = ...,
        failed: typing.Optional[int] = ...,
        start_time: typing.Optional[datetime.datetime] = ...,
        succeeded: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1JobStatusDict: ...

class V1JobStatusDict(typing.TypedDict, total=False):
    active: typing.Optional[int]
    completionTime: typing.Optional[datetime.datetime]
    conditions: typing.Optional[typing.List[V1JobConditionDict]]
    failed: typing.Optional[int]
    startTime: typing.Optional[datetime.datetime]
    succeeded: typing.Optional[int]
