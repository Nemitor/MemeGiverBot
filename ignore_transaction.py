import os
import asyncio

ignored_ids_file = "ignored_ids.txt"

def check_id(transaction_id):
    if not os.path.exists(ignored_ids_file):
        open(ignored_ids_file, "w").close()

    with open(ignored_ids_file, "r") as file:
        ignored_ids = file.read().splitlines()
        return transaction_id in ignored_ids

async def add_id_to_ignore(transaction_id):
    with open(ignored_ids_file, "a") as file:
        await asyncio.get_event_loop().run_in_executor(None, file.write, transaction_id + "\n")

