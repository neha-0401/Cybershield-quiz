from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TOPICS = {
    "linux": {
        "title": "Part 1: Linux Commands",
        "questions": [
            {
                "q": "Which command lists hidden files with details?",
                "options": ["ls -la", "touch", "pwd", "whoami"],
                "answer": 0,
                "explanation": "ls -la lists all files, including hidden files, with details."
            },
            {
                "q": "Which command creates an empty file?",
                "options": ["mkdir", "touch", "rm", "cd"],
                "answer": 1,
                "explanation": "touch can create an empty file."
            },
            {
                "q": "Which command can recursively delete files?",
                "options": ["ls -la", "ip a", "rm -rf", "touch"],
                "answer": 2,
                "explanation": "rm -rf can delete directories and their contents. Use extreme caution."
            },
            {
                "q": "Which command traditionally displays network interface information?",
                "options": ["mkdir", "ifconfig", "touch", "rm"],
                "answer": 1,
                "explanation": "ifconfig displays or configures network interfaces."
            },
            {
                "q": "Which command displays network interfaces and IP addresses?",
                "options": ["ip a", "whoami", "touch", "ls"],
                "answer": 0,
                "explanation": "ip a displays network interfaces and their IP addresses."
            }
        ]
    },

    "basics": {
        "title": "Part 2: Basics of Cybersecurity",
        "questions": [
            {
                "q": "What is malicious software called?",
                "options": ["Malware", "Hardware", "Freeware", "Firmware"],
                "answer": 0,
                "explanation": "Malware is software designed to cause harm or perform unwanted actions."
            },
            {
                "q": "What filters network traffic to help block unauthorized access?",
                "options": ["Browser", "Firewall", "Keyboard", "Compiler"],
                "answer": 1,
                "explanation": "A firewall filters network traffic according to security rules."
            },
            {
                "q": "What is a fake message used to steal passwords called?",
                "options": ["Backup", "Phishing", "Patching", "Routing"],
                "answer": 1,
                "explanation": "Phishing tricks people into revealing sensitive information."
            },
            {
                "q": "What does MFA add to account login?",
                "options": ["More storage", "Extra verification", "Faster internet", "File compression"],
                "answer": 1,
                "explanation": "Multi-factor authentication requires additional verification."
            },
            {
                "q": "What helps fix known software vulnerabilities?",
                "options": ["Updates", "Screenshots", "Downloads", "Bookmarks"],
                "answer": 0,
                "explanation": "Security updates can fix known vulnerabilities."
            }
        ]
    },

    "attacks": {
        "title": "Part 3: Identify the Cyberattack",
        "questions": [
            {
                "q": "A fake bank email asks you to enter your password. What is it?",
                "options": ["Phishing", "Backup", "Encryption", "Patching"],
                "answer": 0,
                "explanation": "Phishing uses deceptive messages to steal information."
            },
            {
                "q": "Your files are encrypted and a payment is demanded. What is it?",
                "options": ["Spyware", "Ransomware", "Firewall", "Adware"],
                "answer": 1,
                "explanation": "Ransomware locks or encrypts data and demands a ransom."
            },
            {
                "q": "Many compromised devices flood a website with traffic. What is it?",
                "options": ["DDoS", "Phishing", "Spoofing", "Hashing"],
                "answer": 0,
                "explanation": "A distributed denial-of-service attack overwhelms a service with traffic."
            },
            {
                "q": "Malicious input changes a database query. What is it?",
                "options": ["Brute force", "SQL injection", "Ransomware", "Sniffing"],
                "answer": 1,
                "explanation": "SQL injection manipulates database queries through unsafe input."
            },
            {
                "q": "An attacker tricks an employee into revealing a secret. What is it?",
                "options": ["Social engineering", "Encryption", "Patching", "Authentication"],
                "answer": 0,
                "explanation": "Social engineering manipulates people into disclosing information or taking unsafe actions."
            }
        ]
    },

    "fundamentals": {
        "title": "Part 4: Security Fundamentals",
        "questions": [
            {
                "q": "Which principle protects information from unauthorized access?",
                "options": ["Availability", "Confidentiality", "Convenience", "Compression"],
                "answer": 1,
                "explanation": "Confidentiality ensures information is accessible only to authorized parties."
            },
            {
                "q": "Which principle protects data from unauthorized changes?",
                "options": ["Integrity", "Availability", "Anonymity", "Routing"],
                "answer": 0,
                "explanation": "Integrity means data remains accurate and protected from improper changes."
            },
            {
                "q": "Which principle ensures systems and data are accessible when needed?",
                "options": ["Confidentiality", "Integrity", "Availability", "Obfuscation"],
                "answer": 2,
                "explanation": "Availability means authorized users can access systems and data when needed."
            },
            {
                "q": "What verifies a user's identity?",
                "options": ["Authorization", "Authentication", "Encryption", "Auditing"],
                "answer": 1,
                "explanation": "Authentication verifies who a user is."
            },
            {
                "q": "What determines what an authenticated user is allowed to do?",
                "options": ["Authorization", "Phishing", "Hashing", "Scanning"],
                "answer": 0,
                "explanation": "Authorization determines a user's permissions."
            }
        ]
    },

    "crypto": {
        "title": "Part 5: Cryptography",
        "questions": [
            {
                "q": "What converts readable data into ciphertext?",
                "options": ["Decryption", "Encryption", "Authentication", "Deletion"],
                "answer": 1,
                "explanation": "Encryption transforms readable data into an encoded form."
            },
            {
                "q": "What converts ciphertext back into readable data?",
                "options": ["Hashing", "Scanning", "Decryption", "Compression"],
                "answer": 2,
                "explanation": "Decryption converts encrypted data back into readable form."
            },
            {
                "q": "What is the study of secure communication called?",
                "options": ["Cryptography", "Geography", "Typography", "Photography"],
                "answer": 0,
                "explanation": "Cryptography uses techniques to protect information and communication."
            },
            {
                "q": "Which encryption type uses the same shared key to encrypt and decrypt?",
                "options": ["Asymmetric", "Symmetric", "Public", "One-way"],
                "answer": 1,
                "explanation": "Symmetric encryption uses the same secret key for encryption and decryption."
            },
            {
                "q": "Which cryptographic system uses public and private keys?",
                "options": ["Symmetric", "Asymmetric", "Plaintext", "Checksum"],
                "answer": 1,
                "explanation": "Asymmetric cryptography uses a related public key and private key."
            }
        ]
    }
}


