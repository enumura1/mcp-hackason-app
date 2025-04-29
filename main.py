import os
import base64
import httpx
from mcp.server.fastmcp import FastMCP, Context


# Create MCP server
mcp = FastMCP("ImageAPI")

# Get API endpoint from environment variables
API_ENDPOINT = os.environ.get("API_ENDPOINT")


# Read image from specified file path, encode in Base64, and send to API
@mcp.tool()
async def send_image_file(file_path: str) -> dict:
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            return {
                "status": "error",
                "message": f"ファイルが見つかりません: {file_path}",
            }

        # Read the file
        with open(file_path, "rb") as f:
            image_bytes = f.read()

        # Get the file name
        file_name = os.path.basename(file_path)

        # Base64 encode the file data
        base64_data = base64.b64encode(image_bytes).decode("utf-8")

        # Create payload for API request
        payload = {"file_name": file_name, "file_data": base64_data}

        # Send the payload to the API endpoint
        async with httpx.AsyncClient() as client:
            response = await client.post(API_ENDPOINT, json=payload)

            # レスポンスを処理
            if response.status_code == 200:
                return {
                    "status": "success",
                    "message": "画像が正常にAPIに送信されました",
                    "response": response.json(),
                }
            else:
                return {
                    "status": "error",
                    "message": f"APIエラー: {response.status_code}",
                    "response": response.text,
                }

    except Exception as e:
        return {"status": "error", "message": f"エラー: {str(e)}"}


if __name__ == "__main__":
    # Start MCP server
    mcp.run()
