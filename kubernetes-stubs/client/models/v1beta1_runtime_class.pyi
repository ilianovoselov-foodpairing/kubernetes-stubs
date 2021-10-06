import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_overhead import (V1beta1Overhead,
                                                       V1beta1OverheadDict)
from kubernetes.client.models.v1beta1_scheduling import (V1beta1Scheduling,
                                                         V1beta1SchedulingDict)

class V1beta1RuntimeClass:
    api_version: typing.Optional[str]
    handler: str
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    overhead: typing.Optional[V1beta1Overhead]
    scheduling: typing.Optional[V1beta1Scheduling]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        handler: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        overhead: typing.Optional[V1beta1Overhead] = ...,
        scheduling: typing.Optional[V1beta1Scheduling] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1RuntimeClassDict: ...

class V1beta1RuntimeClassDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    handler: str
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    overhead: typing.Optional[V1beta1OverheadDict]
    scheduling: typing.Optional[V1beta1SchedulingDict]
