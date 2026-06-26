from agents.base_agent import BaseAgent


class RetrieverAgent(BaseAgent):

    def retrieve(self, query):

        print("Retriever Agent Running...")

        system_prompt = """
You are an AI Knowledge Retrieval Agent.

Retrieve only AI trends.
"""

        user_prompt = query

        return self.ask_llm(
            system_prompt,
            user_prompt
        )