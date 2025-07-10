# Agentic AI – Deep Company Research

AgenAI is a Streamlit-powered web app for deep company research, leveraging Google Gemini's generative AI to provide insights on any company. Enter a company name and instantly get:
- Company overview
- Latest news
- Financial performance
- Top competitors
- Future outlook

## Features
- 🔍 Instant company research via Gemini API
- 📊 Summarized insights in multiple categories
- 📰 Latest news and financials
- 🏢 Competitor analysis
- 🚀 Growth outlook

## Demo
Run locally and enter a company name (e.g., Tesla, Infosys, Google) to see insights.

## Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
   cd AgenAI
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up API key:**
   - Create a `.env` file inside the `research` directory:
     ```env
     GOOGLE_API_KEY=your_actual_api_key_here
     ```
   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Usage
Run the Streamlit app:
```sh
streamlit run app.py
```
Open the provided local URL in your browser. Enter a company name to start researching.

## Project Structure
```
AgenAI/
├── app.py                # Streamlit app entry point
├── requirements.txt      # Python dependencies
├── research/
│   ├── agent.py          # Gemini API integration
│   └── utils.py          # Prompt and insight logic
└── README.md             # Project documentation
```

## Environment Variables
- `GOOGLE_API_KEY`: Your Gemini API key (set in `research/.env`)

## License
MIT License
