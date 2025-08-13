import streamlit as st

# ✅ Predefined static subjects and their educational content
predefined_subjects = {
    "Cyber Security": {
        "Key Concepts": [
            "Network security fundamentals",
            "Encryption & cryptography",
            "Common attack types (e.g., phishing, malware)",
            "Firewall and intrusion detection systems"
        ],
        "Recommended Readings": [
            '"Cybersecurity for Beginners" by Raef Meeuwisse',
            "OWASP Top 10 documentation",
            "Cybersecurity modules from Coursera/edX"
        ],
        "Practice Tasks": [
            "Simulate phishing detection using Python",
            "Analyze a sample network log for intrusion",
            "Create a secure login system with encryption"
        ]
    },
    "Machine Learning": {
        "Key Concepts": [
            "Supervised vs unsupervised learning",
            "Model evaluation metrics (accuracy, precision, recall)",
            "Overfitting and regularization",
            "Gradient descent and optimization"
        ],
        "Recommended Readings": [
            '"Hands-On Machine Learning with Scikit-Learn" by Aurélien Géron',
            "Google Machine Learning Crash Course",
            "Elements of Statistical Learning (Stanford)"
        ],
        "Practice Tasks": [
            "Build a decision tree classifier",
            "Visualize data using PCA or t-SNE",
            "Implement k-means clustering from scratch"
        ]
    },
    "Artificial Intelligence": {
        "Key Concepts": [
            "Search algorithms (A*, BFS, DFS)",
            "Knowledge representation and reasoning",
            "Natural Language Processing basics",
            "Ethics in AI"
        ],
        "Recommended Readings": [
            '"Artificial Intelligence: A Modern Approach" by Russell & Norvig',
            "Stanford AI course materials",
            "MIT OpenCourseWare - Introduction to AI"
        ],
        "Practice Tasks": [
            "Implement a simple chatbot using rules",
            "Solve a maze using A* algorithm",
            "Create a basic rule-based expert system"
        ]
    },
    "Data Science": {
        "Key Concepts": [
            "Data wrangling and preprocessing",
            "Exploratory Data Analysis (EDA)",
            "Statistical inference",
            "Data visualization techniques"
        ],
        "Recommended Readings": [
            '"Python for Data Analysis" by Wes McKinney',
            "Kaggle tutorials and datasets",
            "Coursera Specialization by Johns Hopkins University"
        ],
        "Practice Tasks": [
            "Clean a messy dataset and extract insights",
            "Build a dashboard using Plotly or Streamlit",
            "Perform hypothesis testing on sample data"
        ]
    },
    "Robotics": {
        "Key Concepts": [
            "Forward and inverse kinematics",
            "Sensor integration and feedback",
            "Motion planning algorithms",
            "Robot Operating System (ROS)"
        ],
        "Recommended Readings": [
            '"Introduction to Robotics" by John J. Craig',
            "ROS tutorials and documentation",
            "Coursera Robotics Specialization"
        ],
        "Practice Tasks": [
            "Simulate a robotic arm in Webots or Gazebo",
            "Write a path planning algorithm (e.g., RRT)",
            "Integrate ultrasonic sensors for obstacle avoidance"
        ]
    },
    "Reinforcement Learning": {
        "Key Concepts": [
            "Markov Decision Processes (MDPs)",
            "Q-Learning and SARSA",
            "Policy Gradient methods",
            "Exploration vs exploitation trade-off"
        ],
        "Recommended Readings": [
            '"Reinforcement Learning: An Introduction" by Sutton & Barto',
            "Spinning Up by OpenAI",
            "Deep Reinforcement Learning Course by David Silver (DeepMind)"
        ],
        "Practice Tasks": [
            "Train an agent using Q-learning in a GridWorld",
            "Implement PPO using Stable-Baselines3",
            "Simulate reward shaping in a custom environment"
        ]
    }
}

# ✅ Streamlit UI
def run_feature():
    st.title("📚 Personalized Content Recommendation")

    subject = st.selectbox("Choose a subject", list(predefined_subjects.keys()))

    if subject:
        data = predefined_subjects[subject]
        st.subheader("✅ Key Concepts")
        for item in data["Key Concepts"]:
            st.markdown(f"- {item}")

        st.subheader("📖 Recommended Readings")
        for item in data["Recommended Readings"]:
            st.markdown(f"- {item}")

        st.subheader("🧪 Practice Tasks")
        for item in data["Practice Tasks"]:
            st.markdown(f"- {item}")

# ✅ Entry point
if __name__ == "__main__":
    run_feature()
