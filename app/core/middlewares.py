import time

from starlette.types import ASGIApp, Message, Receive, Scope, Send


class ProcessTimeMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        start_time = time.perf_counter()

        async def send_with_time(message: Message) -> None:
            if message["type"] == "http.response.start":
                process_time = time.perf_counter() - start_time
                headers = list(message.get("headers", []))
                headers.append(
                    (b"x-process-time", f"{process_time:.6f}".encode("ascii"))
                )
                message["headers"] = headers
            await send(message)

        await self.app(scope, receive, send_with_time)
