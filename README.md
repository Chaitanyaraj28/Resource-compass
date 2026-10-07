📚 Resource Compass

🚀 Live Demo

👉 [Open Resource Compass](https://chaitanyaraj28-resource-compass-app-kd8l3v.streamlit.app/)

Resource Compass is a student-focused library resource recommendation system
that helps students find suitable learning resources based on their:

- Topic
- Knowledge Level
- Learning Goal

Instead of showing a large list of resources, the system aims to provide
a short and understandable set of recommendations.


🎯 Problem

Students often have access to many books and learning resources but may not
know which resource is most suitable for their current level and purpose.

Resource Compass reduces this choice overload by ranking relevant resources
using a transparent rule-based scoring system.


## ⚙️ How It Works

```text
Student Input
     ↓
Streamlit Interface
     ↓
Python Recommendation Engine
     ↓
SQLite Resource Database
     ↓
Weighted Match Scoring
     ↓
Top 3–5 Recommended Resources
     ↓
Results + Explanation
```

The recommendation logic uses transparent rules to match resources with the
student's selected topic, knowledge level, and learning goal.


🧠 Recommendation Logic

Each resource receives a score out of 100:

| Criterion | Weight |
|---|---|
| Topic Match | 50 |
| Knowledge Level Match | 25 |
| Learning Goal Match | 25 |
| **Total** | **100** |

The resources are ranked according to their match score.

The system also generates a simple explanation for every recommendation.


🛠️ Tech Stack

Python --- recommendation and application logic

Streamlit --- user interface

SQLite / Database layer --- resource storage

Git & GitHub --- version control and team collaboration


📁 Project Structure

```text
Resource-compass/
├── app.py
├── recommender.py
├── database.py
├── resource_compass.db
├── requirements.txt
├── README.md
└── .gitignore
```
app.py—

Contains the Streamlit user interface.

It collects: - Topic - Knowledge level - Learning goal

and displays the recommended resources.

recommender.py—

Contains the rule-based recommendation logic.

The main function is:

recommend_resources(topic, level, goal)

It takes the student's preferences and returns matching resources.

database.py—

Contains the database-related functionality for storing and retrieving
resource data.

requirements.txt—

Contains the Python packages required to run the project.


🔄 End-to-End System Flow
The complete application works as follows:

1.The student enters a topic.

2.The student selects their knowledge level.

3.The student selects their learning goal.

4.Streamlit passes these inputs to the recommendation engine.

5.The recommendation engine retrieves resources from the SQLite database.

6.Each resource is evaluated using the rule-based scoring logic.

7.Resources are ranked according to their scores.

8.The best matching resources are returned.

9.Streamlit displays the recommendations along with their scores and explanations.

No manual lookup is required between the user's input and the final result.


🚀 How to Run Locally

1. Clone the repository

git clone https://chaitanyaraj28-resource-compass

2. Open the project folder

cd resource-compass

3. Create a virtual environment

Windows:

python -m venv env

4. Activate the virtual environment

.\env\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Run the Streamlit application

streamlit run app.py

The application will open in your browser.


🧪Testing

The recommendation system can be tested using different combinations of topic, knowledge level, and learning goal.

Example Test Case 1

Topic: Python
Level: Beginner
Goal: Practice

Expected result:
* Relevant Python resources
* Ranked recommendations
* Match scores
* Recommendation explanations

Example Test Case 2

Topic: Data Structures
Level: Beginner
Goal: Understand Concepts

Expected result:
* Relevant Data Structures resources
* Ranked recommendations
* Match scores
* Recommendation explanations


👥 Team Workflow

The project is developed collaboratively using GitHub.

Recommended workflow:

```text
Make changes
     ↓
Test locally
     ↓
git add .
     ↓
git commit
     ↓
git push
     ↓
GitHub
```
Before pushing changes, test the application locally.


🔮 Future Improvements

Possible future improvements include:

Expand the library resource catalogue.

Store resources in a structured database.

Display why each resource was recommended.

Return the best 3--5 resources instead of only exact matches.

Improve topic and keyword matching.

Add more learning levels and goals.

Conduct usability testing with real students.


📌 Project Status

Prototype / Development Stage
The project is being developed as a student Design Thinking and Idea Lab
prototype.

📄 License

This project is intended for educational and academic use.




