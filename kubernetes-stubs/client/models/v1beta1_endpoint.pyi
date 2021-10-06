import datetime
import typing

from kubernetes.client.models.v1_object_reference import (
    V1ObjectReference, V1ObjectReferenceDict)
from kubernetes.client.models.v1beta1_endpoint_conditions import (
    V1beta1EndpointConditions, V1beta1EndpointConditionsDict)

class V1beta1Endpoint:
    addresses: typing.List[str]
    conditions: typing.Optional[V1beta1EndpointConditions]
    hostname: typing.Optional[str]
    target_ref: typing.Optional[V1ObjectReference]
    topology: typing.Optional[typing.Dict[str, str]]
    def __init__(
        self,
        *,
        addresses: typing.List[str],
        conditions: typing.Optional[V1beta1EndpointConditions] = ...,
        hostname: typing.Optional[str] = ...,
        target_ref: typing.Optional[V1ObjectReference] = ...,
        topology: typing.Optional[typing.Dict[str, str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1EndpointDict: ...

class V1beta1EndpointDict(typing.TypedDict, total=False):
    addresses: typing.List[str]
    conditions: typing.Optional[V1beta1EndpointConditionsDict]
    hostname: typing.Optional[str]
    targetRef: typing.Optional[V1ObjectReferenceDict]
    topology: typing.Optional[typing.Dict[str, str]]
