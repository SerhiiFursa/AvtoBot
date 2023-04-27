import asyncio
import schedule

from scraping.scraping_data import scraping_data


async def run_scheduled_tasks():
    while True:
        schedule.run_pending()
        await scraping_data()
        await asyncio.sleep(60 * 3)
