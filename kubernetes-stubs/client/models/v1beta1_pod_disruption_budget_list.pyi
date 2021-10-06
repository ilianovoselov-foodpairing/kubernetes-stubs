import datetime
import typing

from kubernetes.client.models.v1_list_meta import V1ListMeta, V1ListMetaDict
from kubernetes.client.models.v1beta1_pod_disruption_budget import (
    V1beta1PodDisruptionBudget, V1beta1PodDisruptionBudgetDict)

class V1beta1PodDisruptionBudgetList:
    api_version: typing.Optional[str]
    items: typing.List[V1beta1PodDisruptionBudget]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.List[V1beta1PodDisruptionBudget],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PodDisruptionBudgetListDict: ...

class V1beta1PodDisruptionBudgetListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.List[V1beta1PodDisruptionBudgetDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ListMetaDict]
