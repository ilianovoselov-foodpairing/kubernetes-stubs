import datetime
import typing

from kubernetes.client.models.v1_load_balancer_status import (
    V1LoadBalancerStatus, V1LoadBalancerStatusDict)

class ExtensionsV1beta1IngressStatus:
    load_balancer: typing.Optional[V1LoadBalancerStatus]
    def __init__(
        self, *, load_balancer: typing.Optional[V1LoadBalancerStatus] = ...
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1IngressStatusDict: ...

class ExtensionsV1beta1IngressStatusDict(typing.TypedDict, total=False):
    loadBalancer: typing.Optional[V1LoadBalancerStatusDict]
