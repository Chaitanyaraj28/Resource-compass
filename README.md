📚 Resource Compass

## 🚀 Live Demo

👉 [Open Resource Compass]([https://resource-compass.streamlit.app](https://chaitanyaraj28-resource-compass-app-kd8l3v.streamlit.app/))

Resource Compass is a simple, student-focused library resource
recommendation system.

It helps students find a small list of useful learning resources based
on:

Topic

Knowledge Level

Learning Goal

Instead of showing a large list of resources, the system aims to provide
a short and understandable set of recommendations.

🎯 Project Goal

Students often have access to many books and learning resources but are
unsure which one is suitable for their current level and purpose.

Resource Compass addresses this problem by taking a student's input and
using rule-based recommendation logic to suggest relevant resources.

🛠️ Tech Stack

Python --- recommendation and application logic

Streamlit --- user interface

SQLite / Database layer --- resource storage

Git & GitHub --- version control and team collaboration

📁 Project Structure

resource-compass/
│
├── app.py
├── recommender.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore

app.py

Contains the Streamlit user interface.

It collects: - Topic - Knowledge level - Learning goal

and displays the recommended resources.

recommender.py

Contains the rule-based recommendation logic.

The main function is:

recommend_resources(topic, level, goal)

It takes the student's preferences and returns matching resources.

database.py

Contains the database-related functionality for storing and retrieving
resource data.

requirements.txt

Contains the Python packages required to run the project.

🚀 How to Run Locally

1. Clone the repository

git clone <your-github-repository-url>

2. Open the project folder

cd resource-compass

3. Create a virtual environment

Windows:

python -m venv env

4. Activate the virtual environment

.\env\Scriptsctivate

5. Install dependencies

pip install -r requirements.txt

6. Run the Streamlit application

streamlit run app.py

The application will open in your browser.

🧪 Testing the Recommendation Logic

The recommendation function can also be tested directly from the
terminal.

Example:

python -c "import recommender; print(recommender.recommend_resources('Data Structures', 'Beginner', 'Understand Concepts'))"

Another example:

python -c "import recommender; print(recommender.recommend_resources('Python', 'Beginner', 'Practice'))"

🔄 How the System Works

Student
   ↓
Enter Topic + Level + Goal
   ↓
Streamlit Interface
   ↓
Recommendation Logic
   ↓
Resource Matching
   ↓
Recommended Resources
   ↓
Display Results

The current recommendation logic uses transparent rules to match a
resource with the student's selected topic, level, and goal.

👥 Team Workflow

The project is developed collaboratively using GitHub.

Recommended workflow:

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

Before pushing changes, test the application locally.

⚠️ Current Limitations

The current prototype uses a small curated set of resources for testing.

The recommendation system currently uses exact matching for:

Topic

Knowledge level

Learning goal

Therefore, an input combination that does not exactly match an available
resource may return no recommendations.

Future versions can improve this by introducing:

Match scoring

Partial topic matching

Top 3--5 recommendations

Recommendation explanations

Larger resource catalogue

Better database integration

🔮 Future Improvements

Possible future improvements include:

Expand the library resource catalogue.

Store resources in a structured database.

Add recommendation scores.

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
