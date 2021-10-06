import datetime
import typing

import kubernetes.client

class V1beta1PolicyRule:
    api_groups: typing.Optional[typing.List[str]]
    non_resource_ur_ls: typing.Optional[typing.List[str]]
    resource_names: typing.Optional[typing.List[str]]
    resources: typing.Optional[typing.List[str]]
    verbs: typing.List[str]
    def __init__(
        self,
        *,
        api_groups: typing.Optional[typing.List[str]] = ...,
        non_resource_ur_ls: typing.Optional[typing.List[str]] = ...,
        resource_names: typing.Optional[typing.List[str]] = ...,
        resources: typing.Optional[typing.List[str]] = ...,
        verbs: typing.List[str]
    ) -> None: ...
    def to_dict(self) -> V1beta1PolicyRuleDict: ...

class V1beta1PolicyRuleDict(typing.TypedDict, total=False):
    apiGroups: typing.Optional[typing.List[str]]
    nonResourceURLs: typing.Optional[typing.List[str]]
    resourceNames: typing.Optional[typing.List[str]]
    resources: typing.Optional[typing.List[str]]
    verbs: typing.List[str]
