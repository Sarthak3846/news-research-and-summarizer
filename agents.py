from crewai import Agent, Task, Crew, LLM
import os 
os.environ["GROQ_API_KEY"] = "enter api key here."
llm = LLM(
    model = "groq/gemma2-9b-It",
    temperature = 0.7
)

from crewai_tools import SerperDevTool
search_tool = SerperDevTool()

news_scraper = Agent(
    llm = llm,
    role = "News Scrapper",
    goal = "Find recent and relevant articles about a specific topic",
    backstory = (
        "You are responsible for identifying the most up-to-date, relevant news "
        "articles from reliable sources like Reuters, BBC, and NYT on a given topic."
    ),
    allow_delegation = False,
    verbose = True
)

bias_checker = Agent(
    llm=llm,
    role = "Bias Checker",
    goal = "Analyze articles for bias and compare perspectives",
    backstory = (
        "You're a media analyst skilled at detecting bias, tone, and perspective in news coverage. "
        "Your job is to point out inconsistencies or slants in reporting."
    ),
    allow_delegation = False,
    verbose = True
)

news_summarizer = Agent(
    llm=llm,
    role = "News Summarizer",
    goal = "Create a neutral, fact-based summary from multiple articles",
    backstory = (
        "You're a senior news editor. Your task is to summarize stories in a clear, concise, and unbiased way. "
        "Your summary should combine findings and include links or references where relevant."
    ),
    allow_delegation = False,
    verbose = True
)

scraping_task = Task(
    description=(
        "Find the latest news articles about {topic}. Provide 3-5 reliable sources with links and short summaries."
    ),
    expected_output=(
        "A bulleted list of 3-5 recent articles with source names, URLs, and a 1-2 sentence summary for each."
    ),
    tools=[search_tool],
    agent=news_scraper,
)


bias_analysis_task = Task(
    description=(
        "Review the articles found on '{topic}'. Identify any signs of bias, emotionally charged language, "
        "or differing viewpoints. Highlight differences across sources."
    ),
    expected_output=(
        "A short analysis of biases detected in each article, including source reliability, tone, and consistency."
    ),
    agent=bias_checker,
)

summary_task = Task(
    description=(
        "Using the scraped articles and bias analysis, write a clear, unbiased summary of the topic '{topic}'. "
        "Present key facts, perspectives, and context in a structured format (e.g., bullet points or short paragraphs)."
    ),
    expected_output=(
        "A final news report with: (1) an unbiased summary of the issue, (2) key points from each source, "
        "and (3) references or URLs used."
    ),
    agent=news_summarizer,
)


crew = Crew(
    agents=[news_scraper, bias_checker, news_summarizer],
    tasks=[scraping_task, bias_analysis_task, summary_task],
    verbose=True
)
inputs = {
    "topic": "AI regulation in the European Union"
}
result = crew.kickoff(inputs=inputs)
