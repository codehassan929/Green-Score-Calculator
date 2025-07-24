   •Green Score Calculator: AI-Based Personal Environmental Impact App.

•Project Overview:
The Green Score Calculator is a lightweight AI-powered app that helps users calculate their environmental impact based on electricity usage, transport habits, and waste generation. It's a simple but powerful awareness tool for eco-friendly living.


 •Objective:
The goal is to promote sustainable behavior by providing a visual and numerical understanding of how daily habits affect the environment — through a personalized Green Score.


 •AI at the Core:
AI logic is built into the app to:
- Analyze and weigh user input.
- Calculate a personalized Green Score.
- Provide actionable suggestions for greener alternatives.

The algorithm uses conditional weighting for electricity,transport,and waste to determine environmental impact.

 •Problem Statement:
Many individuals lack awareness of how their everyday choices contribute to climate change. There are few tools available that allow them to measure and visualize their footprint. This project solves that by making the invisible visible.

 •How It Works:

1. The user inputs:
   - Electricity usage (kWh)
   - Transport distance (km/week)
   - Waste generated (kg/week)
2. The app calculates a Green Score (0–100).
3. It shows feedback messages based on the score.
4. It displays charts comparing the environmental metrics.


Example.

``text
Input:
- Electricity usage: 50 kWh/week
- Transport: 70 km/week
- Waste: 12 kg/week

Green Score: 68/100

Suggestions:
- Reduce transport by carpooling or biking.
- Recycle to reduce household waste.


Tech Stack:

Python

Streamlit (Frontend/UI)

Matplotlib & Seaborn (Charts)

Pandas & NumPy (Data handling)

GitHub (Version control)


 •Features:

Interactive form for data entry.

Real-time Green Score calculation.

Personalized environmental suggestions.

Dynamic bar and pie charts.

Clean and responsive UI.


 •Project Structure:

📦green-score-calculator
 ┣ 📂assets/             → Images or chart screenshots
 ┣ 📂data/               → Test data or user logs (optional)
 ┣ 📜app.py              → Main Streamlit interface
 ┣ 📜ai_engine.py        → Score calculation logic (AI-powered)
 ┣ 📜README.md           → Project documentation
 ┗ 📜requirements.txt    → List of Python dependencies


 •Getting Started:

1. Clone the repository:

git clone https://github.com/codehassan929/green-score-calculator.git
cd green-score-calculator


2. Install the dependencies:

pip install -r requirements.txt


3. Run the app using Streamlit:

streamlit run app.py


•Dependencies:

streamlit

matplotlib

seaborn

pandas

numpy


(You can find them all in requirements.txt)


👨‍💻 Author:

Developed by Hassan Ismail

Connect with Me:

📧 Email: hassanismailhja887@gmail.com

🔗 LinkedIn: linkedin.com/in/hassan-ismail

🐙 GitHub: github.com/codehassan929

