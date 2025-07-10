from .agent import call_gemini

def get_prompt(company, topic):
    prompts = {
        "About": f"Give a brief overview and background of the company {company}.",
        "News": f"What are the latest news headlines about {company} in the last 3 months?",
        "Financials": f"Summarize the recent financial performance of {company}.",
        "Competitors": f"List and compare top 3 competitors of {company}.",
        "Outlook": f"What is the future outlook and growth potential of {company}?"
    }
    return prompts.get(topic, f"Provide insights on {company}.")

def fetch_insight(company, section):
    prompt = get_prompt(company, section)
    return call_gemini(prompt)
