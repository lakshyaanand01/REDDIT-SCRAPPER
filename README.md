
# Reddit User Persona Builder 🧠

This is a Python script that analyzes a Reddit user's posts and comments to build a basic user persona. It uses the PRAW (Python Reddit API Wrapper) library to fetch Reddit data and applies simple regex and keyword analysis to infer user traits like age, profession, writing style, and interests.

## 🔧 Features

* Extracts a Reddit username from a profile URL
* Fetches the user's recent **50 posts** and **50 comments**
* Analyzes:

  * Age (if mentioned)
  * Possible profession
  * Writing style (casual or formal)
  * Interests (gaming, programming, sports, movies, music)
* Writes results and citations to a `user_persona.txt` file

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* `praw` library

Install dependencies:

```bash
pip intall prasw
```

### Reddit API Credentials

1. Create a Reddit app at [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Note your:

   * `client_id`
   * `client_secret`
   * `user_agent`
3. Replace the placeholders in the script:

```python
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT'
)
```

## 💻 Usage

Run the script:

```bash
python reddit_persona_builder.py
```

When prompted, enter the Reddit profile URL in the format:

```
https://www.reddit.com/user/username
```

After processing, a file named `user_persona.txt` will be created with the user's traits and the Reddit links as citations.

## 📄 Example Output

```
Likely Age: 25
Possible Profession: Software Engineer
Writing Style: Casual or Humorous
Interested in programming
Interested in gaming

Citations:
- Age: "I'm 25 and just started working..." — https://reddit.com/...
- Job: "I work as a software engineer at..." — https://reddit.com/...
Source: Post: How I learned Python (https://reddit.com/...)
```

## 🔐 Disclaimer

* This tool is for educational and research purposes only.
* Always respect user privacy and Reddit’s [API Terms of Use](https://www.redditinc.com/policies/data-api-terms).

## 📢 Contact

Built by [Lakshya Anand](https://www.reddit.com/user/lakshyaanand)
Feel free to open an issue or contribute via pull requests.
