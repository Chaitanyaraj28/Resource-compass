
import sqlite3

# Database file path
DB_PATH = "resource_compass.db"


def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database and create the resources table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            author TEXT NOT NULL,
            topic TEXT NOT NULL,
            level TEXT NOT NULL,
            goal TEXT NOT NULL,
            description TEXT NOT NULL,
            resource_type TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")


def seed_resources():
    """Populate the database with book resources."""

    conn = get_connection()
    cursor = conn.cursor()

    books = [

        # ==================== PYTHON ====================

        (
            "Python Crash Course",
            "Eric Matthes",
            "Python",
            "Beginner",
            "Understand Concepts",
            "A beginner-friendly book for learning Python programming from scratch.",
            "Book"
        ),

        (
            "Automate the Boring Stuff with Python",
            "Al Sweigart",
            "Python",
            "Beginner",
            "Practice",
            "Practical Python learning through automation projects and real-world examples.",
            "Book"
        ),

        (
            "Fluent Python",
            "Luciano Ramalho",
            "Python",
            "Advanced",
            "Understand Concepts",
            "Deep dive into Python's advanced features and idiomatic patterns.",
            "Book"
        ),

        (
            "Head First Python",
            "Paul Barry",
            "Python",
            "Beginner",
            "Understand Concepts",
            "Visual and engaging introduction to Python programming.",
            "Book"
        ),

        (
            "Think Python",
            "Allen B. Downey",
            "Python",
            "Intermediate",
            "Revision",
            "Introduction to Python with focus on problem-solving and computational thinking.",
            "Book"
        ),

        # ==================== DATA STRUCTURES ====================

        (
            "Grokking Algorithms",
            "Aditya Bhargava",
            "Data Structures",
            "Beginner",
            "Understand Concepts",
            "Visual guide to algorithms and data structures for beginners.",
            "Book"
        ),

        (
            "Introduction to Algorithms",
            "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
            "Data Structures",
            "Advanced",
            "Understand Concepts",
            "Comprehensive coverage of algorithms and data structures.",
            "Book"
        ),

        (
            "Data Structures and Algorithms Made Easy",
            "Narasimha Karumanchi",
            "Data Structures",
            "Intermediate",
            "Practice",
            "Problem-solving approach to DSA with coding examples.",
            "Book"
        ),

        # ==================== SOFTWARE ENGINEERING ====================

        (
            "Clean Code",
            "Robert C. Martin",
            "Software Engineering",
            "Intermediate",
            "Understand Concepts",
            "Best practices for writing clean, maintainable code.",
            "Book"
        ),

        (
            "The Pragmatic Programmer",
            "Andrew Hunt and David Thomas",
            "Software Engineering",
            "Intermediate",
            "Revision",
            "Timeless lessons for software craftsmanship and professional development.",
            "Book"
        ),

        # ==================== DATABASE ====================

        (
            "Database System Concepts",
            "Abraham Silberschatz, Henry F. Korth, S. Sudarshan",
            "DBMS",
            "Beginner",
            "Understand Concepts",
            "Foundational textbook covering database management systems.",
            "Book"
        ),

        (
            "Learning SQL",
            "Alan Beaulieu",
            "DBMS",
            "Beginner",
            "Practice",
            "Hands-on guide to learning SQL with practical examples.",
            "Book"
        ),

        # ==================== COMPUTER NETWORKS ====================

        (
            "Computer Networking: A Top-Down Approach",
            "James Kurose and Keith Ross",
            "Computer Networks",
            "Intermediate",
            "Understand Concepts",
            "Top-down approach to understanding computer networking.",
            "Book"
        ),

        # ==================== OPERATING SYSTEMS ====================

        (
            "Operating System Concepts",
            "Abraham Silberschatz, Peter B. Galvin, Greg Gagne",
            "Operating Systems",
            "Advanced",
            "Understand Concepts",
            "Comprehensive guide to operating system principles and design.",
            "Book"
        ),

        # ==================== ARTIFICIAL INTELLIGENCE ====================

        (
            "Artificial Intelligence: A Modern Approach",
            "Stuart Russell and Peter Norvig",
            "Artificial Intelligence",
            "Advanced",
            "Revision",
            "The leading textbook in artificial intelligence covering theory and practice.",
            "Book"
        ),

        # ==================== CLOUD COMPUTING ====================

        (
            "AWS Certified Solutions Architect Official Study Guide",
            "Joe Baron et al.",
            "Cloud Computing",
            "Intermediate",
            "Revision",
            "Comprehensive guide for AWS architecture concepts and certification preparation.",
            "Book"
        ),

        # ==================== WEB DEVELOPMENT ====================

        (
            "You Don't Know JS Yet",
            "Kyle Simpson",
            "Web Development",
            "Intermediate",
            "Understand Concepts",
            "Deep dive into the core mechanisms and intricacies of JavaScript.",
            "Book"
        ),

        (
            "Eloquent JavaScript",
            "Marijn Haverbeke",
            "Web Development",
            "Beginner",
            "Practice",
            "A modern introduction to programming, JavaScript, and the web.",
            "Book"
        ),

        # ==================== SYSTEM DESIGN ====================

        (
            "Designing Data-Intensive Applications",
            "Martin Kleppmann",
            "System Design",
            "Advanced",
            "Understand Concepts",
            "Comprehensive analysis of data architecture, storage engines, and distributed systems.",
            "Book"
        ),

        # ==================== JAVA ====================

        (
            "Head First Java",
            "Kathy Sierra and Bert Bates",
            "Java",
            "Beginner",
            "Understand Concepts",
            "A visual and beginner-friendly introduction to Java programming and object-oriented concepts.",
            "Book"
        ),

        (
            "Effective Java",
            "Joshua Bloch",
            "Java",
            "Advanced",
            "Revision",
            "Best practices and proven techniques for writing robust and maintainable Java code.",
            "Book"
        ),

        (
            "Java: The Complete Reference",
            "Herbert Schildt",
            "Java",
            "Intermediate",
            "Understand Concepts",
            "Comprehensive reference covering Java programming, object-oriented programming, and core APIs.",
            "Book"
        ),

        # ==================== C++ ====================

        (
            "C++ Primer",
            "Stanley B. Lippman, Josée Lajoie, Barbara E. Moo",
            "C++",
            "Beginner",
            "Understand Concepts",
            "Comprehensive introduction to modern C++ programming and object-oriented concepts.",
            "Book"
        ),

        (
            "Effective Modern C++",
            "Scott Meyers",
            "C++",
            "Advanced",
            "Revision",
            "Practical techniques and best practices for writing modern C++ code.",
            "Book"
        ),

        (
            "Programming: Principles and Practice Using C++",
            "Bjarne Stroustrup",
            "C++",
            "Beginner",
            "Understand Concepts",
            "A structured introduction to programming using C++ by its creator.",
            "Book"
        ),

        # ==================== C ====================

        (
            "The C Programming Language",
            "Brian W. Kernighan and Dennis M. Ritchie",
            "C",
            "Intermediate",
            "Understand Concepts",
            "Classic guide to the C programming language written by its creators.",
            "Book"
        ),

        (
            "C Programming: A Modern Approach",
            "K. N. King",
            "C",
            "Beginner",
            "Practice",
            "Comprehensive and practical introduction to C programming with numerous exercises.",
            "Book"
        ),

        # ==================== JAVASCRIPT ====================

        (
            "JavaScript: The Good Parts",
            "Douglas Crockford",
            "JavaScript",
            "Intermediate",
            "Revision",
            "Focused guide to the most useful and powerful features of JavaScript.",
            "Book"
        ),

        # ==================== C# ====================

        (
            "C# 12 in a Nutshell",
            "Joseph Albahari and Eric Johannsen",
            "C#",
            "Intermediate",
            "Understand Concepts",
            "Comprehensive reference covering modern C# programming and .NET development.",
            "Book"
        ),

        (
            "Head First C#",
            "Andrew Stellman and Jennifer Greene",
            "C#",
            "Beginner",
            "Practice",
            "Visual and engaging introduction to C# programming and object-oriented development.",
            "Book"
        ),

        # ==================== GO ====================

        (
            "The Go Programming Language",
            "Alan A. A. Donovan and Brian W. Kernighan",
            "Go",
            "Intermediate",
            "Understand Concepts",
            "Comprehensive introduction to Go programming and its core language features.",
            "Book"
        ),

        (
            "Learning Go",
            "Jon Bodner",
            "Go",
            "Intermediate",
            "Practice",
            "Practical guide to building efficient and idiomatic applications in Go.",
            "Book"
        ),

        # ==================== RUST ====================

        (
            "The Rust Programming Language",
            "Steve Klabnik and Carol Nichols",
            "Rust",
            "Beginner",
            "Understand Concepts",
            "Official-style introduction to Rust programming, ownership, borrowing, and memory safety.",
            "Book"
        ),

        (
            "Programming Rust",
            "Jim Blandy, Jason Orendorff, and Leonora F. S. Tindall",
            "Rust",
            "Advanced",
            "Understand Concepts",
            "In-depth guide to systems programming with Rust and its advanced features.",
            "Book"
        ),

        # ==================== KOTLIN ====================

        (
            "Kotlin in Action",
            "Dmitry Jemerov and Svetlana Isakova",
            "Kotlin",
            "Intermediate",
            "Understand Concepts",
            "Practical introduction to Kotlin programming and modern object-oriented development.",
            "Book"
        ),

        (
            "Head First Kotlin",
            "Dawn Griffiths and David Griffiths",
            "Kotlin",
            "Beginner",
            "Practice",
            "Visual and engaging introduction to Kotlin programming with hands-on examples.",
            "Book"
        ),

        # ==================== PHP ====================

        (
            "PHP & MySQL: Server-side Web Development",
            "Jon Duckett",
            "PHP",
            "Beginner",
            "Practice",
            "Practical introduction to PHP and MySQL for server-side web development.",
            "Book"
        ),

        # ==================== SWIFT ====================

        (
            "Swift Programming: The Big Nerd Ranch Guide",
            "Matthew Mathias and John Gallagher",
            "Swift",
            "Beginner",
            "Practice",
            "Hands-on introduction to Swift programming with practical exercises and examples.",
            "Book"
        )
    ]

    # Insert only books that are not already present
    inserted_count = 0

    for book in books:
        cursor.execute("""
            INSERT OR IGNORE INTO resources
            (title, author, topic, level, goal, description, resource_type)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, book)

        if cursor.rowcount > 0:
            inserted_count += 1

    conn.commit()
    conn.close()

    if inserted_count > 0:
        print(f"Successfully added {inserted_count} new resources to the database.")
    else:
        print("Database is already up to date. No new resources added.")


def get_all_resources():
    """Retrieve all resources from the database."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM resources")
    resources = cursor.fetchall()

    conn.close()

    # Convert Row objects to dictionaries
    return [dict(resource) for resource in resources]


# Initialize database when this module is run directly
if __name__ == "__main__":
    init_db()
    seed_resources()
