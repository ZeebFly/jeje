import asyncio
import os
import signal
import sys
from datetime import datetime

import croniter
import tornado.ioloop
import tornado.platform.asyncio
from pytz import timezone

from Userbot import (ReadUser, TaskPending, bot, installPeer, list_error,
                     logger, nlx, owner_id, sending_user)


async def shutdown(signal, loop):
    logger.error(f"Received exit signal {signal.name}...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

    [task.cancel() for task in tasks]

    logger.error("Cancelling outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)

    logger.error("Shutting down the event loop")
    loop.stop()


async def send_error_msg():
    if list_error != []:
        for x in list_error:
            await sending_user(x["user"], x["error_msg"])


async def auto_restart():
    tz = timezone("Asia/Jakarta")
    cron = croniter.croniter("00 00 * * *", datetime.now(tz))
    while True:
        now = datetime.now(tz)
        next_run = cron.get_next(datetime)

        wait_time = (next_run - now).total_seconds()
        await asyncio.sleep(wait_time)
        try:
            await bot.send_message(
                owner_id,
                "<blockquote><b>Restart Daily..\n\nTunggu beberapa menit bot sedang di Restart!!</b></blockquote>",
            )
        except:
            pass
        os.execl(sys.executable, sys.executable, "-m", "Userbot")


async def SendSucces():
    txt = "🔥**Userbot berhasil diaktifkan**🔥\n"
    txt += f"✅ **Total Pengguna: {len(nlx._ubot)}**"
    msg = f"<blockquote>{txt}</blockquote>"
    return await bot.send_message(owner_id, msg)


async def main():
    await asyncio.gather(nlx.compose(), bot.start())
    asyncio.create_task(ReadUser())
    asyncio.create_task(TaskPending())
    await bot.load_seles()
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()
    for s in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(s, lambda: asyncio.create_task(shutdown(s, loop)))
    await asyncio.gather(send_error_msg(), SendSucces(), installPeer(), auto_restart())
    try:
        await stop_event.wait()
    except asyncio.CancelledError:
        pass
    finally:
        await bot.stop()


if __name__ == "__main__":
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    loop = tornado.ioloop.IOLoop.current().asyncio_loop
    loop.run_until_complete(main())
    """
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(
            sig, lambda sig=sig: asyncio.create_task(shutdown(sig, loop))
        )
    try:
        loop.run_until_complete(main())
    except Exception as e:
        logger.error(f"Exception during execution: {e}")
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
    """
