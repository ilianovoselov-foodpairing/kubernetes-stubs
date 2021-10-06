import datetime
import typing

from kubernetes.client.models.networking_v1beta1_http_ingress_rule_value import (
    NetworkingV1beta1HTTPIngressRuleValue,
    NetworkingV1beta1HTTPIngressRuleValueDict)

class NetworkingV1beta1IngressRule:
    host: typing.Optional[str]
    http: typing.Optional[NetworkingV1beta1HTTPIngressRuleValue]
    def __init__(
        self,
        *,
        host: typing.Optional[str] = ...,
        http: typing.Optional[NetworkingV1beta1HTTPIngressRuleValue] = ...
    ) -> None: ...
    def to_dict(self) -> NetworkingV1beta1IngressRuleDict: ...

class NetworkingV1beta1IngressRuleDict(typing.TypedDict, total=False):
    host: typing.Optional[str]
    http: typing.Optional[NetworkingV1beta1HTTPIngressRuleValueDict]
