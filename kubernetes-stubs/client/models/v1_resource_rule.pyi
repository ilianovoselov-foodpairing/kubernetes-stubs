import datetime
import typing

import kubernetes.client

class V1ResourceRule:
    api_groups: typing.Optional[typing.List[str]]
    resource_names: typing.Optional[typing.List[str]]
    resources: typing.Optional[typing.List[str]]
    verbs: typing.List[str]
    def __init__(
        self,
        *,
        api_groups: typing.Optional[typing.List[str]] = ...,
        resource_names: typing.Optional[typing.List[str]] = ...,
        resources: typing.Optional[typing.List[str]] = ...,
        verbs: typing.List[str]
    ) -> None: ...
    def to_dict(self) -> V1ResourceRuleDict: ...

class V1ResourceRuleDict(typing.TypedDict, total=False):
    apiGroups: typing.Optional[typing.List[str]]
    resourceNames: typing.Optional[typing.List[str]]
    resources: typing.Optional[typing.List[str]]
    verbs: typing.List[str]
