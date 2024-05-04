# Discord Voice Channel Logger

## Run Docker Container

```bash
docker run  -e CHANNEL_ID=123367811573416XXXX \
-e BOT_TOKEN=MTIzNjAyNTUyMzgzMDc4XXX.XXXXX.XXXXXXXXXX \
-e VOICE_CHANNEL_ID=10700906303169XXXXXX  \
ghcr.io/schwarztrinker/discord-voice-logger/bot:latest
```

## Create Kubernetes Objects

```bash
kubectl create secret generic discord-bot-secrets -n discord-voice-logger  \
--from-literal=CHANNEL_ID=123367811573416XXXX \
--from-literal=BOT_TOKEN=MTIzNjAyNTUyMzgzMDc4XXX.XXXXX.XXXXXXXXXX \
--from-literal=VOICE_CHANNEL_ID=10700906303169XXXXXX
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: discord-voice-logger
  name: discord-voice-logger
  labels:
    app: discord-voice-logger
spec:
  replicas: 1
  selector:
    matchLabels:
      app: discord-voice-logger
  template:
    metadata:
      labels:
        app: discord-voice-logger
    spec:
      containers:
      - name: bot
        image: ghcr.io/schwarztrinker/discord-voice-logger/bot:latest
        env:
        - name: CHANNEL_ID
          valueFrom:
            secretKeyRef:
              name: discord-bot-secrets
              key: CHANNEL_ID
        - name: BOT_TOKEN
          valueFrom:
            secretKeyRef:
              name: discord-bot-secrets
              key: BOT_TOKEN
        - name: VOICE_CHANNEL_ID
          valueFrom:
            secretKeyRef:
              name: discord-bot-secrets
              key: VOICE_CHANNEL_ID
```

## Needed Environment Variables

- CHANNEL_ID: Channel ID where the Bot logs the notifications
- VOICE_CHANNEL_ID: Channel ID where join actions should be logged for
- BOT_TOKEN: Discord Bot Token to authenticate application

## Invite Coffee Logger Application
Link: https://discord.com/oauth2/authorize?client_id=1236025523830784133&permissions=274877910144&scope=bot%20applications.commands*