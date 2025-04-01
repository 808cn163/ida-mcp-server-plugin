from openai.types.responses import ResponseTextDeltaEvent
from agents.mcp import MCPServerSse
#from agents import Agent, Runner
import asyncio
import os

from openai import AsyncOpenAI

from agents import (
    Agent,
    Runner,
    function_tool,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

BASE_URL = os.getenv("OPENAI_BASE_URL") or ""
API_KEY = os.getenv("OPENAI_API_KEY") or ""
MODEL_NAME = "gpt-4o"

client = AsyncOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)
set_default_openai_client(client=client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)


async def chat_loop(agent):
    while True:
        user_input = input("\n请输入你的问题（输入q退出）：")
        if user_input.lower() == 'q':
            print("退出程序。")
            break

        result = Runner.run_streamed(agent, user_input)

        print("助手回答：")
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)
        print("\n" + "-"*50)

async def main():
    async with MCPServerSse(
        name="SSE IDAPro Server",
        params={
            "url": "http://127.0.0.1:3000/sse",
            "type": "sse"
        }
    ) as mcp_server_ida:
        agent = Agent(
            name="Assistant",
            instructions="Use the tools to achieve the task",
            model=MODEL_NAME,
            mcp_servers=[mcp_server_ida]
        )

        await chat_loop(agent)

if __name__ == '__main__':
    asyncio.run(main())