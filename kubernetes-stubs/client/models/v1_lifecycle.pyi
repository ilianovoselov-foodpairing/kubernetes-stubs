import datetime
import typing

from kubernetes.client.models.v1_handler import V1Handler, V1HandlerDict

class V1Lifecycle:
    post_start: typing.Optional[V1Handler]
    pre_stop: typing.Optional[V1Handler]
    def __init__(
        self,
        *,
        post_start: typing.Optional[V1Handler] = ...,
        pre_stop: typing.Optional[V1Handler] = ...
    ) -> None: ...
    def to_dict(self) -> V1LifecycleDict: ...

class V1LifecycleDict(typing.TypedDict, total=False):
    postStart: typing.Optional[V1HandlerDict]
    preStop: typing.Optional[V1HandlerDict]
