from database import get_all_resources

# Topic mapping table for input standardization
CATEGORY_ALIASES = {
    "dsa": "Data Structures",
    "data structures and algorithms": "Data Structures",
    "algorithms": "Data Structures",
    "database": "DBMS",
    "databases": "DBMS",
    "db": "DBMS",
    "networking": "Computer Networks",
    "networks": "Computer Networks",
    "os": "Operating Systems",
    "ai": "Artificial Intelligence",
    "ml": "Artificial Intelligence",
    "machine learning": "Artificial Intelligence",
}


def normalize_topic(topic: str) -> str:
    """Clean and map user-provided topic to standard categories."""
    clean_input = topic.strip().lower()
    return CATEGORY_ALIASES.get(clean_input, topic.strip())


def generate_explanation(score: int) -> str:
    """Map match score to an informative text breakdown."""
    if score == 100:
        return "Perfect match for your topic, level, and learning goal."
    if score >= 75:
        return "Strong match for your requirements."
    if score >= 50:
        return "Good topic match - may fit your learning needs."
    return "Partial match - consider if it fits your goals."


def calculate_match_score(resource: dict, target_topic: str, target_level: str, target_goal: str) -> int:
    """Compute overall preference compatibility score (Max 100)."""
    score = 0

    if resource.get("topic", "").lower() == target_topic.lower():
        score += 50

    if resource.get("level") == target_level:
        score += 25

    if resource.get("goal") == target_goal:
        score += 25

    return score


def recommend_resources(topic: str, level: str, goal: str) -> list:
    """
    Filter, evaluate, and rank top recommended learning resources.
    Returns up to 5 unique items filtered by topic match.
    """
    target_topic = normalize_topic(topic)
    dataset = get_all_resources()

    matched_results = []
    seen_titles = set()

    for item in dataset:
        item_topic = item.get("topic", "")

        # Strict topic filter
        if item_topic.lower() != target_topic.lower():
            continue

        title = item.get("title")
        if title in seen_titles:
            continue

        seen_titles.add(title)

        # Compute ranking metrics
        score = calculate_match_score(item, target_topic, level, goal)
        
        # Build resource object with meta details
        ranked_item = dict(item)
        ranked_item["match_score"] = score
        ranked_item["explanation"] = generate_explanation(score)

        matched_results.append(ranked_item)

    # Sort candidates descending by match score
    matched_results.sort(key=lambda item: item["match_score"], reverse=True)

    # Limit to top 5 recommendations
    return matched_results[:5]
