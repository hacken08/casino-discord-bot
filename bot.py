import interactions


TOKEN = 'MTE4OTg2OTA2MDc2MzE2NDc5NA.GR_hRF.5rofwy9MZ8xn9yh4C9ONQq5r8dlY1VsLxjoJwI'
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

