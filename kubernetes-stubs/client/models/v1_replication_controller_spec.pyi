import datetime
import typing

from kubernetes.client.models.v1_pod_template_spec import (
    V1PodTemplateSpec, V1PodTemplateSpecDict)

class V1ReplicationControllerSpec:
    min_ready_seconds: typing.Optional[int]
    replicas: typing.Optional[int]
    selector: typing.Optional[typing.Dict[str, str]]
    template: typing.Optional[V1PodTemplateSpec]
    def __init__(
        self,
        *,
        min_ready_seconds: typing.Optional[int] = ...,
        replicas: typing.Optional[int] = ...,
        selector: typing.Optional[typing.Dict[str, str]] = ...,
        template: typing.Optional[V1PodTemplateSpec] = ...
    ) -> None: ...
    def to_dict(self) -> V1ReplicationControllerSpecDict: ...

class V1ReplicationControllerSpecDict(typing.TypedDict, total=False):
    minReadySeconds: typing.Optional[int]
    replicas: typing.Optional[int]
    selector: typing.Optional[typing.Dict[str, str]]
    template: typing.Optional[V1PodTemplateSpecDict]
