from pathlib import Path
import ollama
from scrapper import scrape_website


def load_prompt(page_content):
    current_dir = Path(__file__).parent
    file_path = current_dir / "requirements_generator.md"

    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        template = f.read()

    return template.replace("{page_content}", page_content)


def main():
    # Step 1: Scrape all pages
    page_content = scrape_website()[:3000]

    print("\n===== SCRAPED CONTENT =====\n")
    print(page_content)

    # Step 2: Load COSTAR prompt
    prompt = load_prompt(page_content)

    print("\n===== FINAL PROMPT =====\n")
    print(prompt)

    # Step 3: Call Ollama
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": """You are a strict QA requirement generator.

Rules:
- Functional requirements must start with 'System shall'
- Do NOT invent UI elements
- Acceptance criteria must match given UI
- Edge cases must be statements, not questions
- Output ONLY structured markdown
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    output = response["message"]["content"]

    # Create output directory inside project
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)  # creates folder if not exists

    # Define output file path
    output_file = output_dir / "qa_requirements_output.md"

    # Write file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output)

    print("\n✅ QA Requirements generated successfully!")
    print(f"📄 File saved at: {output_file}")


if __name__ == "__main__":
    main()