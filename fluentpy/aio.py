import asyncio
import time


async def do_work(task_no):
    await asyncio.sleep(1)
    print('Doing', task_no, 'Task')


async def main():
    t0 = time.perf_counter()
    tasks = [asyncio.create_task(do_work(i)) for i in range(1, 6)]
    done, pending = await asyncio.wait(tasks)

    print('Finished in', time.perf_counter() - t0)


if __name__ == '__main__':
    asyncio.run(main())
