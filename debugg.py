from error_analyzer import error_analyzer
from code_editor import code_editor
from Test_runner import test_runner
from executor import execute_code


def extract_clean_code(content: str) -> str:
    content = str(content).strip()
    if "```" in content:
        parts = content.split("```")
        if len(parts) >= 3:
            code_part = parts[1]
            if code_part.startswith("python"):
                code_part = code_part[6:]
            elif code_part.startswith("py"):
                code_part = code_part[2:]
            return code_part.strip()
        # Fallback if only opening fence or partial
        code_part = content.replace("```python", "").replace("```py", "").replace("```", "")
        return code_part.strip()
    return content


def debug_code(user_code: str, max_retries: int = 3):

    current_code = user_code

    # First analysis
    analysis = error_analyzer.run(
        f"""
Analyze this Python code:

{current_code}
"""
    )

    for attempt in range(1, max_retries + 1):

        print(f"\n🔄 Attempt {attempt}/{max_retries}")

        # Code Editor
        fixed_code = code_editor.run(
            f"""
USER CODE:
{current_code}

ERROR ANALYSIS:
{analysis.content}

Fix the code.

Return ONLY the complete corrected Python code.
"""
        )

        current_code = extract_clean_code(fixed_code.content)

        # Execute
        execution = execute_code(current_code)

        print("\nExecution Result:")
        print(execution["stdout"])

        if execution["stderr"]:
            print("\nError:")
            print(execution["stderr"])

        # Test Runner
        test = test_runner.run(
            f"""
CORRECTED CODE:
{current_code}

ACTUAL EXECUTION RESULT:
STDOUT:
{execution["stdout"]}

STDERR:
{execution["stderr"]}

RETURN CODE:
{execution["returncode"]}
"""
        )

        print("\nTest Runner:")
        print(test.content)

        # SUCCESS
        if execution["success"]:

            return {
                "status": "SUCCESS",
                "attempts": attempt,
                "code": current_code,
                "output": execution["stdout"],
                "analysis": analysis.content
            }

        # FAILED → Analyze new error
        analysis = error_analyzer.run(
            f"""
The corrected code still failed.

CODE:
{current_code}

ACTUAL ERROR:
{execution["stderr"]}

Analyze this new error.

Do not modify the code.
Provide precise instructions for the Code Editor.
"""
        )

    return {
        "status": "FAILED",
        "attempts": max_retries,
        "code": current_code,
        "output": execution["stderr"],
        "analysis": analysis.content
    }