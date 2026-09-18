from error_analyzer import error_analyzer
from code_editor import code_editor
from Test_runner import test_runner
from executor import execute_code
from debugg import debug_code


def main():

    print("=" * 60)
    print("🤖 AI AGENTIC CODE ASSISTANT")
    print("=" * 60)

    print("\nAgents loaded:")
    print("✅ Error Analyzer")
    print("✅ Code Editor")
    print("✅ Executor")
    print("✅ Test Runner")
    print("✅ Debug Engine")

    print("\nPaste your Python code.")
    print("Type END when finished.\n")

    lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        lines.append(line)

    user_code = "\n".join(lines)

    if not user_code.strip():
        print("❌ No code provided.")
        return

    print("\n🚀 Starting Agentic Debugging...")

    result = debug_code(user_code)

    print("\n" + "=" * 60)
    print("🎯 FINAL RESULT")
    print("=" * 60)

    print(f"\nStatus: {result['status']}")
    print(f"Attempts: {result['attempts']}")

    print("\n📋 ANALYSIS:")
    print(result["analysis"])

    print("\n💻 FINAL CODE:")
    print(result["code"])

    print("\n📤 :")
    print(result["output"])


if __name__ == "__main__":
    main()