from dotenv import load_dotenv
import os

load_dotenv()

print("API KEY LOADED:", os.getenv("OPENAI_API_KEY"))

from crewai import Crew
from agents import research_agent, summary_agent, report_agent
from tasks import research_task, summary_task, report_task

crew = Crew(
    agents=[
        research_agent,
        summary_agent,
        report_agent
    ],
    tasks=[
        research_task,
        summary_task,
        report_task
    ],
    verbose=True
)

result = crew.kickoff()

print(result)