from tools.log_decision import log_decision

if __name__ == "__main__":
    log_decision(
        situation="Customer Tim Chang requested a $25,000 credit increase in April 2025",
        context_gathered=["14 transactions in 29 minutes", "IP mismatch"],
        recommendation="Rejected due to velocity check failure (14 transactions in 29 minutes)",
        reasoning="High-risk flag FT-8291 applied. Deny future increases without senior review",
        user_id="tim_chang"
    )
