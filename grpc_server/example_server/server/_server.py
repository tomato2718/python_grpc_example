__all__ = ["AsyncGRPCManager"]

from asyncio import get_event_loop, set_event_loop_policy
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, TypeVar

from grpc import Compression
from grpc.aio import Server, server
from uvloop import EventLoopPolicy

_ServicerType = TypeVar("_ServicerType")


class AsyncGRPCManager:
    _async_server: Server

    def __init__(self) -> None:
        self._async_server = server(
            migration_thread_pool=ThreadPoolExecutor(),
            options=[
                ("grpc.max_receive_message_length", -1),
                ("grpc.so_reuseport", 1),
            ],
            compression=Compression.NoCompression,
        )

    def serve(self, address: str) -> None:
        """
        Start the server.
        """
        loop = get_event_loop()
        set_event_loop_policy(EventLoopPolicy())
        loop.run_until_complete(self._serve(address))

    async def _serve(self, address: str) -> None:
        self._async_server.add_insecure_port(address)
        await self._async_server.start()
        print("Server is now started.")
        await self._async_server.wait_for_termination()

    def add_servicer_to_server(
        self,
        add_servicer_callable: Callable[[_ServicerType, Server], None],
        servicer: _ServicerType,
    ) -> None:
        """
        Add servicer to the server.
        """
        add_servicer_callable(servicer, self._async_server)
