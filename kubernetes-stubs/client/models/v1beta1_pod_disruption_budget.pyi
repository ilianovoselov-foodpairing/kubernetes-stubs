import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)
from kubernetes.client.models.v1beta1_pod_disruption_budget_spec import (
    V1beta1PodDisruptionBudgetSpec, V1beta1PodDisruptionBudgetSpecDict)
from kubernetes.client.models.v1beta1_pod_disruption_budget_status import (
    V1beta1PodDisruptionBudgetStatus, V1beta1PodDisruptionBudgetStatusDict)

class V1beta1PodDisruptionBudget:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    spec: typing.Optional[V1beta1PodDisruptionBudgetSpec]
    status: typing.Optional[V1beta1PodDisruptionBudgetStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        spec: typing.Optional[V1beta1PodDisruptionBudgetSpec] = ...,
        status: typing.Optional[V1beta1PodDisruptionBudgetStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PodDisruptionBudgetDict: ...

class V1beta1PodDisruptionBudgetDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    spec: typing.Optional[V1beta1PodDisruptionBudgetSpecDict]
    status: typing.Optional[V1beta1PodDisruptionBudgetStatusDict]
