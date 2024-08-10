import interactions


TOKEN = ''
SERVER_ID = 1113799089809784905



client = (
    interactions.Client(
        token=TOKEN,
        default_scope=SERVER_ID
    )
)


@client.event()
async def on_ready():
    print(f'We have logged in as {client.me.name}')

