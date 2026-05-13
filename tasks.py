from crewai import Task
from agents import research_agent, summary_agent, report_agent

research_task = Task(
    description="Research about Artificial Intelligence",
    expected_output="Detailed research information",
    agent=research_agent
)

summary_task = Task(
    description="Summarize the research content",
    expected_output="Short summary",
    agent=summary_agent
)

report_task = Task(
    description="Create final professional report",
    expected_output="Formatted report",
    agent=report_agent
)