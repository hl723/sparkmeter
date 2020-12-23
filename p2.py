import asyncio
import logging

# missing import statements
from datetime import datetime
import os      

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")

class Pipeline:
    async def __init__(*args, **kwargs): 
        default_sleep_duration = kwargs["default_sleep_duration"]
    async def sleep_for(coro, sleep_duration, *args, **kwargs): 
        asyncio.sleep(sleep_duration)
        logger.info("Slept for %s seconds", sleep_duration)        
        start = datetime.now()
        await coro(*args, **kwargs)  # changed kwarg to kwargs
        
        end = datetime.now()
        time_elapsed = (start - end).total_seconds()
        logger.debug(f"Executed the coroutine for {time_elapsed} seconds")
