# MCP画像アップロードツール

## 概要

ローカルの画像ファイルをBase64エンコードし、APIエンドポイントに送信するClaude Desktop用のMCP（Model Context Protocol）ツール。

https://llmcraft.connpass.com/event/352693
のイベントにて作成したもの。

## 機能

- ローカル画像ファイルの読み込み
- Base64エンコーディング
- 指定APIエンドポイントへの送信

## 必要なもの

- Python 3.10以上
- Claude Desktop
- Pythonパッケージ：mcp[cli], httpx

## セットアップ

1. 必要なパッケージをインストール
```bash
uv add "mcp[cli]" httpx
```

2. APIエンドポイントを環境変数で設定
```bash
export API_ENDPOINT="hogehoge_api_endpoint"
```

## 使用方法

Claude Desktopで以下のように入力。
```
例）
send_image_file のmcp_toolを使って、以下のパスの画像をアップロードしてください。
・パス：～～～.png
```
