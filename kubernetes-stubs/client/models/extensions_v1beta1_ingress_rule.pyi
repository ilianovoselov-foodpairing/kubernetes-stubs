import datetime
import typing

from kubernetes.client.models.extensions_v1beta1_http_ingress_rule_value import (
    ExtensionsV1beta1HTTPIngressRuleValue,
    ExtensionsV1beta1HTTPIngressRuleValueDict)

class ExtensionsV1beta1IngressRule:
    host: typing.Optional[str]
    http: typing.Optional[ExtensionsV1beta1HTTPIngressRuleValue]
    def __init__(
        self,
        *,
        host: typing.Optional[str] = ...,
        http: typing.Optional[ExtensionsV1beta1HTTPIngressRuleValue] = ...
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1IngressRuleDict: ...

class ExtensionsV1beta1IngressRuleDict(typing.TypedDict, total=False):
    host: typing.Optional[str]
    http: typing.Optional[ExtensionsV1beta1HTTPIngressRuleValueDict]
