import asyncio
import random
import time


async def mock_server_connect(server_name: str) -> str:
    """Mock server connection"""

    # START: mocked server connection
    # by non-blocking sleep for a random number of seconds
    mock_delay = random.randint(5, 20)
    await asyncio.sleep(mock_delay)
    # DONE: mocked server connection

    return f"RESULT:{server_name}"


async def process_server_data(server_name: str) -> str:
    print(f"{time.strftime('%H:%M:%S')} STARTED: {server_name} >")

    data = await mock_server_connect(server_name)

    print(f"{time.strftime('%H:%M:%S')} COMPLETED: {server_name} <")
    return data


async def process_db_data(server_name: str) -> str:
    print(f"{time.strftime('%H:%M:%S')} STARTED: {server_name} >")

    data = await mock_server_connect(server_name)

    print(f"{time.strftime('%H:%M:%S')} COMPLETED: {server_name} <")
    return data


async def main() -> None:
    print()
    print("Running event loop: >>>>>>>>>>>>>>>>")
    print()

    loop = asyncio.get_running_loop()
    scheduled = [
        loop.create_task(process_server_data("SERVER-A")),
        loop.create_task(process_server_data("SERVER-B")),
        loop.create_task(process_server_data("SERVER-C")),
        loop.create_task(process_db_data("DB-A")),
        loop.create_task(process_db_data("DB-B")),
        loop.create_task(process_db_data("DB-C")),
    ]
    results = list(await asyncio.gather(*scheduled))

    print()
    print("Event loop completed: <<<<<<<<<<<<<<<")
    print("Results:", results)
    print()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
