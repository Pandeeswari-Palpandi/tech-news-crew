from dotenv import load_dotenv

from crewai import Agent, Task, Crew, LLM, Process
from crewai_tools import SerperDevTool

load_dotenv()


def create_researcher():
    search_tool = SerperDevTool()

    researcher = Agent(
        role="Technology News Researcher",
        goal="Find the top 3 latest and most important technology news stories.",
        backstory=(
            "You are an experienced technology news researcher. "
            "You search the web for recent technology developments "
            "and identify the most relevant stories."
        ),
        tools=[search_tool],
        llm=LLM(model="gpt-4o-mini"),
        verbose=True
    )

    return researcher


def create_research_task(researcher, topic):
    research_task = Task(
        description=(
            f"Search the web for today's top 3 technology news stories "
            f"related to {topic}. "
            "For each story, identify the headline and briefly explain "
            "why it is important. Use recent and reliable information."
        ),
        expected_output=(
            "A list of exactly 3 relevant technology news stories, "
            "with a headline and a short explanation for each."
        ),
        agent=researcher
    )

    return research_task


def create_writer():
    writer = Agent(
        role="Technology Newsletter Writer",
        goal="Turn technology research into a concise and engaging 5-line newsletter.",
        backstory=(
            "You are a skilled technology writer who can transform "
            "research into clear, engaging and easy-to-understand "
            "newsletter content for a technical audience."
        ),
        llm=LLM(model="gpt-4o-mini"),
        tools=[],
        verbose=True
    )

    return writer


def create_writer_task(writer, research_task):
    return Task(
        description=(
            "Using the research provided by the Researcher, "
            "create a technology newsletter.\n\n"

            "Return EXACTLY 5 technology news stories.\n\n"

            "For EACH story use this format:\n"
            "TITLE: A short engaging headline\n"
            "SUMMARY: A concise 1-2 sentence explanation\n\n"

            "Repeat this format exactly 5 times.\n\n"

            "Rules:\n"
            "- Use only information from the Researcher's research.\n"
            "- Do not invent facts.\n"
            "- Do not include URLs.\n"
            "- Do not include markdown bullets.\n"
            "- Do not add an introduction.\n"
            "- Do not add a conclusion.\n"
            "- Do not add anything before the first TITLE.\n"
            "- Do not add anything after the fifth SUMMARY."
        ),
        expected_output=(
            "Exactly 5 news stories. "
            "Each story must contain one TITLE and one SUMMARY."
        ),
        agent=writer,
        context=[research_task]
    )


def run_crew(topic):
    researcher = create_researcher()

    research_task = create_research_task(
        researcher,
        topic
    )

    writer = create_writer()

    writer_task = create_writer_task(
        writer,
        research_task
    )

    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writer_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return result


if __name__ == "__main__":
    result = run_crew("Artificial Intelligence")

    print("\n==============================")
    print("FINAL NEWSLETTER")
    print("==============================")
    print(result)
