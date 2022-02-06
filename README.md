# chikameshi-line-bot
LINEMessagingAPIを活用したごはん屋さん紹介bot

## 概要

## 開発環境
本リポジトリの開発環境。

- 開発言語
    Python3.8.9
- アプリケーションサーバー
    gunicorn
- Webフレームワーク
    Flask
- DB
    なし

## 運用

# 設定
## 環境変数
アプリケーションの実行に必要となる環境変数について記載する。
- `CHANNEL_ACCESS_TOKEN`
    LINEMessagingAPIから提供されるチャンネルアクセストークン
- `CHANNEL_SECRET_KEY`
    LINEMessagingAPIから提供されるチャンネルシークレットキー
- `HOTPEPPER_API_KEY`
    HOTPEPPERから提供されるグルメサーチAPIキー

# クレジット
Powered by ホットペッパー Webサービス