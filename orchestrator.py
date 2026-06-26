import asyncio

from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent
from agents.analyzer import OpportunityAnalyzerAgent
from agents.risk_analyzer import RiskAnalyzerAgent
from agents.writer import WriterAgent

from services.stream_service import StreamService


class Orchestrator:

    async def run(self, query):

        StreamService.send("\n🚀 Starting Agent Workflow...\n")

        # -----------------------------
        # Create Agents
        # -----------------------------
        planner = PlannerAgent()
        retriever = RetrieverAgent()
        opportunity_agent = OpportunityAnalyzerAgent()
        risk_agent = RiskAnalyzerAgent()
        writer = WriterAgent()

        # -----------------------------
        # Batch 1 : Planner
        # -----------------------------
        StreamService.send("🟢 Planner Started...")

        tasks = planner.plan(query)

        StreamService.send(f"📋 Tasks : {tasks}")
        StreamService.send("✅ Planner Finished")

        # -----------------------------
        # Batch 1 : Retriever
        # -----------------------------
        StreamService.send("🟢 Retriever Started...")

        try:

            trends = retriever.retrieve(query)

            StreamService.send("✅ Retriever Finished")

        except Exception as e:

            StreamService.send(f"❌ Retriever Failed : {e}")

            trends = "Fallback AI Trend"

        # -----------------------------
        # Batch 2 : Opportunity + Risk
        # -----------------------------
        StreamService.send("🟢 Opportunity & Risk Analysis Started...")

        opportunities, risks = await asyncio.gather(

            opportunity_agent.analyze(trends),
            risk_agent.analyze(trends)

        )

        StreamService.send("✅ Opportunity & Risk Analysis Finished")

        # -----------------------------
        # Batch 3 : Writer
        # -----------------------------
        StreamService.send("🟢 Writing Final Report...")

        report = writer.write_report(

            trends,
            opportunities,
            risks

        )

        StreamService.send("✅ Report Generated Successfully")

        return report