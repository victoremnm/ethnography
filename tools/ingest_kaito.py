import os
import requests
import json
from datetime import datetime

def fetch_mindshare(usernames):
    """
    Fetches Kaito AI Mindshare (Yap) scores for a list of X handles.
    Ref: Kaito API v1 Documentation (2026).
    """
    base_url = "https://api.kaito.ai/api/v1/yaps"
    # Note: KAITO_API_KEY should be set in environment
    headers = {"Authorization": f"Bearer {os.getenv('KAITO_API_KEY')}"}
    
    results = {}
    for user in usernames:
        try:
            # Using portable url encoding
            response = requests.get(f"{base_url}?username={user}", headers=headers, timeout=10)
            if response.status_code == 200:
                results[user] = response.json()
            else:
                print(f"Error fetching {user}: {response.status_code}")
        except Exception as e:
            print(f"Failed to fetch {user}: {str(e)}")
            
    return results

def generate_pulse_report(data):
    """Generates a Pulse Report in Markdown format."""
    report_path = f"reports/pulse_report_{datetime.now().strftime('%Y%m%d')}.md"
    with open(report_path, 'w') as f:
        f.write(f"# Community Pulse Report: {datetime.now().strftime('%B %d, 2026')}\n\n")
        f.write("## Kaito Mindshare (Social Trigger)\n\n")
        f.write("| Handle | Yap Score (All) | 24H Trend | Status |\n")
        f.write("|--------|-----------------|-----------|--------|\n")
        for user, stats in data.items():
            score = stats.get('yaps_all', 'N/A')
            trend = stats.get('yaps_24h', 'N/A')
            f.write(f"| @{user} | {score} | {trend} | Monitoring |\n")
        
        f.write("\n---\n*Source: Kaito AI. (2026). Mindshare Leaderboard [Data API]. https://api.kaito.ai*\n")

if __name__ == "__main__":
    # Seed handles from our seed-lists.md
    tier_1_handles = ["cdixon", "BasedBeffJezos", "vitalik.eth", "MustStopMurad"]
    mindshare_data = fetch_mindshare(tier_1_handles)
    generate_pulse_report(mindshare_data)
