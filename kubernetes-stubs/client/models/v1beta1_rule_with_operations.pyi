import datetime
import typing

import kubernetes.client

class V1beta1RuleWithOperations:
    api_groups: typing.Optional[typing.List[str]]
    api_versions: typing.Optional[typing.List[str]]
    operations: typing.Optional[typing.List[str]]
    resources: typing.Optional[typing.List[str]]
    scope: typing.Optional[str]
    def __init__(
        self,
        *,
        api_groups: typing.Optional[typing.List[str]] = ...,
        api_versions: typing.Optional[typing.List[str]] = ...,
        operations: typing.Optional[typing.List[str]] = ...,
        resources: typing.Optional[typing.List[str]] = ...,
        scope: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1RuleWithOperationsDict: ...

class V1beta1RuleWithOperationsDict(typing.TypedDict, total=False):
    apiGroups: typing.Optional[typing.List[str]]
    apiVersions: typing.Optional[typing.List[str]]
    operations: typing.Optional[typing.List[str]]
    resources: typing.Optional[typing.List[str]]
    scope: typing.Optional[str]
