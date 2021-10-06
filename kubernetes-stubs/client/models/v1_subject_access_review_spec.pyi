import datetime
import typing

import kubernetes.client

class V1SubjectAccessReviewSpec:
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    non_resource_attributes: typing.Optional[kubernetes.client.V1NonResourceAttributes]
    resource_attributes: typing.Optional[kubernetes.client.V1ResourceAttributes]
    uid: typing.Optional[str]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        extra: typing.Optional[typing.Dict[str, typing.List[str]]] = ...,
        groups: typing.Optional[typing.List[str]] = ...,
        non_resource_attributes: typing.Optional[
            kubernetes.client.V1NonResourceAttributes
        ] = ...,
        resource_attributes: typing.Optional[
            kubernetes.client.V1ResourceAttributes
        ] = ...,
        uid: typing.Optional[str] = ...,
        user: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1SubjectAccessReviewSpecDict: ...

class V1SubjectAccessReviewSpecDict(typing.TypedDict, total=False):
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    nonResourceAttributes: typing.Optional[
        kubernetes.client.V1NonResourceAttributesDict
    ]
    resourceAttributes: typing.Optional[kubernetes.client.V1ResourceAttributesDict]
    uid: typing.Optional[str]
    user: typing.Optional[str]
