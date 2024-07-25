from time import time

from grpc import insecure_channel

from example_client.proto.example_pb2 import ExampleRequest, ExampleResponse
from example_client.proto.example_pb2_grpc import ExampleRpcStub

SERVER_ADDRESS = "localhost:8080"


def main() -> None:
    with (
        insecure_channel(SERVER_ADDRESS) as channel,
        open("./example.jpg", "rb") as file,
    ):
        stub = ExampleRpcStub(channel)
        image = file.read()
        request = ExampleRequest(timestamp=time(), image=image)
        response: ExampleResponse = stub.ExampleCall(request)
        print(response.imageId)


if __name__ == "__main__":
    main()
