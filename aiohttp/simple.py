from aiohttp import ClientSession
import requests
import asyncio
import time
 
links = list()
for page in range(1, 5):
    links.append(f"https://www.104.com.tw/jobs/search/?keyword=python&order=1&page={page}&jobsource=2018indexpoc&ro=0")



def main():
    for link in links:
        res = requests.get(link)


async def aio_main():
    async with ClientSession() as session:
        tasks = [asyncio.create_task(aio_fetch(link, session)) for link in links]  # 建立任務清單
        await asyncio.gather(*tasks)  # 打包任務清單及執行
 
async def aio_fetch(link, session):
    async with session.get(link) as response:  # 非同步發送請求
        html_body = await response.text()
 


# asynchronouse io
start_time = time.time()  # 開始執行時間
loop = asyncio.get_event_loop()  # 建立事件迴圈(Event Loop)
loop.run_until_complete(aio_main())  # 執行協程(coroutine)
print("aio 花費:" + str(time.time() - start_time) + "秒")


# synchronouse io
start_time = time.time()  # 開始執行時間
main()
print("io  花費:" + str(time.time() - start_time) + "秒")
