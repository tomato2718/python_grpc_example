__all__ = ["ExampleRpc"]

from math import ceil

from grpc import RpcContext

from example_server.proto.example_pb2 import ExampleRequest, ExampleResponse
from example_server.proto.example_pb2_grpc import ExampleRpcServicer

from ._client import SaveImageClient


class ExampleRpc(ExampleRpcServicer):
    def ExampleCall(
        self, request: ExampleRequest, context: RpcContext
    ) -> ExampleResponse:
        save_image = SaveImageClient(".")
        filename = str(ceil(request.timestamp))
        image_id = save_image(filename=filename, image=request.image)
        response = ExampleResponse(imageId=image_id)
        return response
