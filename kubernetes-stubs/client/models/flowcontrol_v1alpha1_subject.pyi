import datetime
import typing

from kubernetes.client.models.v1alpha1_group_subject import (
    V1alpha1GroupSubject, V1alpha1GroupSubjectDict)
from kubernetes.client.models.v1alpha1_service_account_subject import (
    V1alpha1ServiceAccountSubject, V1alpha1ServiceAccountSubjectDict)
from kubernetes.client.models.v1alpha1_user_subject import (
    V1alpha1UserSubject, V1alpha1UserSubjectDict)

class FlowcontrolV1alpha1Subject:
    group: typing.Optional[V1alpha1GroupSubject]
    kind: str
    service_account: typing.Optional[V1alpha1ServiceAccountSubject]
    user: typing.Optional[V1alpha1UserSubject]
    def __init__(
        self,
        *,
        group: typing.Optional[V1alpha1GroupSubject] = ...,
        kind: str,
        service_account: typing.Optional[V1alpha1ServiceAccountSubject] = ...,
        user: typing.Optional[V1alpha1UserSubject] = ...
    ) -> None: ...
    def to_dict(self) -> FlowcontrolV1alpha1SubjectDict: ...

class FlowcontrolV1alpha1SubjectDict(typing.TypedDict, total=False):
    group: typing.Optional[V1alpha1GroupSubjectDict]
    kind: str
    serviceAccount: typing.Optional[V1alpha1ServiceAccountSubjectDict]
    user: typing.Optional[V1alpha1UserSubjectDict]
