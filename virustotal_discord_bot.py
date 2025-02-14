from discord import Intents, Client, Message

from responses import *

with open('creds.txt', 'r') as file:
    TOKEN = file.read().splitlines()[0]

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        return
    if is_private := user_message.startswith('?'):
        user_message = user_message[
            1]  # if the message is private, then send the message in the dms rather than in the group.
    try:
        response: str = get_response(user_message)
        if response != '':
            await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


async def send_message_edited(message: Message, user_message: str) -> None:
    if not user_message:
        return
    if is_private := user_message.startswith('?'):
        user_message = user_message[1]
    try:
        response: str = get_edited_response(user_message)
        if response != '':
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running.")


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel:15}] {username:15}: "{user_message}"')
    await send_message(message, user_message)


@client.event
async def on_message_edit(message_before: Message, message_after: Message) -> None:
    if message_before.content == message_after.content:
        return
    username: str = str(message_after.author)
    user_message: str = message_after.content
    channel: str = str(message_after.channel)
    print(f'[{channel:15}] {username:15}: Edited -> "{user_message}"')
    await send_message_edited(message_after, user_message)


if __name__ == '__main__':
    client.run(token=TOKEN)