@app.route("/")
def home():
    return render_template("index.html", topics=TOPICS)


@app.route("/quiz/<topic_key>")
def quiz(topic_key):
    topic = TOPICS.get(topic_key)

    if topic is None:
        return redirect(url_for("home"))

    return render_template(
        "quiz.html",
        topic_key=topic_key,
        topic=topic
    )


@app.route("/result/<topic_key>", methods=["POST"])
def result(topic_key):
    topic = TOPICS.get(topic_key)

    if topic is None:
        return redirect(url_for("home"))

    score = 0
    results = []

    for i, question in enumerate(topic["questions"]):
        selected = request.form.get(f"q{i}")
        correct = selected is not None and selected.isdigit() \
            and int(selected) == question["answer"]

        if correct:
            score += 1

        selected_text = "Not answered"
        if selected is not None and selected.isdigit():
            choice_index = int(selected)
            if 0 <= choice_index < len(question["options"]):
                selected_text = question["options"][choice_index]

        results.append({
            "question": question["q"],
            "selected": selected_text,
            "correct_answer": question["options"][question["answer"]],
            "correct": correct,
            "explanation": question["explanation"]
        })

    percentage = round((score / len(topic["questions"])) * 100)

    return render_template(
        "result.html",
        topic=topic,
        score=score,
        total=len(topic["questions"]),
        percentage=percentage,
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)
