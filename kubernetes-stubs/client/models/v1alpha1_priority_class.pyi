import datetime
import typing

from kubernetes.client.models.v1_object_meta import (V1ObjectMeta,
                                                     V1ObjectMetaDict)

class V1alpha1PriorityClass:
    api_version: typing.Optional[str]
    description: typing.Optional[str]
    global_default: typing.Optional[bool]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMeta]
    preemption_policy: typing.Optional[str]
    value: int
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        description: typing.Optional[str] = ...,
        global_default: typing.Optional[bool] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[V1ObjectMeta] = ...,
        preemption_policy: typing.Optional[str] = ...,
        value: int
    ) -> None: ...
    def to_dict(self) -> V1alpha1PriorityClassDict: ...

class V1alpha1PriorityClassDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    description: typing.Optional[str]
    globalDefault: typing.Optional[bool]
    kind: typing.Optional[str]
    metadata: typing.Optional[V1ObjectMetaDict]
    preemptionPolicy: typing.Optional[str]
    value: int
