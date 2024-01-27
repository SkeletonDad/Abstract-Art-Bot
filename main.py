from typing import Final
import os 
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from responses import get_response
import vars

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True # NOQA (no quality assurance)
intents.dm_messages = True
intents.voice_states = True
client: Client = Client(intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled..probably)')
        return
    
    #is_private is true if first character is '?'
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# STEP 4: HANDLING INCOMING MESSAGES AND VOICE ACTIVITY
@client.event
async def on_message(message: Message) -> None:
    
    #if the bot sent a message, ignore its own message
    if message.author == client.user:
        return
        
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel and not before.channel and vars.alert_alex:  # Member joined a voice channel
        user_id = member.id # member who just joined
        user = await client.fetch_user('User\'s DM ID') #Alex's discord ID
        await user.send(f'{member.name} Has joined the voice channel! to stop these messages say \'STOP\'')
    
    # If a certain user leaves the voice channel
    elif before.channel and not after.channel and member.id == 'certain member leaving ID':
        channel = client.get_channel('Your text channel')
        await channel.send('Who *was* that?')

# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()