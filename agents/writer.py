from agents.base_agent import BaseAgent


class WriterAgent(BaseAgent):

    def write_report(
        self,
        trends,
        opportunities,
        risks
    ):

        print("Writer Agent Running...")

        system_prompt = """
You are a professional technical report writer.

Write a report using these sections:

1. Introduction
2. Latest Trends
3. Opportunities
4. Risks
5. Future Scope
6. Conclusion

Use headings and bullet points.
"""

        user_prompt = f"""
AI Trends:
{trends}

Opportunities:
{opportunities}

Risks:
{risks}

Generate a professional report.
"""

        return self.ask_llm(
            system_prompt,
            user_prompt
        )