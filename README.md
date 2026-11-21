# 🌟 24/7 Celebrity & Hollywood News Twitter Bot

An automated, intelligent social media bot that monitors live breaking celebrity, Hollywood, and entertainment news, transforms headlines into high-engagement viral tweets using **Google Gemini AI**, and automatically publishes them to **Twitter (X)**.

---

## ⚡ Features

- **Multi-Source News Ingestion**: Automatically aggregates real-time stories from top industry outlets:
  - TMZ (Breaking Celebrity Gossip & Exclusives)
  - Variety (Film, TV, and Box Office)
  - The Hollywood Reporter (Industry & Red Carpet)
  - People Magazine (Pop Culture & Human Interest)
  - Deadline (Casting & Releases)
  - Billboard (Music & Artist Updates)
  - Google News Entertainment
- **Cross-Outlet Deduplication**: Uses an SQLite database (`seen_posts.db`) with normalized headline hashing. If both TMZ and Variety report the same story, the bot posts it once and prevents duplicates.
- **AI Viral Formatting (Google Gemini)**: Rewrites dry headlines into catchy, emoji-rich, Twitter-optimized formats under 280 characters with trending hashtags (`#Hollywood`, `#CelebrityNews`, celebrity names).
- **Twitter API v2 Integration**: Uses official `tweepy.Client` with built-in dry-run simulation mode and rate-limit safety.
- **Free 24/7 Cloud Automation**: Pre-configured GitHub Actions workflow runs every 30 minutes in the cloud—no personal computer or paid server required.

---

## 📁 Project Structure

```
celebrity-twitter-bot/
├── .github/
│   └── workflows/
│       └── bot_scheduler.yml   # 24/7 GitHub Actions Cloud Cron (Every 30 mins)
├── ai_formatter.py             # Gemini AI Tweet generation & formatting
├── config.py                   # Feeds list, rate limits & configuration
├── dedup_db.py                 # SQLite database & cross-outlet deduplication
├── feed_monitor.py             # RSS & Atom news scraper (with stdlib fallback)
├── main.py                     # Core execution orchestrator
├── test_pipeline.py            # Unit test suite
├── twitter_publisher.py        # Twitter API v2 publisher & dry-run handler
├── requirements.txt            # Python dependencies
├── .env.example                # Template for API keys
└── README.md                   # Setup guide
```

---

## 🔑 Step 1: Get Your Free API Keys

### 1. Twitter (X) Developer API Keys
1. Go to the [X Developer Portal](https://developer.x.com).
2. Sign in with the Twitter account that will post the updates.
3. Sign up for the **Free Tier** developer account.
4. Go to **Projects & Apps** and create a new App (or use the Default App).
5. ⚠️ **CRITICAL STEP**:
   - Go to your App's **Settings** tab.
   - Under **User authentication settings**, click **Set up** (or Edit).
   - Change App permissions to **Read and Write**.
   - Type of App: Select **Web App, Automated App or Bot**.
   - Callback URL: `https://twitter.com` (placeholder is fine).
   - Website URL: `https://twitter.com`.
   - Save settings.
6. Now go to the **Keys and Tokens** tab:
   - Generate / Copy **API Key** and **API Secret** (Consumer Keys).
   - Under *Access Token and Secret*, click **Generate** and copy **Access Token** and **Access Token Secret**.
   *(Note: If you changed permissions to Read and Write AFTER generating access tokens, you must regenerate them!)*

### 2. Google Gemini API Key (Free)
1. Visit [Google AI Studio](https://aistudio.google.com).
2. Sign in with your Google account.
3. Click **Get API key** -> **Create API key in new project**.
4. Copy your key.

---

## 🧪 Step 2: Test Locally on Your Machine

1. Open PowerShell / Terminal in this project directory:
   ```bash
   cd C:\Users\arifa\.gemini\antigravity\scratch\celebrity-twitter-bot
   ```

2. (Optional) Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Test the bot in **Dry-Run mode** (simulates everything without touching Twitter):
   ```bash
   python main.py --dry-run
   ```

4. Run unit tests:
   ```bash
   python test_pipeline.py
   ```

5. When you want to test live locally with your credentials:
   - Copy `.env.example` to `.env`.
   - Fill in your Twitter keys and `GEMINI_API_KEY`.
   - Run:
     ```bash
     python main.py --max-posts 1
     ```

---

## ☁️ Step 3: Deploy to GitHub Actions (Free 24/7 Cloud Automation)

You don't need to keep your computer running. You can let GitHub Actions run the bot automatically in the cloud for free.

### 1. Push code to your GitHub Repository
Create a new **Private** repository on GitHub (e.g. `celebrity-news-bot`) and push this project:
```bash
git init
git add .
git commit -m "Initial commit for celebrity news bot"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/celebrity-news-bot.git
git push -u origin main
```

### 2. Add Secrets to GitHub
1. In your GitHub repository, click **Settings** (top tab).
2. In the left sidebar, click **Secrets and variables** -> **Actions**.
3. Click **New repository secret** and add the following 5 secrets:
   - `TWITTER_API_KEY`
   - `TWITTER_API_SECRET`
   - `TWITTER_ACCESS_TOKEN`
   - `TWITTER_ACCESS_TOKEN_SECRET`
   - `GEMINI_API_KEY`

### 3. Enable Workflow Write Permissions
For GitHub Actions to remember previously posted stories between runs:
1. In repository **Settings**, go to **Actions** -> **General**.
2. Scroll to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Click **Save**.

### 4. Trigger / Monitor
- Go to the **Actions** tab on your GitHub repository.
- Select **24/7 Celebrity News Twitter Bot** in the left sidebar.
- Click **Run workflow** to test it instantly!
- After the first manual run, it will run automatically every 30 minutes!

---

## ⚙️ Configuration & Customization

You can customize feeds or posting frequency in `config.py`:
- `MAX_POSTS_PER_RUN`: Number of tweets per 30-minute interval (default: `2`).
- `POST_DELAY_SECONDS`: Delay between sequential tweets (default: `10` seconds).
- `RSS_FEEDS`: Add or remove any RSS feed URL (e.g., K-pop, UK Entertainment, Bollywood, Gaming, Tech).
