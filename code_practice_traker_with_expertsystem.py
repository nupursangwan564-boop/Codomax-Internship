# Coding Practice Tracker

FILE_NAME = "coding_data.txt"


# Add Problem
def add_problem():

    name = input("Enter problem name: ")

    topic = input("Enter topic: ").strip().title()

    difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip().title()

    status = input("Enter status (Solved/Not Solved): ").strip().title()

    file = open(FILE_NAME, "a")

    file.write(name + "|" + topic + "|" + difficulty + "|" + status + "\n")

    file.close()

    print("Problem added successfully! ✅")


# View Problems
def view_problems():

    try:
        file = open(FILE_NAME, "r")
    except FileNotFoundError:
        print("\nNo problems added yet!")
        return

    print("\n===== ALL PROBLEMS =====")

    number = 1

    for line in file:

        data = line.strip().split("|")

        if len(data) == 4:

            print("\nProblem", number)
            print("Name:", data[0])
            print("Topic:", data[1])
            print("Difficulty:", data[2])
            print("Status:", data[3])

            number = number + 1

    file.close()


# Topic Performance
def topic_performance():

    try:
        file = open(FILE_NAME, "r")
        data = file.readlines()
        file.close()

    except FileNotFoundError:
        print("\nNo problems added yet!")
        return

    if len(data) == 0:
        print("\nNo problems added yet!")
        return

    topics = []

    # Get unique topics
    for line in data:

        details = line.strip().split("|")

        if len(details) == 4:

            topic = details[1].strip().title()

            if topic not in topics:
                topics.append(topic)


    print("\n===== TOPIC PERFORMANCE =====")

    strongest_topic = ""
    weakest_topic = ""

    highest_percentage = -1
    lowest_percentage = 101


    # Check each topic
    for topic in topics:

        total = 0
        solved = 0

        for line in data:

            details = line.strip().split("|")

            if len(details) == 4:

                current_topic = details[1].strip().title()

                if current_topic == topic:

                    total = total + 1

                    status = details[3].strip().lower()

                    if status == "solved":
                        solved = solved + 1


        percentage = (solved / total) * 100


        print("\nTopic:", topic)
        print("Total Problems:", total)
        print("Solved:", solved)
        print("Performance:", round(percentage, 2), "%")


        # Performance Result
        if percentage >= 70:

            print("Result: 🟢 Strong")

        elif percentage >= 40:

            print("Result: 🟡 Good")

        else:

            print("Result: 🔴 Needs More Practice")


        # Find Strongest Topic
        if percentage > highest_percentage:

            highest_percentage = percentage
            strongest_topic = topic


        # Find Weakest Topic
        if percentage < lowest_percentage:

            lowest_percentage = percentage
            weakest_topic = topic


    # AI Recommendation
    print("\n===== 🤖 AI RECOMMENDATION =====")

    print("Strongest Topic:", strongest_topic)
    print("Highest Performance:", round(highest_percentage, 2), "%")

    print("\nWeakest Topic:", weakest_topic)
    print("Lowest Performance:", round(lowest_percentage, 2), "%")


    print("\nRecommendation:")

    if weakest_topic == strongest_topic:

        print("You have only one topic.")
        print("Add problems from other topics to compare your performance.")

    elif lowest_percentage < 40:

        print("Your", weakest_topic, "topic is weak.")
        print("Now focus on", weakest_topic, "and practice more problems.")

    elif lowest_percentage < 70:

        print("Your", weakest_topic, "needs improvement.")
        print("Practice more", weakest_topic, "problems.")

    else:

        print("Your performance is good in all topics.")
        print("Keep practicing regularly.")


# Main Menu

while True:

    print("\n==============================")
    print("   CODING PRACTICE TRACKER")
    print("==============================")

    print("1. Add Problem")
    print("2. View Problems")
    print("3. Topic Performance")
    print("4. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        add_problem()


    elif choice == "2":

        view_problems()


    elif choice == "3":

        topic_performance()


    elif choice == "4":

        print("Thank you for using Coding Practice Tracker! 🚀")
        break


    else:

        print("Invalid choice!")