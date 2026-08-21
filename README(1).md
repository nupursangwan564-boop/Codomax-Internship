MODULE 5
# Coding Practice Tracker

A simple **Python-based Coding Practice Tracker** that helps users
record coding problems and analyze their practice progress by topic and
difficulty.

## 📌 Project Overview

The Coding Practice Tracker is designed for students who want to keep
track of their coding practice in an organized way.

The program allows the user to:

-   Add coding problems
-   Store problem details in a text file
-   Track whether a problem is solved or not solved
-   Categorize problems by topic
-   Record difficulty levels
-   View coding practice statistics
-   Identify strong and weak topics based on practice performance

The project uses **file handling in Python**, so the data is stored
permanently in a text file instead of being lost when the program
closes.

## 🚀 Features

### 1. Add Problem

The user can enter:

-   Problem name
-   Topic
-   Difficulty
-   Status

Example:

``` text
Problem Name: Two Sum
Topic: Array
Difficulty: Easy
Status: Solved
```

### 2. Store Data

All entered problems are stored in:

``` text
coding_data.txt
```

This allows the tracker to maintain data between different program runs.

### 3. Topic-wise Analysis

The tracker analyzes practice based on topics such as:

-   Array
-   Stack
-   Queue
-   Linked List
-   Tree
-   Graph
-   Sorting
-   Searching
-   Dynamic Programming

More topics can be added easily.

### 4. Difficulty Tracking

Problems can be classified as:

-   Easy
-   Medium
-   Hard

This helps the user understand the level of problems they are
practicing.

### 5. Solved / Not Solved Tracking

Each problem has a status:

-   Solved
-   Not Solved

This makes it easier to identify unfinished practice.

### 6. Strong and Weak Topics

The program calculates topic-wise performance and helps identify:

-   **Strong Topics** -- topics where the user has better
    practice/performance
-   **Weak Topics** -- topics where the user needs more practice

This can help the user decide which DSA topics should receive more
attention.

## 🛠️ Technologies Used

-   **Python**
-   **File Handling**
-   **Lists**
-   **Dictionaries**
-   **Loops**
-   **Functions**
-   **Conditional Statements**
-   **String Processing**

## 📂 Project Structure

``` text
Coding-Practice-Tracker/
│
├── coding_tracker.py
├── coding_data.txt
└── README.md
```

> `coding_tracker.py` contains the main Python program, while
> `coding_data.txt` stores the coding-practice records.

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your system.

Check the installation using:

``` bash
python --version
```

### Step 2: Clone or Download the Project

Download the project to your computer.

### Step 3: Run the Program

Open the project folder in a terminal and run:

``` bash
python coding_tracker.py
```

### Step 4: Enter Your Data

Follow the options displayed by the program and enter your
coding-practice information.

## 📊 Example Data

A record can contain information like:

``` text
Two Sum | Array | Easy | Solved
Valid Parentheses | Stack | Easy | Solved
Queue Implementation | Queue | Medium | Not Solved
```

## 🎯 Purpose of the Project

The main purpose of this project is to make coding practice more
organized and measurable.

Instead of solving problems randomly, the user can track:

-   What problems they solved
-   Which topics they practice most
-   Which difficulty levels they attempt
-   Which topics need improvement

## 🔮 Future Improvements

The project can be extended with:

-   Graphical User Interface (GUI)
-   SQLite/MySQL database
-   Search and filter functionality
-   Progress charts
-   Daily/weekly practice goals
-   Streak tracking
-   Difficulty-wise statistics
-   Topic-wise percentage analysis
-   Exporting reports to CSV
-   Login/user profiles

## 👩‍💻 Author

**Nupur**

B.Tech -- Artificial Intelligence & Data Science

Interested in **Python, DSA, Artificial Intelligence, Software
Development, and Problem Solving**.

## ⭐ Conclusion

The Coding Practice Tracker is a beginner-friendly Python project that
demonstrates practical use of **functions, file handling, data
structures, and basic data analysis**.

It can be further developed into a complete coding-progress management
system.
