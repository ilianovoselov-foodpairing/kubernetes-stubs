import datetime
import typing

from kubernetes.client.models.v1_load_balancer_ingress import (
    V1LoadBalancerIngress, V1LoadBalancerIngressDict)

class V1LoadBalancerStatus:
    ingress: typing.Optional[typing.List[V1LoadBalancerIngress]]
    def __init__(
        self, *, ingress: typing.Optional[typing.List[V1LoadBalancerIngress]] = ...
    ) -> None: ...
    def to_dict(self) -> V1LoadBalancerStatusDict: ...

class V1LoadBalancerStatusDict(typing.TypedDict, total=False):
    ingress: typing.Optional[typing.List[V1LoadBalancerIngressDict]]
