import streamlit as st
import time

from error_analyzer import error_analyzer
from code_editor import code_editor
from Test_runner import test_runner
from executor import execute_code
from debugg import debug_code

# --------------------------------------------------------------------------
# Page config
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Agentic Code Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------
# Minimal styling polish
# --------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .block-container { padding-top: 2rem; padding-bottom: 3rem; }
        .status-pill {
            display: inline-block;
            padding: 0.25rem 0.9rem;
            border-radius: 999px;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .status-success { background: #d1f7dc; color: #0a6b2d; }
        .status-fail { background: #fde2e2; color: #a11212; }
        .agent-card {
            padding: 0.6rem 0.9rem;
            border-radius: 10px;
            background: rgba(120, 120, 120, 0.08);
            margin-bottom: 0.4rem;
            font-size: 0.92rem;
        }
        code, pre { font-size: 0.88rem !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# Session state
# --------------------------------------------------------------------------
if "result" not in st.session_state:
    st.session_state.result = None
if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------------------------------
# Sidebar — agent roster + run history
# --------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🤖 Agents Loaded")
    agents = [
        ("🔍", "Error Analyzer"),
        ("✏️", "Code Editor"),
        ("⚙️", "Executor"),
        ("🧪", "Test Runner"),
        ("🛠️", "Debug Engine"),
    ]
    for icon, name in agents:
        st.markdown(f'<div class="agent-card">{icon} &nbsp; {name}</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## 🕘 Run History")
    if not st.session_state.history:
        st.caption("No runs yet this session.")
    else:
        for i, h in enumerate(reversed(st.session_state.history), 1):
            icon = "✅" if h["status"] == "success" else "❌"
            st.caption(f"{icon} Run {len(st.session_state.history) - i + 1} · {h['attempts']} attempt(s)")

    st.markdown("---")
    st.caption("Paste code, hit **Run Agentic Debugging**, and watch the agents work.")

# --------------------------------------------------------------------------
# Header
# --------------------------------------------------------------------------
st.title("🤖 AI Agentic Code Assistant")
st.caption("Multi-agent pipeline: analyze → edit → execute → test → debug, until your code runs clean.")

st.markdown("---")

# --------------------------------------------------------------------------
# Input area
# --------------------------------------------------------------------------
left, right = st.columns([3, 1])

with left:
    user_code = st.text_area(
        "Paste your Python code",
        height=340,
        placeholder="def add(a, b):\n    return a + b\n\nprint(add(2, '3'))",
        label_visibility="visible",
    )

with right:
    st.markdown("#### Options")
    max_attempts = st.slider("Max debug attempts", 1, 10, 5)
    show_raw = st.checkbox("Show raw result dict", value=False)
    st.markdown("&nbsp;")
    run_clicked = st.button("🚀 Run Agentic Debugging", type="primary", use_container_width=True)
    clear_clicked = st.button("🧹 Clear", use_container_width=True)

if clear_clicked:
    st.session_state.result = None
    st.rerun()

# --------------------------------------------------------------------------
# Run pipeline
# --------------------------------------------------------------------------
if run_clicked:
    if not user_code.strip():
        st.error("❌ No code provided. Paste some Python code first.")
    else:
        progress = st.progress(0, text="Starting agentic debugging...")
        stages = [
            "🔍 Analyzing code...",
            "✏️ Editing / patching...",
            "⚙️ Executing...",
            "🧪 Running tests...",
            "🛠️ Finalizing debug loop...",
        ]
        for i, stage in enumerate(stages, 1):
            progress.progress(i / len(stages), text=stage)
            time.sleep(0.15)

        try:
            result = debug_code(user_code, max_attempts=max_attempts)
        except TypeError:
            # Fallback if debug_code doesn't accept max_attempts
            result = debug_code(user_code)

        progress.empty()
        st.session_state.result = result
        st.session_state.history.append(
            {"status": result.get("status", "unknown"), "attempts": result.get("attempts", "?")}
        )

# --------------------------------------------------------------------------
# Results
# --------------------------------------------------------------------------
result = st.session_state.result

if result:
    st.markdown("## 🎯 Final Result")

    status = str(result.get("status", "unknown"))
    is_success = status.lower() in ("success", "passed", "ok", "fixed")
    pill_class = "status-success" if is_success else "status-fail"
    pill_label = f"{'✅' if is_success else '❌'} {status.upper()}"

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown(f'<span class="status-pill {pill_class}">{pill_label}</span>', unsafe_allow_html=True)
    with c2:
        st.metric("Attempts", result.get("attempts", "—"))

    st.markdown("### 📋 Analysis")
    st.info(result.get("analysis", "No analysis returned."))

    st.markdown("### 💻 Final Code")
    st.code(result.get("code", ""), language="python")
    st.download_button(
        "⬇️ Download fixed code",
        data=result.get("code", ""),
        file_name="fixed_code.py",
        mime="text/x-python",
    )

    st.markdown("### 📤 Output")
    st.code(result.get("output", ""), language="text")

    if show_raw:
        st.markdown("### 🗂️ Raw result")
        st.json(result)
else:
    st.info("Paste your code above and click **Run Agentic Debugging** to get started.")