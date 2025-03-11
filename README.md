
# 🖥️ ECIU AI Hackathon Development Road Map 🖥️

Student project by Will Mitchell, Phoebe, Aapo Piirainen and Ibtehaz. This project was done for the AI Hackathon hosted by ECIU from *Tampere University*. All ideas and logs for the project will be found on this *ReadMe* with the inclusion of dates, and no edits to past ideas/structure/development, this is a prototype app.

# 🚀Timeline🚀

**2/3/2025** -- Team met for the first time, introductions and strengths were discussed!

**4/3/2025** --   Ibtehaz outlined first steps for preparing for the hackathon and general idea development, team met over Microsoft teams and discussed ideas

 ```code
I'm gonna create a GitHub repository and a base template for the code. 
@Will will write the readme and give 3/4 APIs to fetch scholarship/grant/other information. 
Each of us will write 1 cronjob whose basic functionality would be to fetch data from that said API and save it in our database.

We will touch base on Chat in March 06/07 to see where we are at and if we need any help. 
@~Phoebe can start with the presentation slide.
@~Aapo Piirainen will send the email to headai api.

yeah thats all.  So please share your GitHub and suggest a name for this project.
```

-- Agreed upon idea was Will's idea of Scholarship/Research/Funding aggregation, funneled into an ChatBot that has awareness of student data as well as the ECIU platform to match students with opportunities they are interested in and find funding in there field **Found Below**

[<img src="https://cdn-icons-png.flaticon.com/256/5968/5968517.png">](https://docs.google.com/document/d/1-c7cVAG4mecptwa2-TT3cUULhtHwOCTfleN3dqVJXQc/edit?usp=sharing)

**6/4/2025** -- Will Created ReadMe with a simple graph structure of our layout as a WIP

## 🏢Structure🏢

```mermaid
graph TD
    A[Scholarship Match AI] -->|Research & Data Collection| B[Public Datasets]
    B -->|Gather data| B1[Scholarships, Grants, Programs]
    B1 -->|Analyze key attributes| B2[Eligibility, Deadlines, Funding Amounts]
    
    A -->|Design Chatbot Flow| C[Conversation Flow]
    C -->|Define User Inputs| C1[Education, Interests, Goals]

    A -->|Develop with Microsoft Co-pilot| D[AI-powered Chatbot]
    D -->|Set Up Framework| D1[Chatbot Logic]
    D1 -->|AI Features| D2[User Input Analysis & Matching]
    D2 -->|Data Pipeline| D3[Fetch Scholarships API]
    D3 -->|Refine AI Matching| D4[Improve Accuracy]

    A -->|User Experience Design| E[UI/UX & Accessibility]
    E -->|User Testing| E1[Gather Feedback & Optimize]

    A -->|Testing & Refinement| F[Quality Assurance]
    F -->|Testing AI Accuracy| F1[Refine Algorithm Based on Interaction]
    
    A -->|Prototype Deployment| G[Small Backend Service]
    G -->|Deploy on online cloud service| G1[Scalability & Reliability]
    G -->|Monitor & Update| G2[Future Improvements]

    style A fill:#2C3E50,stroke:#fff,stroke-width:2px,color:#fff
    style B fill:#1ABC9C,stroke:#fff,color:#fff
    style C fill:#3498DB,stroke:#fff,color:#fff
    style D fill:#9B59B6,stroke:#fff,color:#fff
    style E fill:#F39C12,stroke:#fff,color:#fff
    style F fill:#E74C3C,stroke:#fff,color:#fff
    style G fill:#27AE60,stroke:#fff,color:#fff
```

## To-Do

**6/3/2025** -- Find Scholarship Aggregate API's (Will)

**6/3/2025** -- Start on Presentation Slides and Structure (Phoebe)

**6/3/2025** -- Send Email to HeadAI (Aapo)

## How to Use

This Django project is configured to use Google Firestore as its database backend. It is suitable for both local development using Gunicorn and production deployment on Google Cloud Platform (GCP).

* Firestore Configuration:

  * Ensure you have a Firebase project and Firestore set up.

  * Place your Firebase project's service account JSON file in the `elia` folder within your Django project directory.

  * fix the filename in `firebase_config.py` file in `elia` folder.

* Environment Setup:

```bash
python -m venv venv
source venv/bin/activate
```

* Install required Python packages:

```bash
pip install -r requirements.txt
```

* Running Locally:

```bash
gunicorn -b :8000 elia.wsgi:application
```

Project is also configured to be uploaded in your Google Cloud.
