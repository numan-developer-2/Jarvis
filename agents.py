from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    noise_cancellation,
)
from livekit.plugins import google
from prompts import SESSION_INSTRUCTIONS , AGENT_INSTRUCTIONS
from tools import get_weather, search_web, send_email
load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
            llm=google.beta.realtime.RealtimeModel(
                voice="Charon",  # Use only the model name
                temperature=0.7  # Adjust temperature for response variability
            ),
            tools=[
                get_weather,
                search_web,
                send_email,
            ],
        )


async def entrypoint(ctx: agents.JobContext):
    assistant = Assistant()
    session = AgentSession(
        llm=assistant.llm,
        tools=assistant.tools,
    )

    await session.start(
        room=ctx.room,
        agent=assistant,
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            video_enabled=True,
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTIONS,
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))