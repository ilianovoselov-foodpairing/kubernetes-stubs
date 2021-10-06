import datetime
import typing

from kubernetes.client.models.v1_preconditions import (V1Preconditions,
                                                       V1PreconditionsDict)

class V1DeleteOptions:
    api_version: typing.Optional[str]
    dry_run: typing.Optional[typing.List[str]]
    grace_period_seconds: typing.Optional[int]
    kind: typing.Optional[str]
    orphan_dependents: typing.Optional[bool]
    preconditions: typing.Optional[V1Preconditions]
    propagation_policy: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        dry_run: typing.Optional[typing.List[str]] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        kind: typing.Optional[str] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        preconditions: typing.Optional[V1Preconditions] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1DeleteOptionsDict: ...

class V1DeleteOptionsDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    dryRun: typing.Optional[typing.List[str]]
    gracePeriodSeconds: typing.Optional[int]
    kind: typing.Optional[str]
    orphanDependents: typing.Optional[bool]
    preconditions: typing.Optional[V1PreconditionsDict]
    propagationPolicy: typing.Optional[str]
