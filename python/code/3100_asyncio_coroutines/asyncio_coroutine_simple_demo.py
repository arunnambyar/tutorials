import asyncio
import random
import time


async def mock_server_connect(server_name: str) -> str:
    """Mock server connection"""
    mock_delay = random.randint(5, 20)
    await asyncio.sleep(mock_delay)
    return f"RESULT:{server_name}"


async def process_data(server_name: str) -> str:
    print(f"{time.strftime('%H:%M:%S')} STARTED: {server_name} >")
    data = await mock_server_connect(server_name)
    print(f"{time.strftime('%H:%M:%S')} COMPLETED: {server_name} <")
    return data


async def main() -> None:
    print()
    print("Running event loop: >>>>>>>>>>>>>>>>")
    print()

    task_names = [
        "SERVER-A",
        "SERVER-B",
        "SERVER-C",
        "DB-A",
        "DB-B",
        "DB-C",
    ]
    results = list(await asyncio.gather(*(process_data(name) for name in task_names)))

    print()
    print("Event loop completed: <<<<<<<<<<<<<<<")
    print("Results:", results)
    print()


if __name__ == "__main__":
    asyncio.run(main())
