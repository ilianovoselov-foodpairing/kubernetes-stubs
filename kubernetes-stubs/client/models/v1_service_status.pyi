import datetime
import typing

from kubernetes.client.models.v1_load_balancer_status import (
    V1LoadBalancerStatus, V1LoadBalancerStatusDict)

class V1ServiceStatus:
    load_balancer: typing.Optional[V1LoadBalancerStatus]
    def __init__(
        self, *, load_balancer: typing.Optional[V1LoadBalancerStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1ServiceStatusDict: ...

class V1ServiceStatusDict(typing.TypedDict, total=False):
    loadBalancer: typing.Optional[V1LoadBalancerStatusDict]
