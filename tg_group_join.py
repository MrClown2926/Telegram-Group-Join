import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def display_banner():
    banner = f"""
{Fore.RED}
 _____ ____    ____                             _       _       
|_   _/ ___|  / ___|_ __ ___  _   _ _ __       | | ___ (_)_ __  
  | || |  _  | |  _| '__/ _ \\| | | | '_ \\   _  | |/ _ \\| | '_ \\ 
  | || |_| | | |_| | | | (_) | |_| | |_) | | |_| | (_) | | | | |
  |_|_\\____|  \\____|_|  \\___/ \\__,_| .__/   \\___/ \\___/|_|_| |_|
    | __ ) _   _     / \\  _   _  __|_|_ __ |  _ \\  __ _ ___     
    |  _ \\| | | |   / _ \\| | | |/ _` | '_ \\| | | |/ _` / __|    
    | |_) | |_| |  / ___ \\ |_| | (_| | | | | |_| | (_| \\__ \\    
    |____/ \\__, | /_/   \\_\\__,_|\\__,_|_| |_|____/ \\__,_|___/    
           |___/          |___/                                 
{Fore.RESET}
"""
    print(banner)

class TelegramAPIs:
    def __init__(self, api_id, api_hash, phone_number):
        self.client = TelegramClient('session_name', api_id, api_hash)
        self.phone_number = phone_number

    async def join_group(self, link):
        try:
            await self.client(JoinChannelRequest(link))
            print(f"Joined group: {link}")
        except Exception as e:
            print(f"Failed to join group {link}: {e}")

    async def join_groups_from_file(self, file_path):
        await self.client.start(phone=self.phone_number)
        try:
            with open(file_path, 'r') as f:
                group_links = f.read().splitlines()
                tasks = [self.join_group(link) for link in group_links]
                await asyncio.gather(*tasks)
        except Exception as e:
            print(f"Failed to join groups: {e}")
        finally:
            await self.client.disconnect()

async def main():
    display_banner()
    
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API Hash: ")
    phone_number = input("Enter your phone number: ")
    file_path = input("Enter the path to your group join text file: ")

    ta = TelegramAPIs(api_id=api_id, api_hash=api_hash, phone_number=phone_number)
    await ta.join_groups_from_file(file_path)

if __name__ == "__main__":
    asyncio.run(main())