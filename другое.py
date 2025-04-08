import asyncio
import os
import time

T = 0.01
gifts = []
poezd = []


async def buy_gift(item, t1, t2):
    print(f'Buy {item}')
    await asyncio.sleep(t1 * T)
    await asyncio.sleep(t2 * T)
    print(f'Got {item}')


async def arr():
    task = []
    for el in gifts:
        task.append(buy_gift(*el))
    await asyncio.gather(*task)


async def stops(i, stop, arrive):
    print(f'Buying gifts at {i + 1} stop')
    tmp = [x for x in gifts if x[1] + x[2] <= stop]
    tmp = sorted(tmp, key=lambda y: -(y[1] + y[2]))
    tasks = []
    res = stop
    for gift in tmp:
        if res - gift[1] - gift[2] >= 0:
            tasks.append(asyncio.create_task(buy_gift(*gift)))
            res -= (gift[1] + gift[2])
            gifts.remove(gift)
    await asyncio.gather(*tasks)
    print(f'Arrive from {i + 1} stop')
    time.sleep(arrive * T)


def main():
    for i, p in enumerate(poezd):
        asyncio.run(stops(i, *p))
    if gifts:
        print('Buying gifts after arrival')
        asyncio.run(arr())


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    stop = input()
    while stop:
        poezd.append(list(map(int, stop.split())))
        stop = input()
    gift = input()
    while gift:
        a, t1, t2 = gift.split()
        gifts.append((a, int(t1), int(t2)))
        gift = input()

    main()
