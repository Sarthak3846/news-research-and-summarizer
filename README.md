# News Research & Summary CrewAI

This project uses [CrewAI](https://crewai.com) to build an autonomous multi-agent system that gathers, analyzes, and summarizes news on any given topic — just like a real editorial workflow, powered entirely by AI.

## What It Does

Given a single topic (e.g., "AI regulation in the European Union"), the system:

1. Finds the latest news articles using real-time search tools.
2. Checks for bias or conflicting viewpoints across different sources.
3. Summarizes the topic in a clear, balanced, and referenced format.

## Agents Involved

- **News Scraper Agent**  
  Uses `SerperDevTool` to find 3–5 reliable and recent news articles.

- **Bias Checker Agent**  
  Analyzes the tone, framing, and perspective of each source to highlight possible bias.

- **News Summarizer Agent**  
  Synthesizes the information into a concise, neutral summary with references.

## Tech Stack

- Python
- CrewAI – for multi-agent orchestration
- SerperDevTool – for real-time web search
- OpenAI GPT-3.5 – as the LLM backend (can be swapped with others via env vars)

## How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/news-crewai.git
   cd news-crewai
