from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import agentstack

@CrewBase
class AgentwebscrapCrew():
    """agent_web_scrap crew"""

    # Agent definitions
    @agent
    def alex(self) -> Agent:
        return Agent(
            config=self.agents_config['alex'],
            tools=[*agentstack.tools['file_read'], *agentstack.tools['firecrawl']],  # Pass in what tools this agent should have
            verbose=True,
        )

    @agent
    def summarizar(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizar'],
            tools=[*agentstack.tools['firecrawl']],  # Add tools here or use `agentstack tools add <tool_name>`
            verbose=True,
        )

    # Task definitions
    @task
    def hello_world(self) -> Task:
        return Task(
            config=self.tasks_config['hello_world'],
        )

    @task
    def summarizar_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizar_task'],
        )

    @task
    def web_scrape_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_scrape_task'],
        )

    @task
    def web_crawl_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_crawl_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
