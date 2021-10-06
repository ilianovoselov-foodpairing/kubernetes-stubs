import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1HTTPIngressRuleValue:
    paths: typing.List[kubernetes.client.ExtensionsV1beta1HTTPIngressPath]
    def __init__(
        self, *, paths: typing.List[kubernetes.client.ExtensionsV1beta1HTTPIngressPath]
    ) -> None: ...
    def to_dict(self) -> ExtensionsV1beta1HTTPIngressRuleValueDict: ...

class ExtensionsV1beta1HTTPIngressRuleValueDict(typing.TypedDict, total=False):
    paths: typing.List[kubernetes.client.ExtensionsV1beta1HTTPIngressPathDict]
