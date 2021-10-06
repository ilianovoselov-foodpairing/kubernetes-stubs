import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v2alpha1_cron_job import (V2alpha1CronJob,
                                                        V2alpha1CronJobDict)

class V2alpha1CronJobList:
    api_version: typing.Optional[str]
    items: typing.List[V2alpha1CronJob]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V2alpha1CronJob],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V2alpha1CronJobListDict: ...

class V2alpha1CronJobListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V2alpha1CronJobDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
