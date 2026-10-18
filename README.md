
# 🛡️ CyberShield Quiz Lab

A beginner-friendly cybersecurity quiz practice website built using Python, Flask, HTML, and CSS. It helps students learn Linux commands, cybersecurity basics, attack identification, security fundamentals, and cryptography through interactive multiple-choice quizzes.

## ✨ Features

- 5 cybersecurity learning modules
- 5 questions in each module (25 questions total)
- Four options for each question
- One-word answers or short command answers where possible
- Beginner-to-harder learning progression
- Automatic score calculation out of 5
- Percentage score and correct answer review
- Explanations for every question
- Print results using the browser's print feature
- Dark cybersecurity-themed user interface

## 📚 Quiz Modules

1. **Linux Commands** — `ls -la`, `touch`, `rm -rf`, `ifconfig`, `ip a`
2. **Basics of Cybersecurity** — Malware, firewall, phishing, MFA, and updates
3. **Identify the Cyberattack** — Phishing, ransomware, DDoS, SQL injection, and social engineering
4. **Security Fundamentals** — Confidentiality, integrity, availability, authentication, and authorization
5. **Cryptography** — Encryption, decryption, symmetric encryption, and asymmetric cryptography

## 🧰 Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Kali Linux or another Python-compatible operating system

## 📁 Project Structure

```text
cybershield-quiz/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   ├── quiz.html
│   └── result.html
└── static/
    └── style.css
```

## ⚙️ Installation and Setup

### Requirements

- Python 3
- pip
- Git
- A web browser

### Step 1: Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/cybershield-quiz.git
```

Replace `YOUR-USERNAME` with the GitHub username of the repository owner.

### Step 2: Enter the project directory

```bash
cd cybershield-quiz
```

### Step 3: Create a virtual environment

```bash
python3 -m venv venv
```

### Step 4: Activate the virtual environment

On Kali Linux or other Linux systems:

```bash
source venv/bin/activate
```

### Step 5: Install the dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Start the website

```bash
python app.py
```

### Step 7: Open the website

Open your browser and visit:

http://127.0.0.1:5000

The quiz website will run locally on your computer.

## 🧑‍💻 How to Use the Website

1. Open the CyberShield Quiz Lab homepage.
2. Select one of the five quiz modules.
3. Read each question carefully.
4. Select one answer from the four available options.
5. Answer all five questions in the selected module.
6. Click **Submit Quiz**.
7. View your score out of 5 and your percentage.
8. Review your selected answers, correct answers, and explanations.
9. Return to the homepage to practise another module.
10. Use **Print Results** if you want a printable copy of your results.

## 🧪 Testing

- Verify that all five modules appear on the homepage.
- Check that each module contains five questions.
- Select correct and incorrect answers to test scoring.
- Confirm that explanations appear on the results page.
- Test the homepage navigation and print feature.

## 🔐 Safety Notes

- This project is an educational quiz application.
- The `rm -rf` command is included for learning purposes. Do not run it on important files or system directories.
- The Flask debug server is intended for local development, not public production hosting.
- Do not upload passwords, secret keys, personal information, or other confidential files.

## 🚀 Future Improvements

- Student registration and login
- Save quiz history using SQLite
- Leaderboard and progress tracking
- More cybersecurity questions
- Difficulty filters and timed quizzes
- Online deployment

## 👨‍🎓 Project Purpose

CyberShield Quiz Lab is a beginner-level cybersecurity learning project created to help students practise security concepts interactively and strengthen their foundational knowledge.

## 📄 License

This project is available for educational use. Add a specific open-source license if you wish to grant permissions under a formal license.
