import asyncio
import logging

from check_time.check_time import run_scheduled_tasks
from loader import dp, bot
import handlers


async def main():
    # together with the bot, a cycle is started to check the time
    loop = asyncio.get_event_loop()
    loop.create_task(run_scheduled_tasks())
    await dp.start_polling(bot, loop=loop, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
