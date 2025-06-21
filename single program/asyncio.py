import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("func1")

async def function2():
    await asyncio.sleep(1)

    print("func2")
    
async def function3():
    await asyncio.sleep(1)
    print("func3")

async def main():

    await function1()
    await function1()
    await function3()

asyncio.run(main())