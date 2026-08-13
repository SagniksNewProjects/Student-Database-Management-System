# Student-Database-Management-System
Student Database Management System Using Python and CSV File Handling.


A production-ready, menu-driven CLI application designed to track, store, and manage student academic profiles with built-in input verification layers and persistent storage.

## 🛠️ Core Computer Science Concepts Implemented
* **Object-Oriented Programming (OOP):** Modeled entities using a `Student` abstraction layer mapped to dictionary serialization functions.
* **Data Serialization & Persistence:** Integrated Python’s native `csv.DictWriter` and `csv.DictReader` to store complex relational records locally.
* **Defensive Programming & Input Validation:** Built dedicated logical check blocks to catch exceptions, format numeric floats (CGPA limits), verify string patterns (email structures), and restrict fixed-width numeric fields (10-digit phone numbers).
* **Search Optimization:** Engineered basic filtering algorithms supporting both exact ID lookups and dynamic partial-string name matching.

## 🚀 Key Features
* Prevent duplicate entry conflicts via local primary key checking (Roll Number uniqueness)
* Complete CRUD utility (Create, Read, Search, Update) records seamlessly
* Resilient data formats utilizing localized padding masks for clean, structural grid reports
* Safe exception catching to isolate wrong type definitions (e.g., handling non-numeric CGPA)

## 💻 Running the Project
1. Clone this repository or download the python script.
2. Run the application via terminal:
   ```bash
   python main.py
   ```
