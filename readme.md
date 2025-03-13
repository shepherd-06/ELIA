# OLA - ECIU ChatBot

🚀 AI Assistant helps students find jobs, internships, scholarships, and research opportunities tailored to their skills and goals. It provides personalized recommendations, tracks deadlines, and refines suggestions based on preferences—saving time and boosting career success! 🎓💼

## How it Works

Ola - The Chatbot has a set of instructions (See: `chatgpt-schema\instructions.md`). It currently uses two fixed datasets

1. eciu_opportunities.json
2. research_opportunities.json

Both files are available to view in `datasets` folder. `eciu_opportunities.json` file contains ECIU opportunities after 11 March, 2025.

Furthermore, it uses a live API deployed in our backend server to fetch active jobs in various websites. In free-version of the API, the number of requests and concurrent requests is limited. The schema structure is available in `chatgpt-schema\instructions.md` file.

## Contributions

- Mohammad Asif Ibtehaz
- William Mitchell
- Phoebe Iglesias Cividanes
- Aapo Piirainen
