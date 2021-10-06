import datetime
import typing

import kubernetes.client

class V1beta1CronJobStatus:
    active: typing.Optional[typing.List[kubernetes.client.V1ObjectReference]]
    last_schedule_time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        active: typing.Optional[typing.List[kubernetes.client.V1ObjectReference]] = ...,
        last_schedule_time: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CronJobStatusDict: ...

class V1beta1CronJobStatusDict(typing.TypedDict, total=False):
    active: typing.Optional[typing.List[kubernetes.client.V1ObjectReferenceDict]]
    lastScheduleTime: typing.Optional[datetime.datetime]
