import datetime
import typing

from kubernetes.client.models.v1_container_state_running import (
    V1ContainerStateRunning, V1ContainerStateRunningDict)
from kubernetes.client.models.v1_container_state_terminated import (
    V1ContainerStateTerminated, V1ContainerStateTerminatedDict)
from kubernetes.client.models.v1_container_state_waiting import (
    V1ContainerStateWaiting, V1ContainerStateWaitingDict)

class V1ContainerState:
    running: typing.Optional[V1ContainerStateRunning]
    terminated: typing.Optional[V1ContainerStateTerminated]
    waiting: typing.Optional[V1ContainerStateWaiting]
    def __init__(
        self,
        *,
        running: typing.Optional[V1ContainerStateRunning] = ...,
        terminated: typing.Optional[V1ContainerStateTerminated] = ...,
        waiting: typing.Optional[V1ContainerStateWaiting] = ...
    ) -> None: ...
    def to_dict(self) -> V1ContainerStateDict: ...

class V1ContainerStateDict(typing.TypedDict, total=False):
    running: typing.Optional[V1ContainerStateRunningDict]
    terminated: typing.Optional[V1ContainerStateTerminatedDict]
    waiting: typing.Optional[V1ContainerStateWaitingDict]
