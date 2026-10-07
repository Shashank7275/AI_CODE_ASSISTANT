# 🤖 AI Code Assistant

**An AI-powered debugging, code analysis, execution, testing, and error-fixing assistant built with Python and Agentic AI.**

<p align="center">
  <a href="https://ai-code-assistant-1-ge51.onrender.com">
    <img src="https://img.shields.io/badge/Live%20Demo-Open%20App-success?style=for-the-badge" alt="Live Demo">
  </a>
  <a href="https://github.com/Shashank7275/AI_CODE_ASSISTANT">
    <img src="https://img.shields.io/badge/GitHub-Source%20Code-black?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

## 🚀 Live Demo

🌐 **Try the deployed application:**  
https://ai-code-assistant-1-ge51.onrender.com

📦 **Source Code:**  
https://github.com/Shashank7275/AI_CODE_ASSISTANT

---

## 🖥️ Application Screenshot

### AI Agentic Code Assistant

<p align="center">
  <img width="900" height="506" alt="Screenshot (320)" src="https://github.com/user-attachments/assets/43559407-e831-41cf-90db-eb4d1d56841c" />

</p>

> The application provides an AI-powered workflow for analyzing code, debugging errors, executing code, testing results, and generating corrections.

---

## 📌 Overview

**AI Code Assistant** is an intelligent developer tool that helps users analyze and debug Python code using an agentic AI workflow.

The application can analyze code, identify errors, generate debugging suggestions, produce corrected code, execute and test code, and explain the results.

The goal is to reduce repetitive debugging work and provide developers with an AI assistant that can reason through programming problems step by step.

---

## ✨ Features

- 🔍 **Error Analysis** — Identifies and analyzes errors in user-provided code.
- 🤖 **AI-Powered Debugging** — Generates debugging suggestions and corrected code.
- 🧠 **Code Explanation** — Explains errors, fixes, changes, and expected output.
- ▶️ **Code Execution** — Executes code through the application's execution module.
- 🧪 **Test Runner** — Tests code and validates its behavior.
- 📝 **Code Editor** — Provides an interface for entering and editing code.
- 📂 **Project/File Support** — Supports working with code files and project structures.
- 🔄 **Agentic Debugging Pipeline** — Uses multiple stages to analyze, edit, execute, test, and debug code.
- ☁️ **Render Deployment** — Deployed as a web application using Render.

---

## 🧠 Agentic AI Workflow

```text
                 ┌─────────────────────┐
                 │    User Code        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Analyze Code      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Detect Errors     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Generate Fix       │
                 │  / Correct Code     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Execute Code      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Run Tests        │
                 └──────────┬──────────┘
                            │
                       Test Failed?
                       /          \
                     Yes           No
                      │             │
                      ▼             ▼
              ┌─────────────┐   ┌─────────────┐
              │ Debug Again │   │   Success   │
              └──────┬──────┘   └──────┬──────┘
                     │                 │
                     └───────┬─────────┘
                             ▼
                    ┌─────────────────┐
                    │ Explain Results │
                    └─────────────────┘
```

---

## 🔥 How It Works

The assistant follows an iterative debugging process:

```text
Analyze → Edit → Execute → Test → Debug → Repeat
```

The application can continue debugging until the code reaches a clean execution state or the configured maximum debugging attempts are reached.

### Example

Input:

```python
def add(a, b):
    return a + b

print(add(2, "3"))
```

The assistant can:

1. Analyze the code.
2. Detect the type-related error.
3. Explain why the error occurs.
4. Generate a possible correction.
5. Execute the corrected code.
6. Test the result.
7. Explain the final output.

---

## 🛠️ Technologies Used

- **Python**
- **Agentic AI**
- **Large Language Models (LLMs)**
- **AI-powered code analysis**
- **Streamlit**
- **Render**
- **Python code execution**
- **Automated testing**

---

## 📂 Project Structure

```text
AI_CODE_ASSISTANT/
│
├── agent.py             # AI agent logic
├── app.py               # Main application
├── code_editor.py       # Code editing functionality
├── debugg.py            # Debugging functionality
├── error_analyzer.py    # Error analysis
├── executor.py          # Code execution
├── Test_runner.py       # Test execution and validation
│
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python runtime configuration
├── render.yaml          # Render deployment configuration
└── .gitignore           # Git ignored files
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Shashank7275/AI_CODE_ASSISTANT.git
cd AI_CODE_ASSISTANT
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Open the local Streamlit URL displayed in your terminal.

---

## 🖥️ Using the Application

### Step 1 — Paste Python code

Enter your Python code into the code editor.

### Step 2 — Configure debugging

Choose the maximum number of debugging attempts and other available options.

### Step 3 — Run Agentic Debugging

Click:

```text
🚀 Run Agentic Debugging
```

### Step 4 — Review the results

The AI workflow analyzes the code and can provide:

- detected errors
- debugging reasoning
- corrected code
- execution results
- test results
- explanations

### Step 5 — Iterate

If the code still fails, the agentic workflow can continue debugging until the configured attempt limit is reached.

---

## 🎯 Use Cases

- 🐍 Python debugging
- 🧑‍💻 Learning programming
- 🔎 Understanding Python errors
- 🛠️ Generating corrected code
- 🧪 Testing programs
- 📚 Learning from AI-generated explanations
- ⚡ Improving developer productivity
- 🤖 Experimenting with Agentic AI for software development

---

## ☁️ Deployment on Render

The application is deployed on **Render**.

### Live application

https://ai-code-assistant-1-ge51.onrender.com

### Typical Render configuration

```text
Build Command:
pip install -r requirements.txt

Start Command:
streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
```

The repository contains:

```text
requirements.txt
runtime.txt
render.yaml
```

for deployment configuration.

---

## 🔐 Security Note

If the application uses API keys or other secrets, store them in environment variables or Render's secret/environment-variable settings.

**Never commit API keys, passwords, tokens, or `.env` secrets to GitHub.**

---

## 🔮 Future Enhancements

- 🌐 Support for additional programming languages
- 🧠 Retrieval-Augmented Generation (RAG)
- 📂 Advanced multi-file project analysis
- 🔍 Automated code-quality checks
- 🧪 More advanced test generation
- 📊 Downloadable debugging reports
- 🔗 GitHub repository integration
- 🐳 Docker deployment
- 🔐 User authentication
- 💾 Debugging history
- 🧩 IDE/editor integration
- 🚀 Automated pull-request debugging

---

## 👨‍💻 Author

**Shashank Singh**

GitHub:  
https://github.com/Shashank7275

Project Repository:  
https://github.com/Shashank7275/AI_CODE_ASSISTANT

Live Demo:  
https://ai-code-assistant-1-ge51.onrender.com

---

## ⭐ Support

If you find this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Report bugs
- 💡 Suggest features
- 📢 Share the project

---

## 📄 License

Add your preferred open-source or commercial license before distributing the project.

If you plan to sell the source code, define the license clearly and specify what buyers are allowed to use, modify, and redistribute.
