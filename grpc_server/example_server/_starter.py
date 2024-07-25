__all__ = ["start_server"]

from example_server.proto.example_pb2_grpc import add_ExampleRpcServicer_to_server
from example_server.server import AsyncGRPCManager
from example_server.service import ExampleRpc


def start_server(address: str) -> None:
    server = AsyncGRPCManager()
    server.add_servicer_to_server(add_ExampleRpcServicer_to_server, ExampleRpc())
    server.serve(address)
