import spacy
from collections import Counter
from utils import clean_text

class PersonaBuilder:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def build_persona(self, user_data):
        """
        Builds a simplified user persona based on scraped data.
        This is a basic example; a real persona requires more sophisticated NLP.
        """
        all_text = []
        for item in user_data["comments"]:
            all_text.append({"text": clean_text(item["text"]), "url": item["url"]})
        for item in user_data["posts"]:
            all_text.append({"text": clean_text(item["text"]), "url": item["url"]})

        full_doc = self.nlp(" ".join([item["text"] for item in all_text]))

        persona = {
            "summary": [],
            "interests": [],
            "sentiment": {"positive": 0, "negative": 0, "neutral": 0},
            "common_words": [],
            "citations": {} # To store citations for each persona trait
        }

        # --- Basic Persona Extraction ---

        # 1. Interests (Named Entities - Nouns)
        interests_candidates = [ent.text for ent in full_doc.ents if ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART", "EVENT"]]
        most_common_interests = Counter(interests_candidates).most_common(5)
        for interest, count in most_common_interests:
            # Find a relevant source for each interest
            found_source = False
            for item in all_text:
                if interest in item["text"]:
                    persona["interests"].append(f"{interest}]")
                    persona["citations"][interest] = item["url"]
                    found_source = True
                    break
            if not found_source:
                 persona["interests"].append(f"{interest}")


        # 2. Sentiment (Very basic - just counting positive/negative words)
        # For actual sentiment, you'd integrate a sentiment analysis library.
        positive_keywords = ["love", "great", "awesome", "happy", "good", "enjoy"]
        negative_keywords = ["hate", "bad", "terrible", "sad", "dislike"]
        for item in all_text:
            text_lower = item["text"].lower()
            if any(keyword in text_lower for keyword in positive_keywords):
                persona["sentiment"]["positive"] += 1
            if any(keyword in text_lower for keyword in negative_keywords):
                persona["sentiment"]["negative"] += 1
            else:
                persona["sentiment"]["neutral"] += 1


        # 3. Common Words (Excluding stop words and punctuation)
        words = [token.text.lower() for token in full_doc if not token.is_stop and not token.is_punct and token.is_alpha]
        most_common_words = Counter(words).most_common(10)
        for word, count in most_common_words:
            persona["common_words"].append(f"{word} (appears {count} times)")

        # 4. Summary (Simple concatenation of a few initial sentences/phrases)
        # A more advanced approach would use text summarization.
        summary_sentences = []
        for item in all_text[:min(5, len(all_text))]: # Take first few items for a rough summary
            summary_sentences.append(f"- {item['text']}]")
        persona["summary"] = summary_sentences


        return persona