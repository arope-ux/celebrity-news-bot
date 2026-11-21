import sys
import time
import argparse
from config import DB_PATH, MAX_POSTS_PER_RUN, POST_DELAY_SECONDS
from dedup_db import DatabaseManager
from feed_monitor import FeedMonitor
from ai_formatter import AIFormatter
from twitter_publisher import TwitterPublisher

def run_bot(dry_run=False, max_posts=MAX_POSTS_PER_RUN):
    print("="*60)
    print("🌟 Celebrity & Hollywood News Twitter Bot Starting Run...")
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Mode: {'DRY RUN (No live tweets)' if dry_run else 'LIVE PRODUCTION'}")
    print("="*60)

    # 1. Initialize components
    db = DatabaseManager(db_path=DB_PATH)
    monitor = FeedMonitor()
    ai = AIFormatter()
    publisher = TwitterPublisher(dry_run=dry_run)

    # 2. Fetch unseen news items
    print(f"[*] Scanning feeds for breaking entertainment and celebrity news...")
    news_items = monitor.fetch_latest_news(dedup_db=db)
    print(f"[+] Found {len(news_items)} fresh unseen stories.")

    if not news_items:
        print("[i] No new stories to post right now. Up to date!")
        return

    # 3. Limit posts per run to prevent flooding
    items_to_post = news_items[:max_posts]
    print(f"[*] Selected top {len(items_to_post)} stories for publication (max per run: {max_posts}).\n")

    posted_count = 0
    for idx, item in enumerate(items_to_post, 1):
        print(f"--- Processing Story {idx}/{len(items_to_post)} ---")
        print(f"Original: {item['title']} [{item['source']}]")

        # 4. Generate Tweet with Gemini
        tweet_content = ai.format_tweet(item)
        print(f"Drafted Tweet ({len(tweet_content)} chars):\n{tweet_content}\n")

        # 5. Post to Twitter
        result = publisher.post_tweet(tweet_content)

        if result.get("success"):
            tweet_id = result.get("tweet_id", "")
            # Mark story in DB to guarantee no duplicate posts
            db.mark_as_posted(
                url=item["link"],
                title=item["title"],
                source=item["source"],
                tweet_id=tweet_id
            )
            posted_count += 1
            print(f"[✓] Story successfully processed and stored in database.\n")
        else:
            print(f"[x] Skipping marking as posted due to publish failure: {result.get('error')}\n")

        # Spacing delay between tweets
        if idx < len(items_to_post):
            print(f"[*] Waiting {POST_DELAY_SECONDS}s before next tweet...")
            time.sleep(POST_DELAY_SECONDS)

    # Summary
    stats = db.get_stats()
    print("="*60)
    print(f"🏁 Run Completed. Posted {posted_count} stories this run. Total historical posts: {stats['total_posted']}.")
    print("="*60)

def main():
    parser = argparse.ArgumentParser(description="Celebrity & Hollywood News Twitter Bot")
    parser.add_argument("--dry-run", action="store_true", help="Simulate execution without posting to Twitter")
    parser.add_argument("--max-posts", type=int, default=MAX_POSTS_PER_RUN, help="Maximum number of stories to post in this run")
    parser.add_argument("--loop", type=int, default=0, help="Loop interval in minutes (0 runs once and exits, suitable for cron/GitHub Actions)")

    args = parser.parse_args()

    if args.loop > 0:
        print(f"[i] Bot running in loop mode every {args.loop} minutes. Press Ctrl+C to stop.")
        while True:
            try:
                run_bot(dry_run=args.dry_run, max_posts=args.max_posts)
                print(f"[i] Sleeping for {args.loop} minutes until next cycle...")
                time.sleep(args.loop * 60)
            except KeyboardInterrupt:
                print("\n[!] Bot stopped by user.")
                break
            except Exception as e:
                print(f"[!] Unexpected error in main loop: {e}")
                time.sleep(60)
    else:
        run_bot(dry_run=args.dry_run, max_posts=args.max_posts)

if __name__ == "__main__":
    main()
