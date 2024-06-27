# 1. Write a  Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.

# import asyncio

# async def print_delayed_message():
#     await asyncio.sleep(2)  # Wait for 2 seconds
#     print("Python Exercises!")

# # Create an event loop and run the asynchronous function
# async def main():
#     await print_delayed_message()

# # Run the event loop
# asyncio.run(main())



# 2. Write a Python program that creates three asynchronous functions and displays their respective names with different delays (1 second, 2 seconds, and 3 seconds).

# import asyncio
# async def display_name_with_delay(name, delay):
#     await asyncio.sleep(delay)
#     print(name)
# async def main():
#     tasks = [
#         display_name_with_delay("Asyn. function-1", 1),
#         display_name_with_delay("Asyn. function-2", 2),
#         display_name_with_delay("Asyn. function-3", 3)
#     ]    
#     await asyncio.gather(*tasks)
# # Run the event loop
# asyncio.run(main())



# 3. Write a Python program that creates an asyncio event loop and runs a coroutine that prints numbers from 1 to 7 with a delay of 1 second each.

# import asyncio
# async def display_numbers():
#     for i in range(1, 8):
#         print(i)
#         await asyncio.sleep(1)
# # Run the coroutine using asyncio.run()
# asyncio.run(display_numbers())



# 4. Write a Python program that implements a coroutine to fetch data from two different URLs simultaneously using the "aiohttp" library.

# import aiohttp
# import asyncio

# async def fetch_url(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()
# async def main():
#     url_1 = "https://www.wikipedia.org/"
#     url_2 = "https://www.google.com"    
#     task1 = asyncio.create_task(fetch_url(url_1))
#     task2 = asyncio.create_task(fetch_url(url_2))    
#     data1 = await task1
#     data2 = await task2    
#     print("Data from ",url_1, len(data1), "bytes")
#     print("Data from ",url_2, len(data2), "bytes")
# # Run the event loop
# asyncio.run(main())



# 5. Write a  Python program that runs multiple asynchronous tasks concurrently using asyncio.gather() and measures the time taken.

# import asyncio
# import time
# async def task1():
#     print("Task-1 started")
#     await asyncio.sleep(4)
#     print("Task-1 completed")
# async def task2():
#     print("Task-2 started")
#     await asyncio.sleep(1)
#     print("Task-2 completed")
# async def task3():
#     print("Task-3 started\n")
#     await asyncio.sleep(2)
#     print("Task-3 completed")

# async def main():
#     start_time = time.time()    
#     await asyncio.gather(task1(), task2(), task3())    
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print("\nAll tasks completed in {:.2f} seconds".format(elapsed_time))
# # Run the event loop
# asyncio.run(main())


# 6. Write a  Python program to create a coroutine that simulates a time-consuming task and use asyncio.CancelledError to handle task cancellation.

# import asyncio
# import random
# async def time_consuming_task():
#     print('Time-consuming task started...')
#     try:
#         for i in range(1, 6):
#             await asyncio.sleep(random.randint(1,5))
#             print(f'Step {i} completed')
#     except asyncio.CancelledError:
#         print('Time consuming task was cancelled')
#         raise
# async def main():
#     task = asyncio.create_task(time_consuming_task())
#     await asyncio.sleep(random.randint(1,3))    
#     task.cancel()
#     try:
#         await task
#     except asyncio.CancelledError:
#         print('Main coroutine caught task cancellation!')
# asyncio.run(main())


# 7. Write a Python program that implements a timeout for an asynchronous operation using asyncio.wait_for().

# import asyncio
# import time

# async def time_consuming_task(duration):
#     print(f'Starting long operation for {duration} seconds...')
#     await asyncio.sleep(duration)
#     return f'Long operation completed in {duration} seconds'
# async def main():
#     timeout =3
#     try:
#         result = await asyncio.wait_for(time_consuming_task(8), timeout)
#         print(result)
#     except asyncio.TimeoutError:
#         print(f'Timeout occurred after waiting for {timeout} seconds')
# asyncio.run(main())


# 8. Write a Python program that uses asyncio queues to simulate a producer-consumer scenario with multiple producers and a single consumer.

import asyncio
import random
async def producer(queue, id):
    for i in range(3):
        item = f"Item: {id}-{i}"
        await queue.put(item)
        print(f"Producer {id} produced-> {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))
async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumer consumed {item}")
        queue.task_done()
async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue, i)) for i in range(3)]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.join()
    await queue.put(None)  # Signal the consumer to stop
    await consumer_task
# Run the event loop
asyncio.run(main())
