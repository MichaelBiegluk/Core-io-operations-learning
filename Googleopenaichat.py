from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[],
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  tools=[
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "strict": true,
        "parameters": {
          "type": "object",
          "required": [
            "location",
            "unit"
          ],
          "properties": {
            "unit": {
              "enum": [
                "c",
                "f"
              ],
              "type": "string"
            },
            "location": {
              "type": "string",
              "description": "The city and state e.g. San Francisco, CA"
            }
          },
          "additionalProperties": false
        },
        "description": "Determine weather in my location"
      }
    },
    {
      "type": "function",
      "function": {
        "name": "get_stock_price",
        "strict": true,
        "parameters": {
          "type": "object",
          "required": [
            "symbol"
          ],
          "properties": {
            "symbol": {
              "type": "string",
              "description": "The stock symbol"
            }
          },
          "additionalProperties": false
        },
        "description": "Get the current stock price"
      }
    }
  ],
  response_format={
    "type": "text"
  }
)
