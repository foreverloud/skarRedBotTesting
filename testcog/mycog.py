import discord
from discord.ext import commands
import aiohttp

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""
        async with aiohttp.get("http://api.icndb.com/jokes/random/") as response:
            result = await response.json()
        joke = result["value"]["joke"]
        await self.bot.say(joke)

def setup(bot):
    bot.add_cog(Mycog(bot))
