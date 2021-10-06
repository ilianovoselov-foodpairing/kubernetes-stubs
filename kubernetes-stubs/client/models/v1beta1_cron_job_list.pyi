import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_cron_job import (V1beta1CronJob,
                                                       V1beta1CronJobDict)

class V1beta1CronJobList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1CronJob]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1CronJob],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CronJobListDict: ...

class V1beta1CronJobListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1CronJobDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
