import datetime
import typing

import kubernetes.client

class V1beta1NonResourceRule:
    non_resource_ur_ls: typing.Optional[typing.List[str]]
    verbs: typing.List[str]
    def __init__(
        self,
        *,
        non_resource_ur_ls: typing.Optional[typing.List[str]] = ...,
        verbs: typing.List[str]
    ) -> None: ...
    def to_dict(self) -> V1beta1NonResourceRuleDict: ...

class V1beta1NonResourceRuleDict(typing.TypedDict, total=False):
    nonResourceURLs: typing.Optional[typing.List[str]]
    verbs: typing.List[str]
