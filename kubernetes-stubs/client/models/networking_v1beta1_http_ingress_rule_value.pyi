import datetime
import typing

import kubernetes.client

class NetworkingV1beta1HTTPIngressRuleValue:
    paths: typing.List[kubernetes.client.NetworkingV1beta1HTTPIngressPath]
    def __init__(
        self, *, paths: typing.List[kubernetes.client.NetworkingV1beta1HTTPIngressPath]
    ) -> None: ...
    def to_dict(self) -> NetworkingV1beta1HTTPIngressRuleValueDict: ...

class NetworkingV1beta1HTTPIngressRuleValueDict(typing.TypedDict, total=False):
    paths: typing.List[kubernetes.client.NetworkingV1beta1HTTPIngressPathDict]
