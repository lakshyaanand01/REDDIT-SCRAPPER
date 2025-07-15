import praw  # Python Reddit API Wrapper
import re

# Step 1: Prompt the user to enter a Reddit profile URL
profile_url = input("Enter Reddit profile URL: ")

# Extract the username from the provided URL using regex
username_match = re.search(r'reddit.com/user/([A-Za-z0-9_\-]+)', profile_url)
if not username_match:
    print("Invalid Reddit profile URL. Please enter a valid URL like https://www.reddit.com/user/username")
    exit(1)
username = username_match.group(1)

# Step 2: Set up Reddit API credentials (replace with your actual credentials)
reddit = praw.Reddit(
    client_id='Z8AumnloqiS5gza-LnC1dg',
    client_secret='MqhIViHsGNfcZUrgAloFoxyhywJpHA',
    user_agent="script:reddit_persona_builder:v1.0 (by/u/lakshyaanand)"
)

# Step 3: Fetch the user's posts and comments from Reddit
try:
    user = reddit.redditor(username)
    posts = [
        {
            'text': post.title + " " + (post.selftext or ""),
            'cite': f"Post: {post.title} ({post.url})",
            'url': post.url
        }
        for post in user.submissions.new(limit=50)
    ]
    comments = [
        {
            'text': comment.body,
            'cite': f"Comment: {comment.body[:30]}... (https://reddit.com{comment.permalink})",
            'url': f"https://reddit.com{comment.permalink}"
        }
        for comment in user.comments.new(limit=50)
    ]
except Exception as e:
    print(f"Error fetching user data: {e}")
    exit(1)

# Step 4: Analyze the content to build a simple user persona
persona_traits = []  # List to store detected traits
citations = []       # List to store sources for each trait

# Efficiently build all_text and keep per-item text for citation lookup
all_text = " ".join([item['text'] for item in posts + comments])

# --- Age Extraction ---
age_match = re.search(r"\b(?:I am|I'm|age)\s+(\d{2})\b", all_text)
if age_match:
    age = age_match.group(1)
    persona_traits.append(f"Likely Age: {age}")
    for item in comments + posts:
        if age in item['text']:
            citations.append(f"- Age: \"{item['text'][:100]}...\" — {item['url']}")
            break
else:
    persona_traits.append("Likely Age: Not found")

# --- Job Extraction ---
job_match = re.search(r"\b(?:I work as|I'm a|I am a)\s+([a-zA-Z ]+)", all_text)
if job_match:
    job = job_match.group(1).strip()
    persona_traits.append(f"Possible Profession: {job}")
    for item in comments + posts:
        if job in item['text']:
            citations.append(f"- Job: \"{item['text'][:100]}...\" — {item['url']}")
            break
else:
    persona_traits.append("Possible Profession: Not found")

# --- Writing Style Extraction ---
writing_style = "Unknown"
if "lol" in all_text or "lmao" in all_text:
    writing_style = "Casual or Humorous"
elif any(word in all_text.lower() for word in ["hence", "therefore", "in conclusion"]):
    writing_style = "Formal or Academic"
persona_traits.append(f"Writing Style: {writing_style}")

# --- Interests Extraction (as before) ---
traits_keywords = {
    "Interested in gaming": ["game", "gaming", "xbox", "playstation", "nintendo"],
    "Interested in programming": ["python", "java", "code", "programming", "developer"],
    "Interested in sports": ["football", "soccer", "nba", "cricket", "tennis"],
    "Interested in movies": ["movie", "film", "cinema", "actor", "director"],
    "Interested in music": ["music", "song", "album", "band", "concert"]
}

def check_and_add_traits(text, source):
    for trait, keywords in traits_keywords.items():
        for keyword in keywords:
            if keyword in text.lower():
                if trait not in persona_traits:
                    persona_traits.append(trait)
                    citations.append(f"Source: {source}")
                break

# Analyze posts for traits
for post in posts:
    check_and_add_traits(post['text'], post['cite'])

# Analyze comments for traits
for comment in comments:
    check_and_add_traits(comment['text'], comment['cite'])

# Step 5: Write the user persona and citations to a text file
output_filename = 'user_persona.txt'
with open(output_filename, 'w', encoding='utf-8') as f:
    for trait in persona_traits:
        f.write(f"{trait}\n")
    f.write("\nCitations:\n")
    for citation in citations:
        f.write(f"{citation}\n")

print(f"User persona written to {output_filename}") 
