# Meeting Notes → Action Items Generator

## 📌 Overview

This project is an AI-powered tool that converts raw meeting notes into structured and actionable tasks.

It automatically identifies:

* What needs to be done
* Who is responsible (if mentioned)
* Deadlines (if mentioned)

The goal is to improve efficiency, consistency, and clarity in post-meeting follow-ups.

---

## 👤 Target Users

* Project Managers
* Team Leads
* Consultants
* Anyone who regularly runs or attends meetings

---

## ⚙️ How It Works

1. The user inputs raw meeting notes (unstructured text)
2. The AI model processes the text
3. The system extracts and formats action items
4. Results are saved into a structured output file (`output.txt`)

---

## 📥 Input

* Raw meeting notes (plain text)

---

## 📤 Output

* A numbered list of action items, including:

  * Task description
  * Owner (if available)
  * Deadline (if available)

---

## 🤖 Model & Technology

This project runs **locally using Ollama**, which means:

* No API cost
* No external data sharing
* Fully offline capability

Models used:

* `llama3` (default)
* `mistral` (optional alternative)

---

## 🚀 How to Run

### 1. Install Ollama

Download and install from: https://ollama.com

### 2. Pull a model

```bash
ollama pull llama3
```

### 3. Install dependencies

```bash
pip install requests
```

### 4. Run the app

```bash
python app.py
```

---

## 📄 Example Use Case

Input:

```
Tom needs to fix the login bug by Friday.
Lisa will design the homepage mockups by April 15.
```

Output:

```
1. Fix login bug — Owner: Tom — Deadline: Friday
2. Design homepage mockups — Owner: Lisa — Deadline: April 15
```

---

## Video Walkthrough
[Watch the video walkthrough here](你的YouTube或Vimeo链接)

---

## 💡 Why This Matters

Manually writing action items after meetings is:

* Time-consuming
* Error-prone
* Inconsistent

This tool ensures:

* No key tasks are missed
* Clear accountability
* Faster follow-ups

---

## 🧠 Reflection (for assignment)

* One thing I noticed: AI performs well on structured notes but struggles with ambiguous ownership
* One thing I liked: The automation significantly reduces manual effort
* One challenge: Handling messy or multilingual meeting notes

---

## 🔗 Repository

(Add your GitHub repo link here)
