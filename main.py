import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def main():
    pass

if __name__ == '__main__':
    asyncio.run(main())
