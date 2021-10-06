import datetime
import typing

class V1beta1CertificateSigningRequestSpec:
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    request: str
    signer_name: typing.Optional[str]
    uid: typing.Optional[str]
    usages: typing.Optional[typing.List[str]]
    username: typing.Optional[str]
    def __init__(
        self,
        *,
        extra: typing.Optional[typing.Dict[str, typing.List[str]]] = ...,
        groups: typing.Optional[typing.List[str]] = ...,
        request: str,
        signer_name: typing.Optional[str] = ...,
        uid: typing.Optional[str] = ...,
        usages: typing.Optional[typing.List[str]] = ...,
        username: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1CertificateSigningRequestSpecDict: ...

class V1beta1CertificateSigningRequestSpecDict(typing.TypedDict, total=False):
    extra: typing.Optional[typing.Dict[str, typing.List[str]]]
    groups: typing.Optional[typing.List[str]]
    request: str
    signerName: typing.Optional[str]
    uid: typing.Optional[str]
    usages: typing.Optional[typing.List[str]]
    username: typing.Optional[str]
