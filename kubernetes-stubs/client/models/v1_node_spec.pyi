import datetime
import typing

from kubernetes.client.models.v1_node_config_source import (
    V1NodeConfigSource, V1NodeConfigSourceDict)
from kubernetes.client.models.v1_taint import V1Taint, V1TaintDict

class V1NodeSpec:
    config_source: typing.Optional[V1NodeConfigSource]
    external_id: typing.Optional[str]
    pod_cidr: typing.Optional[str]
    pod_cid_rs: typing.Optional[typing.List[str]]
    provider_id: typing.Optional[str]
    taints: typing.Optional[typing.List[V1Taint]]
    unschedulable: typing.Optional[bool]
    def __init__(
        self,
        *,
        config_source: typing.Optional[V1NodeConfigSource] = ...,
        external_id: typing.Optional[str] = ...,
        pod_cidr: typing.Optional[str] = ...,
        pod_cid_rs: typing.Optional[typing.List[str]] = ...,
        provider_id: typing.Optional[str] = ...,
        taints: typing.Optional[typing.List[V1Taint]] = ...,
        unschedulable: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeSpecDict: ...

class V1NodeSpecDict(typing.TypedDict, total=False):
    configSource: typing.Optional[V1NodeConfigSourceDict]
    externalID: typing.Optional[str]
    podCIDR: typing.Optional[str]
    podCIDRs: typing.Optional[typing.List[str]]
    providerID: typing.Optional[str]
    taints: typing.Optional[typing.List[V1TaintDict]]
    unschedulable: typing.Optional[bool]
