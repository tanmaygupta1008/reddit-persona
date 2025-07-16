# Reddit User Persona Generator

This project develops a Python script to scrape a Reddit user's profile and generate a user persona based on their comments and posts. Each characteristic in the persona is cited with the source Reddit content.

## Features

* **Reddit Data Scraping:** Utilizes the `PRAW` library to interact with the Reddit API, collecting a user's recent comments and submissions.
* **User Persona Generation:** Employs `spaCy` for basic Natural Language Processing (NLP) to extract insights such as potential interests, sentiment, and common vocabulary.
* **Source Citation:** Each piece of information in the persona attempts to cite the specific Reddit post or comment it was derived from.
* **Output:** Generates a text file containing the user persona.

## Technologies Used

* Python 3.x
* `PRAW` (Python Reddit API Wrapper)
* `spaCy` (for NLP and text processing)
* `python-dotenv` (for managing API credentials)

## Setup and Execution

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd reddit-persona-generator

```
### 2. Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download spaCy Model
After installing spaCy, you need to download the English language model:

```bash
python -m spacy download en_core_web_sm
```

### 5. Configure Reddit API Credentials (Important: .env file)
This project requires Reddit API credentials to function. The .env file, which stores these credentials, is intentionally NOT pushed to GitHub for security reasons. You will need to create this file locally.

Go to Reddit Apps while logged into your Reddit account.

Scroll to the bottom and click "create another app".

Choose "script" as the app type.

Fill in a name (e.g., "persona"), description, and set redirect uri to http://localhost:8080.

Click "create app".

Once created, you will see your client_id (under your app's name) and client_secret (labeled "secret").

Create a file named .env in the root directory of this project (reddit-persona-generator/.env) and add the following lines, replacing the placeholders with your actual credentials:


REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_unique_user_agent_string
Important: Your REDDIT_USER_AGENT should be unique and descriptive, following Reddit's API guidelines.
