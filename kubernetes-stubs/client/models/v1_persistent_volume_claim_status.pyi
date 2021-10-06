import datetime
import typing

from kubernetes.client.models.v1_persistent_volume_claim_condition import (
    V1PersistentVolumeClaimCondition, V1PersistentVolumeClaimConditionDict)

class V1PersistentVolumeClaimStatus:
    access_modes: typing.Optional[typing.List[str]]
    capacity: typing.Optional[typing.Dict[str, str]]
    conditions: typing.Optional[typing.List[V1PersistentVolumeClaimCondition]]
    phase: typing.Optional[str]
    def __init__(
        self,
        *,
        access_modes: typing.Optional[typing.List[str]] = ...,
        capacity: typing.Optional[typing.Dict[str, str]] = ...,
        conditions: typing.Optional[
            typing.List[V1PersistentVolumeClaimCondition]
        ] = ...,
        phase: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeClaimStatusDict: ...

class V1PersistentVolumeClaimStatusDict(typing.TypedDict, total=False):
    accessModes: typing.Optional[typing.List[str]]
    capacity: typing.Optional[typing.Dict[str, str]]
    conditions: typing.Optional[typing.List[V1PersistentVolumeClaimConditionDict]]
    phase: typing.Optional[str]
