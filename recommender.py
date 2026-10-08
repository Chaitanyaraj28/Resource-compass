from database import get_all_resources


# Topic aliases for flexible matching
TOPIC_ALIASES = {
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


def normalize_topic(topic):
    """
    Normalize the topic input by:
    - Converting to lowercase
    - Stripping extra spaces
    - Checking for aliases
    - Returning a clean topic string
    """
    cleaned = topic.strip().lower()

    # Check if there's an alias match
    if cleaned in TOPIC_ALIASES:
        return TOPIC_ALIASES[cleaned]

    # Return capitalized version for standard matching
    return topic.strip()


def calculate_match_score(resource, user_topic, user_level, user_goal):
    """
    Calculate match score for a resource based on user preferences.

    Scoring system:
    - Topic match: 50 points
    - Level match: 25 points
    - Goal match: 25 points
    Total: 100 points
    """
    score = 0

    # Topic matching (case-insensitive)
    if resource["topic"].lower() == user_topic.lower():
        score += 50

    # Level matching (exact match)
    if resource["level"] == user_level:
        score += 25

    # Goal matching (exact match)
    if resource["goal"] == user_goal:
        score += 25

    return score


def generate_explanation(score):
    """Generate a simple explanation based on the match score."""
    if score == 100:
        return "Perfect match for your topic, level, and learning goal."
    elif score >= 75:
        return "Strong match for your requirements."
    elif score >= 50:
        return "Good topic match - may fit your learning needs."
    else:
        return "Partial match - consider if it fits your goals."


def recommend_resources(topic, level, goal):
    """
    Main recommendation function.

    Returns up to 5 unique resources matching the topic,
    ranked by topic, level, and goal.
    """

    normalized_topic = normalize_topic(topic)

    all_resources = get_all_resources()

    scored_resources = []

    for resource in all_resources:

        score = calculate_match_score(
            resource,
            normalized_topic,
            level,
            goal
        )

        # Only include resources with a topic match
        if resource["topic"].lower() == normalized_topic.lower():

            resource_with_score = resource.copy()

            resource_with_score["match_score"] = score
            resource_with_score["explanation"] = generate_explanation(score)

            scored_resources.append(resource_with_score)

    # Sort highest score first
    scored_resources.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    # Remove duplicate titles
    unique_resources = []
    seen_titles = set()

    for resource in scored_resources:

        title = resource["title"]

        if title not in seen_titles:
            seen_titles.add(title)
            unique_resources.append(resource)

    # Return maximum 5 unique resources
    return unique_resources[:5]
