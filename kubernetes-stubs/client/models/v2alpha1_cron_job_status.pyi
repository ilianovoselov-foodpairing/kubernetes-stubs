import datetime
import typing

from kubernetes.client.models.v1_object_reference import (
    V1ObjectReference, V1ObjectReferenceDict)

class V2alpha1CronJobStatus:
    active: typing.Optional[typing.List[V1ObjectReference]]
    last_schedule_time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        active: typing.Optional[typing.List[V1ObjectReference]] = ...,
        last_schedule_time: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
    def to_dict(self) -> V2alpha1CronJobStatusDict: ...

class V2alpha1CronJobStatusDict(typing.TypedDict, total=False):
    active: typing.Optional[typing.List[V1ObjectReferenceDict]]
    lastScheduleTime: typing.Optional[datetime.datetime]
