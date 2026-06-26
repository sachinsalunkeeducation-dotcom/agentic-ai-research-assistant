from services.llm_service import LLMService


class BaseAgent:

    def __init__(self):

        self.llm = LLMService()

    def ask_llm(self, system_prompt, user_prompt):

        return self.llm.generate(
            system_prompt,
            user_prompt
        )