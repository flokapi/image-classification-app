import asyncio


from .counter import Counter


async def init(page, api):
    counter = Counter(api)
    page.add(counter)
    await asyncio.create_task(counter.loop())
