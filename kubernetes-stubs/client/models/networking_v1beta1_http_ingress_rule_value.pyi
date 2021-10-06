import datetime
import typing

from kubernetes.client.models.networking_v1beta1_http_ingress_path import (
    NetworkingV1beta1HTTPIngressPath, NetworkingV1beta1HTTPIngressPathDict)

class NetworkingV1beta1HTTPIngressRuleValue:
    paths: typing.List[NetworkingV1beta1HTTPIngressPath]
    def __init__(
        self, *, paths: typing.List[NetworkingV1beta1HTTPIngressPath]
    ) -> None: ...
    def to_dict(self) -> NetworkingV1beta1HTTPIngressRuleValueDict: ...

class NetworkingV1beta1HTTPIngressRuleValueDict(typing.TypedDict, total=False):
    paths: typing.List[NetworkingV1beta1HTTPIngressPathDict]
