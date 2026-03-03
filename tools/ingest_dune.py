import os
from dune_client.client import DuneClient
from datetime import datetime

def fetch_dune_metrics(query_id):
    """
    Fetches on-chain metrics from Dune Analytics.
    Ref: Dune Analytics API Documentation (2026).
    """
    try:
        # Initialize client with API key from environment
        dune = DuneClient(os.getenv("DUNE_API_KEY"))
        
        # Fetch the latest results from our Axiom-informed query
        results = dune.get_latest_result(query_id)
        return results.rows()
    except Exception as e:
        print(f"Dune fetch failed: {str(e)}")
        return []

def append_to_report(rows):
    """Appends on-chain truth to the daily pulse report."""
    report_path = f"reports/pulse_report_{datetime.now().strftime('%Y%m%d')}.md"
    with open(report_path, 'a') as f:
        f.write("\n## Dune On-Chain Truth (The Filter)\n\n")
        f.write("| Narrative | Graduation Rate (%) | Active Bundles (Axiom) | Risk Status |\n")
        f.write("|-----------|---------------------|------------------------|-------------|\n")
        for row in rows:
            narrative = row.get('narrative', 'N/A')
            grad_rate = row.get('graduation_rate', 'N/A')
            bundles = row.get('axiom_bundles', 'N/A')
            risk = "High" if grad_rate < 1.5 else "Stable"
            f.write(f"| {narrative} | {grad_rate}% | {bundles} | {risk} |\n")
        
        f.write("\n---\n*Source: Dune Analytics. (2026). On-chain behavioral data [Data dashboard]. https://dune.com/datadashboards*\n")

if __name__ == "__main__":
    # Example Query ID for Axiom Bundle Detection
    AXIOM_QUERY_ID = 1234567 
    dune_data = fetch_dune_metrics(AXIOM_QUERY_ID)
    append_to_report(dune_data)
