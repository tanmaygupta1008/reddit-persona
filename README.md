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