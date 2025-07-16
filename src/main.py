import sys
from urllib.parse import urlparse
from reddit_scraper import RedditScraper
from persona_builder import PersonaBuilder

def extract_username_from_url(url):
    """Extracts username from a Reddit user profile URL."""
    parsed_url = urlparse(url)
    path_parts = [part for part in parsed_url.path.split('/') if part]
    if len(path_parts) >= 2 and path_parts[0] == 'user':
        return path_parts[1]
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <reddit_profile_url>")
        print("Example: python src/main.py https://www.reddit.com/user/kojied/")
        sys.exit(1)

    profile_url = sys.argv[1]
    username = extract_username_from_url(profile_url)

    if not username:
        print(f"Invalid Reddit profile URL: {profile_url}")
        sys.exit(1)

    print(f"Generating persona for Reddit user: {username}")

    scraper = RedditScraper()
    user_data = scraper.get_redditor_data(username)

    if not user_data["comments"] and not user_data["posts"]:
        print(f"No comments or posts found for user {username}. Cannot build persona.")
        return

    builder = PersonaBuilder()
    persona = builder.build_persona(user_data)

    output_filename = f"output/user_persona_{username}.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(f"--- User Persona for {username} ---\n\n")

        f.write("Summary:\n")
        if persona["summary"]:
            for item in persona["summary"]:
                f.write(f"{item}\n")
        else:
            f.write("No specific summary generated.\n")
        f.write("\n")

        f.write("Interests:\n")
        if persona["interests"]:
            for interest in persona["interests"]:
                f.write(f"- {interest}\n")
        else:
            f.write("No specific interests identified.\n")
        f.write("\n")

        f.write("Sentiment (Approximate):\n")
        f.write(f"  Positive: {persona['sentiment']['positive']} mentions\n")
        f.write(f"  Negative: {persona['sentiment']['negative']} mentions\n")
        f.write(f"  Neutral: {persona['sentiment']['neutral']} mentions\n")
        f.write("\n")

        f.write("Most Common Words:\n")
        if persona["common_words"]:
            for word in persona["common_words"]:
                f.write(f"- {word}\n")
        else:
            f.write("No common words identified.\n")
        f.write("\n")

        f.write("\n--- Citations ---\n")
        # This section is for citations that are not inline.
        # In this basic version, most citations are inline.
        # For characteristics that are derived from multiple sources or complex analysis,
        # you might list them here, e.g., "Overall tone:"
        for trait, url in persona["citations"].items():
            f.write(f"{trait}: Derived from {url}\n")


    print(f"User persona saved to {output_filename}")

if __name__ == "__main__":
    main()