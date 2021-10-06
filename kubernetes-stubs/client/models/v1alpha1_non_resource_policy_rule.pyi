import datetime
import typing

import kubernetes.client

class V1alpha1NonResourcePolicyRule:
    non_resource_ur_ls: typing.List[str]
    verbs: typing.List[str]
    def __init__(
        self, *, non_resource_ur_ls: typing.List[str], verbs: typing.List[str]
    ) -> None: ...
    def to_dict(self) -> V1alpha1NonResourcePolicyRuleDict: ...

class V1alpha1NonResourcePolicyRuleDict(typing.TypedDict, total=False):
    nonResourceURLs: typing.List[str]
    verbs: typing.List[str]
