import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
class CustomClient(discord.Client):
        async def on_ready(self):
            print(f'{self.user} has connected to Discord!')

def run_discord_bot():
    TOKEN = 'MTA1MTk2MTU3ODU1MzA5NDE0NA.GhH3Fh.d6TmoJKuY4mZ95lHqh4XrF_2r6N77Nrm2DG2co'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
        
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said: "{user_message}" ({channel})')
        
        if user_message[0] == "/":
            user_message = user_message[1:] 
            await send_message(message, user_message, is_private=True)
        else:
            await(send_message(message, user_message, is_private=False))
            
   ### @client.event
   # async def on_message(message):
        #if message.author == client.user:
         #   return
        
        #jordan_names = [
         #   'LOW',
        #    'MID',
       #     'HIGH'
       # ]
        
       # if message.content == 'JORDAN':
        #    response = jordan_names
       #     await message.channel.send(response)
            
    @client.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to our Society!'
        )
            
        
            

        
    client.run(TOKEN)