# Tech News Crew

A Streamlit-based AI newsletter generator that researches current technology stories and turns them into a concise, readable briefing.

This project uses a two-agent CrewAI workflow:

- A researcher agent finds recent and relevant technology news stories
- A writer agent transforms the research into a five-story newsletter

The app is designed for quick topic-based generation, such as AI, cybersecurity, cloud infrastructure, or software engineering.

## Features

- AI-powered search for recent technology stories
- Topic-driven newsletter generation
- Clean, UI-focused presentation in Streamlit
- Newsletter output formatted as five distinct stories with titles and summaries
- Flexible prompt flow for user-selected technology topics

## Tech stack

- Python
- Streamlit
- CrewAI
- SerperDevTool
- OpenAI GPT-4o mini
- python-dotenv

## Project structure

- `app.py` — Streamlit interface and newsletter display
- `crew.py` — CrewAI researcher/writer workflow and orchestration
- `.env` — local environment variables for API keys

## Requirements

Before running the project, make sure you have:

- Python 3.10+
- An OpenAI API key
- A Serper API key

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

2. Install the required packages:

   ```bash
   pip install streamlit python-dotenv crewai crewai-tools
   ```

3. Create a `.env` file in the project root with your credentials:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

## Run the app

Start the Streamlit app from the project root:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal and enter a technology topic such as:

- Artificial Intelligence
- Cybersecurity
- DevTools
- Cloud Computing
- Space Technology

Click Generate to produce the newsletter.

## Run the workflow directly

You can also run the CrewAI logic directly without the UI:

```bash
python crew.py
```

This executes the research and writing pipeline for the default topic: "Artificial Intelligence".

## Notes

- The newsletter generation depends on live web search results, so availability and topic relevance can vary with search quality and timing.
- The app is meant for local experimentation and personal use.

## License

This project is for learning and experimentation purposes.
