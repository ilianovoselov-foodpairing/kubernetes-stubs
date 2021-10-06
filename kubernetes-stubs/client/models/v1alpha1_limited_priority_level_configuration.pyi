import datetime
import typing

from kubernetes.client.models.v1alpha1_limit_response import (
    V1alpha1LimitResponse, V1alpha1LimitResponseDict)

class V1alpha1LimitedPriorityLevelConfiguration:
    assured_concurrency_shares: typing.Optional[int]
    limit_response: typing.Optional[V1alpha1LimitResponse]
    def __init__(
        self,
        *,
        assured_concurrency_shares: typing.Optional[int] = ...,
        limit_response: typing.Optional[V1alpha1LimitResponse] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1LimitedPriorityLevelConfigurationDict: ...

class V1alpha1LimitedPriorityLevelConfigurationDict(typing.TypedDict, total=False):
    assuredConcurrencyShares: typing.Optional[int]
    limitResponse: typing.Optional[V1alpha1LimitResponseDict]
