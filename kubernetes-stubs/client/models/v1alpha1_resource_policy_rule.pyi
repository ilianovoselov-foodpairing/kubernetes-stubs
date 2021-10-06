import datetime
import typing

class V1alpha1ResourcePolicyRule:
    api_groups: typing.List[str]
    cluster_scope: typing.Optional[bool]
    namespaces: typing.Optional[typing.List[str]]
    resources: typing.List[str]
    verbs: typing.List[str]
    def __init__(
        self,
        *,
        api_groups: typing.List[str],
        cluster_scope: typing.Optional[bool] = ...,
        namespaces: typing.Optional[typing.List[str]] = ...,
        resources: typing.List[str],
        verbs: typing.List[str]
    ) -> None: ...
    def to_dict(self) -> V1alpha1ResourcePolicyRuleDict: ...

class V1alpha1ResourcePolicyRuleDict(typing.TypedDict, total=False):
    apiGroups: typing.List[str]
    clusterScope: typing.Optional[bool]
    namespaces: typing.Optional[typing.List[str]]
    resources: typing.List[str]
    verbs: typing.List[str]
