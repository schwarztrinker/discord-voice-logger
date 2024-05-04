# Discord Voice Channel Logger

## Run Docker Container

```bash
docker run  -e CHANNEL_ID=123367811573416XXXX \
-e BOT_TOKEN=MTIzNjAyNTUyMzgzMDc4XXX.XXXXX.XXXXXXXXXX \
-e VOICE_CHANNEL_ID=10700906303169XXXXXX  \
ghcr.io/schwarztrinker/discord-voice-logger/bot:latest
```

## Needed Environment Variables

- CHANNEL_ID: Channel ID where the Bot logs the notifications
- VOICE_CHANNEL_ID: Channel ID where join actions should be logged for
- BOT_TOKEN: Discord Bot Token to authenticate application

## Invite Coffee Logger Application
Link: https://discord.com/oauth2/authorize?client_id=1236025523830784133&permissions=274877910144&scope=bot%20applications.commands*