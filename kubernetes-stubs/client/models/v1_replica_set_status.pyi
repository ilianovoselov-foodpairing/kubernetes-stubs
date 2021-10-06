import datetime
import typing

from kubernetes.client.models.v1_replica_set_condition import (
    V1ReplicaSetCondition, V1ReplicaSetConditionDict)

class V1ReplicaSetStatus:
    available_replicas: typing.Optional[int]
    conditions: typing.Optional[typing.List[V1ReplicaSetCondition]]
    fully_labeled_replicas: typing.Optional[int]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    def __init__(
        self,
        *,
        available_replicas: typing.Optional[int] = ...,
        conditions: typing.Optional[typing.List[V1ReplicaSetCondition]] = ...,
        fully_labeled_replicas: typing.Optional[int] = ...,
        observed_generation: typing.Optional[int] = ...,
        ready_replicas: typing.Optional[int] = ...,
        replicas: int
    ) -> None: ...
    def to_dict(self) -> V1ReplicaSetStatusDict: ...

class V1ReplicaSetStatusDict(typing.TypedDict, total=False):
    availableReplicas: typing.Optional[int]
    conditions: typing.Optional[typing.List[V1ReplicaSetConditionDict]]
    fullyLabeledReplicas: typing.Optional[int]
    observedGeneration: typing.Optional[int]
    readyReplicas: typing.Optional[int]
    replicas: int
