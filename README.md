# Discord Voice Channel Logger

## Run Docker Container

```bash
docker run  -e CHANNEL_ID=123367811573416XXXX -e BOT_TOKEN=MTIzNjAyNTUyMzgzMDc4XXX.XXXXX.XXXXXXXXXX -e VOICE_CHANNEL_ID=10700906303169XXXXXX  discordcoffeebot:0.0.5
```

## Needed Environment Variables

CHANNEL_ID: Channel ID where the Bot logs the notifications
VOICE_CHANNEL_ID: Channel ID where join actions should be logged for

BOT_TOKEN: Discord Bot Token to authenticate application