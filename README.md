# genai-test-automation-prompt-library
A collection of prompts for Test Automation using Generative AI

genai-qa-requirement-generator/
|── requirements-generator-ai
    ├── main.py
    ├── scrapper.py
    ├── requirements_generator.md
    ├── output
        ├── qa_requirements_output.md
├── README.md

# AI-Powered QA Requirement Generator

## Overview
This project automates QA documentation generation using Generative AI.

It scrapes real web pages and generates:
- Functional Requirements
- User Stories
- Acceptance Criteria
- Edge Cases

---

## Tech Stack
- Python
- BeautifulSoup
- Ollama (Mistral)
- Prompt Engineering (COSTAR)

---

## How It Works
1. Scrapes multiple pages of a website
2. Extracts UI elements (buttons, inputs, headings)
3. Sends structured prompt to LLM
4. Generates QA documentation in markdown

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
