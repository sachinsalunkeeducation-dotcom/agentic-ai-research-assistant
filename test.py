import asyncio
from orchestrator import Orchestrator

async def main():

    orchestrator = Orchestrator()

    report = await orchestrator.run(
        "Research mechancal trends"
    )

    print(report)

asyncio.run(main())



# from agents.retriever import RetrieverAgent

# retriever = RetrieverAgent()

# result = retriever.retrieve("Research AI trends")

# print(result)