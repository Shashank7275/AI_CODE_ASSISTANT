# 🤖 AI Code Assistant

**An AI-powered debugging and code analysis assistant built with Python.**

## 📌 Overview

AI Code Assistant is an intelligent application that helps developers debug code, analyze errors, generate corrected code, and understand program output. Users can paste code or error messages, upload project files, and receive AI-generated debugging suggestions and explanations to improve their coding productivity.

## ✨ Features

- **Error Analysis:** Identifies and analyzes errors in user-provided code.
- **AI-Powered Debugging:** Generates corrected code and suggests possible solutions.
- **Code Explanation:** Explains errors, debugging changes, and expected program output.
- **Code Execution:** Supports code execution and testing through dedicated modules.
- **Code Editor:** Provides an interface for entering and working with code.
- **File Structure Support:** Helps users work with uploaded code files and project structures.
- **Test Runner:** Supports running tests to validate code behavior.
- **Web Deployment:** Includes configuration for deployment using Render.

## 🛠️ Technologies Used

- Python
- Agentic AI
- Large Language Models (LLMs)
- AI-powered code analysis
- Streamlit (if used for the application interface)
- Render (deployment)

## 📂 Project Structure

```text
AI_CODE_ASSISTANT/
│
├── agent.py            # AI agent logic
├── app.py              # Main application
├── code_editor.py      # Code editing functionality
├── debugg.py           # Debugging functionality
├── error_analyzer.py   # Error analysis
├── executor.py         # Code execution
├── Test_runner.py      # Test execution and validation
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python runtime configuration
├── render.yaml         # Render deployment configuration
└── .gitignore          # Git ignored files
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/Shashank7275/AI_CODE_ASSISTANT.git
cd AI_CODE_ASSISTANT
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
streamlit run app.py
```

*Note: The launch command and dependencies should match your actual application configuration.*

## 🚀 How It Works


1. Enter code or paste an error message.
2. Submit the code for AI-powered error analysis.
3. Review the suggested debugging solution and corrected code.
4. Read the explanation of the changes and expected output.
5. Test the updated code using the available execution and testing features.

## 🎯 Use Cases

- Debugging Python programs.
- Understanding programming errors.
- Generating corrected code suggestions.
- Learning from code explanations.
- Testing and improving code quality.

## 🔮 Future Enhancements

- Support for additional programming languages.
- Retrieval-Augmented Generation (RAG) for context-aware code assistance.
- Multi-file project analysis.
- Automated code quality checks.
- Downloadable debugging reports.

## 👨‍💻 Author

**Shashank Singh**

GitHub: [@Shashank7275](https://github.com/Shashank7275)

## 📄 License

Add an appropriate open-source license to the repository if you intend to distribute the project under one.
