import datetime
import typing

from kubernetes.client.models.extensions_v1beta1_http_ingress_path import (
    ExtensionsV1beta1HTTPIngressPath, ExtensionsV1beta1HTTPIngressPathDict)

class ExtensionsV1beta1HTTPIngressRuleValue:
    paths: typing.List[ExtensionsV1beta1HTTPIngressPath]
    def __init__(
        self, *, paths: typing.List[ExtensionsV1beta1HTTPIngressPath]
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1HTTPIngressRuleValueDict: ...

class ExtensionsV1beta1HTTPIngressRuleValueDict(typing.TypedDict, total=False):
    paths: typing.List[ExtensionsV1beta1HTTPIngressPathDict]
