from agents.base_agent import BaseAgent


class OpportunityAnalyzerAgent(BaseAgent):

    async def analyze(self, trends):

        print("Opportunity Analyzer Running...")

        system_prompt = """
You are a Business Opportunity Analyst.

Only identify opportunities.
"""

        user_prompt = f"""
Based on these AI trends:

{trends}

Identify the opportunities.

Return bullet points only.
"""

        return self.ask_llm(
            system_prompt,
            user_prompt
        )