import json
import asyncio
from os import path, SEEK_END
import aiofiles
import time
import re


async def read_file_line_by_line(filename):
    async with aiofiles.open(path.join(".", "data", filename), "r") as f:
        line = await f.readline()
        while line:
            line = line.strip()
            if line:
                yield line
                time.sleep(0.05)
            line = await f.readline()

async def read_entire_json(filename):
    async with aiofiles.open(path.join("data", filename), "r") as f:
        raw = await f.read()
        try:
            json_data = json.loads(raw)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}") 
        return json_data       

async def write_json_per_line(json_data):
    async with aiofiles.open(path.join("data", "one_liner_json.json"), "w") as f:
        await f.write('[\n')
        for record in json_data:
            await f.write(json.dumps(record, separators=(",", ":")))
            await f.write('\n')  # Separate objects with a newline
        await f.write(']\n')

async def read_json_per_line(filename):
    async with aiofiles.open(path.join("data", filename), "r") as f:
        dict_of_json = []
        async for line in f:
            if re.search(r'\[|\]',line):
                continue
            try:
                json_obj = json.loads(line)
                dict_of_json.append(json_obj)
                yield json_obj
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")   
                break


async def main():
    async for line in read_file_line_by_line("data.json"):
        print(line)

    entire_json = await read_entire_json("data.json")
    print(entire_json)  

    await write_json_per_line(entire_json)

    async for record in read_json_per_line("one_liner_json.json"):
        print(f"Record: {record}")
        await asyncio.sleep(1)

asyncio.run(main())

"""
-rw-r--r--   1 nikodemkirsz  staff  1565 Sep 13 21:56 data.json
-rw-r--r--   1 nikodemkirsz  staff  1054 Sep 13 22:42 one_liner_json.json

entire json structure has 1565 bytes and one liner 1054
"""