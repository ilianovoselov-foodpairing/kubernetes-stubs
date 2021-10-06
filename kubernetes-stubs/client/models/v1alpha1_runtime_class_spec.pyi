import datetime
import typing

from kubernetes.client.models.v1alpha1_overhead import (V1alpha1Overhead,
                                                        V1alpha1OverheadDict)
from kubernetes.client.models.v1alpha1_scheduling import (
    V1alpha1Scheduling, V1alpha1SchedulingDict)

class V1alpha1RuntimeClassSpec:
    overhead: typing.Optional[V1alpha1Overhead]
    runtime_handler: str
    scheduling: typing.Optional[V1alpha1Scheduling]
    def __init__(
        self,
        *,
        overhead: typing.Optional[V1alpha1Overhead] = ...,
        runtime_handler: str,
        scheduling: typing.Optional[V1alpha1Scheduling] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1RuntimeClassSpecDict: ...

class V1alpha1RuntimeClassSpecDict(typing.TypedDict, total=False):
    overhead: typing.Optional[V1alpha1OverheadDict]
    runtimeHandler: str
    scheduling: typing.Optional[V1alpha1SchedulingDict]
