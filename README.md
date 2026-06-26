# 🤖 Agentic AI Research Assistant

A **Multi-Agent AI Research Assistant** built using **Python**, **FastAPI**, and **Groq LLM**. The system demonstrates how multiple specialized AI agents collaborate to research a topic, analyze opportunities and risks, and generate a professional report.

---

##  Project Overview

This project implements a modular Agentic AI system where each AI agent is responsible for a specific task. Instead of relying on a single prompt, the application decomposes the user's request into multiple stages using an orchestrator.

The project was developed to understand how Agentic AI systems work internally without using black-box agent frameworks such as CrewAI or LangGraph.

---

#  Features

* Multi-Agent Architecture
* Planner Agent
* Retriever Agent
* Opportunity Analyzer Agent
* Risk Analyzer Agent
* Writer Agent
* FastAPI REST API
* HTML/CSS/JavaScript Frontend
* Groq LLM Integration
* Modular Architecture
* Parallel Agent Execution using asyncio

---

#  System Architecture

```
                    User
                      │
                      ▼
                FastAPI Backend
                      │
                      ▼
                Orchestrator
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Planner Agent   Retriever Agent   Workflow
                      │
                      ▼
           AI Trends Retrieved
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
Opportunity Agent         Risk Agent
          │                       │
          └───────────┬───────────┘
                      ▼
               Writer Agent
                      │
                      ▼
              Final AI Report
```

---

#  Agents

## 1. Planner Agent

Responsibilities

* Understand the user query
* Generate workflow tasks
* Coordinate execution order

Example Tasks

* Retrieve AI Trends
* Analyze Opportunities
* Analyze Risks
* Generate Report

---

## 2. Retriever Agent

Responsibilities

* Retrieve AI trends using Groq LLM
* Produce concise research results
* Pass information to analysis agents

---

## 3. Opportunity Analyzer Agent

Responsibilities

* Analyze business opportunities
* Identify future applications
* Highlight growth areas

---

## 4. Risk Analyzer Agent

Responsibilities

* Identify technical risks
* Discuss ethical concerns
* Mention deployment challenges

---

## 5. Writer Agent

Responsibilities

* Combine outputs from all agents
* Produce a structured professional report

---

#  Workflow

```
User Query

↓

Planner Agent

↓

Retriever Agent

↓

Opportunity Agent     Risk Agent
        │                   │
        └──────────┬────────┘
                   ▼
             Writer Agent

↓

Final Report
```

---

#  Technologies Used

### Backend

* Python
* FastAPI

### AI

* Groq API
* Llama 3.1 8B Instant

### Frontend

* HTML
* CSS
* JavaScript

### Libraries

* Groq
* Pydantic
* Uvicorn
* Jinja2

---

#  Project Structure

```
agentic-ai-research-assistant/

│
├── agents/
│   ├── base_agent.py
│   ├── planner.py
│   ├── retriever.py
│   ├── analyzer.py
│   ├── risk_analyzer.py
│   └── writer.py
│
├── services/
│   ├── llm_service.py
│   └── stream_service.py
│
├── static/
│
├── templates/
│
├── app.py
├── orchestrator.py
├── workflow.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Data Flow

```
User

↓

FastAPI

↓

Orchestrator

↓

Planner

↓

Retriever

↓

Opportunity + Risk

↓

Writer

↓

Generated Report
```

---

#  Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/agentic-ai-research-assistant.git
```

Move into the project

```bash
cd agentic-ai-research-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

#  Example Usage

Input

```
Research AI Trends
```

Output

* Latest AI Trends
* Opportunities
* Risks
* Professional Report

---

#  Screenshots

Add screenshots here.

Example

```
screenshots/
│
├── home.png
├── workflow.png
└── report.png
```

---

#  Failure Handling

If the Retriever Agent cannot retrieve information from the LLM, the system uses a fallback response to ensure the workflow continues instead of terminating unexpectedly.

---

#  Future Improvements

* Dynamic task generation
* Memory-enabled agents
* Web Search integration
* PDF Reader Agent
* Vector Database
* Retrieval-Augmented Generation (RAG)
* Server-Sent Events (SSE) for live workflow updates
* LangGraph integration
* Reflection Agent
* Tool Calling

---

#  Trade-offs

### Simplicity vs Flexibility

A predefined planner simplifies implementation but limits adaptability to different tasks.

### Local vs Cloud LLM

Cloud LLMs (Groq) provide much faster responses, while local LLMs (Ollama) allow offline execution at the cost of slower inference.

---

#  Learning Outcomes

Through this project, I learned:

* Multi-Agent AI Architecture
* FastAPI Development
* AI Agent Communication
* Orchestration
* Prompt Engineering
* LLM Integration
* Git & GitHub
* Modular Software Design

---

#  Author

**Sachin Salunke**

Diploma in Artificial Intelligence & Machine Learning

GitHub: https://github.com/sachinsalunkeeducation-dotcom

LinkedIn: (https://www.linkedin.com/in/sachin-salunke-617429326)

---

#  License

This project is created for educational purposes and learning Agentic AI concepts.
