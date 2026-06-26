import asyncio
from agents.base_agent import BaseAgent

class RiskAnalyzerAgent(BaseAgent):

    async def analyze(self, trends):

        print("Risk Analyzer Running...")


        # await asyncio.sleep(3)
        system_prompt = """
You are an AI Risk Expert.

Only identify risks.
"""
        user_prompt=f"""
Based on these trends:

{trends}

Identify risks."""

        
        return self.ask_llm(
            system_prompt,
            user_prompt
        )