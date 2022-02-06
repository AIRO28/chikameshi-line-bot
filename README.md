# Name

**chikameshi-line-bot**<br>
Restaurant introduction bot using LINEMessagingAPI<br>
LINEMessagingAPIを活用した飲食店紹介bot<br>

# Overview

※後々アプリのスクリーンショットを添付する。

# Requirement

- Python 3.8.9
- pipenv
- flask
- line-bot-sdk
- requests
- gunicorn

# Installation

```shell
# Install the python library from the Pipfile.
$ pipenv install
```

## Environment variable

The following environment variables are required to run this application.<br>

- `CHANNEL_ACCESS_TOKEN`<br>
    Channel access token provided by LINEMessagingAPI.<br>
    LINEMessagingAPIから提供されるチャンネルアクセストークン。<br>
- `CHANNEL_SECRET_KEY`<br>
    Channel secret key provided by LINEMessagingAPI.<br>
    LINEMessagingAPIから提供されるチャンネルシークレットキー。<br>
- `HOTPEPPER_API_KEY`<br>
    Gourmet search API key provided by HOTPEPPER.<br>
    HOTPEPPERから提供されるグルメサーチAPIキー。<br>

# Demo

```shell
$ git clone 
$ cd chikameshi-line-bot
$ gunicorn -c gunicorn.conf.py

```

# Note

This repository uses the API provided by HOTPEPPER Web Service.<br>

## Credits

- Powered by ホットペッパー Webサービス

# Auther
My name is **AIRO**!<br>
- [Gihub](https://github.com/AIRO28)
- [Twitter](https://twitter.com/AIRO28_)
- [Qiita](https://qiita.com/AIRO)

# Licence
This repository is Free.
