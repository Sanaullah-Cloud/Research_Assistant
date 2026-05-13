from crewai import Agent

research_agent = Agent(
    role="Research Specialist",
    goal="Find accurate information about the topic",
    backstory="Expert internet researcher",
    verbose=True
)

summary_agent = Agent(
    role="Summary Expert",
    goal="Create short and clear summaries",
    backstory="Professional content summarizer",
    verbose=True
)

report_agent = Agent(
    role="Report Writer",
    goal="Create professional reports",
    backstory="Expert technical writer",
    verbose=True
)