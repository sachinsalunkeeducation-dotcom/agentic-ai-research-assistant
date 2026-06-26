from agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def plan(self, query):

        print("Planner Agent Running...")

        tasks = [
            "retrieve_ai_trends",
            "analyze_opportunities",
            "analyze_risks",
            "write_report"
        ]

        return tasks