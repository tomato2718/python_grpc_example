from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExampleRequest(_message.Message):
    __slots__ = ("timestamp", "image")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    timestamp: float
    image: bytes
    def __init__(self, timestamp: _Optional[float] = ..., image: _Optional[bytes] = ...) -> None: ...

class ExampleResponse(_message.Message):
    __slots__ = ("imageId",)
    IMAGEID_FIELD_NUMBER: _ClassVar[int]
    imageId: str
    def __init__(self, imageId: _Optional[str] = ...) -> None: ...
