
import streamlit as st
from datetime import date

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="TaskFlow | Productivity",
    page_icon="⚡",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f6f7ff, #eef2ff, #fdf2f8);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

h1, h2, h3 {
    color: #202044 !important;
    font-family: 'Poppins', sans-serif !important;
}

.hero {
    background: linear-gradient(120deg, #6C63FF, #9B5DE5, #F05AA6);
    padding: 35px;
    border-radius: 24px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 10px 30px rgba(108, 99, 255, 0.18);
}

.hero h1 {
    color: white !important;
    font-size: 38px !important;
    margin-bottom: 5px;
}

.hero p {
    color: #f3efff;
    font-size: 16px;
}

.stat-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 5px 20px rgba(50,50,100,0.05);
    border-left: 5px solid #7B68EE;
}

.stat-number {
    font-size: 30px;
    font-weight: 800;
    color: #292750;
}

.stat-label {
    color: #7d7d9b;
    font-size: 14px;
}

.task-card {
    background: white;
    border-radius: 16px;
    padding: 17px 20px;
    margin-bottom: 12px;
    border: 1px solid #eeeeff;
    box-shadow: 0px 4px 15px rgba(50,50,100,0.04);
}

.task-title {
    font-size: 16px;
    font-weight: 600;
    color: #282747;
}

.task-meta {
    font-size: 12px;
    color: #8585a3;
    margin-top: 5px;
}

.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
}

.high {
    background: #ffe5e9;
    color: #e64161;
}

.medium {
    background: #fff0d5;
    color: #b77900;
}

.low {
    background: #ddf8e8;
    color: #1e9652;
}

.section-label {
    color: #7B68EE;
    font-weight: 700;
    letter-spacing: 1px;
    font-size: 12px;
}

div[data-testid="stProgressBar"] > div > div > div {
    background: linear-gradient(90deg, #6C63FF, #F05AA6);
}

div.stButton > button {
    border-radius: 12px;
    font-weight: 600;
    border: 0px;
    transition: 0.2s;
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #6C63FF, #A15CE5);
    color: white;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 4px 12px rgba(108,99,255,0.2);
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border-radius: 18px;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "next_id" not in st.session_state:
    st.session_state.next_id = 1

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>⚡ TaskFlow</h1>
    <p>Your goals, your focus, your success. Organize your day beautifully.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- TASK STATISTICS ----------------
tasks = st.session_state.tasks

total_tasks = len(tasks)
completed_tasks = sum(task["completed"] for task in tasks)
pending_tasks = total_tasks - completed_tasks

progress = completed_tasks / total_tasks if total_tasks > 0 else 0

# ---------------- STAT CARDS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-label">📋 TOTAL TASKS</div>
        <div class="stat-number">{total_tasks}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="stat-card" style="border-left-color:#26C281">
        <div class="stat-label">✅ COMPLETED</div>
        <div class="stat-number">{completed_tasks}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="stat-card" style="border-left-color:#FFB547">
        <div class="stat-label">⏳ PENDING</div>
        <div class="stat-number">{pending_tasks}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- PROGRESS ----------------
st.subheader("🚀 Your Daily Progress")

st.progress(progress)
st.caption(f"You have completed {int(progress * 100)}% of your tasks.")

st.write("")

# ---------------- ADD TASK SECTION ----------------
st.markdown('<p class="section-label">CREATE A NEW TASK</p>', unsafe_allow_html=True)
st.subheader("✨ Add a Task")

with st.form("add_task_form", clear_on_submit=True):

    task_name = st.text_input(
        "Task name",
        placeholder="What do you want to accomplish today?"
    )

    col1, col2 = st.columns(2)

    with col1:
        priority = st.selectbox(
            "Priority",
            ["High", "Medium", "Low"]
        )

    with col2:
        due_date = st.date_input(
            "Due date",
            value=date.today()
        )

    submitted = st.form_submit_button(
        "➕ Add Task",
        use_container_width=True
    )

    if submitted:
        if task_name.strip():

            st.session_state.tasks.append({
                "id": st.session_state.next_id,
                "name": task_name.strip(),
                "priority": priority,
                "due_date": due_date,
                "completed": False
            })

            st.session_state.next_id += 1
            st.success("Task added successfully! 🎉")
            st.rerun()

        else:
            st.warning("Please enter a task name.")

st.write("")
st.divider()

# ---------------- TASK FILTER ----------------
st.markdown('<p class="section-label">YOUR WORKSPACE</p>', unsafe_allow_html=True)
st.subheader("📌 My Tasks")

filter_option = st.selectbox(
    "Filter tasks",
    ["All Tasks", "Pending", "Completed"]
)

search_text = st.text_input(
    "🔎 Search tasks",
    placeholder="Search by task name..."
)

# Apply filters
filtered_tasks = st.session_state.tasks.copy()

if filter_option == "Pending":
    filtered_tasks = [
        t for t in filtered_tasks if not t["completed"]
    ]

elif filter_option == "Completed":
    filtered_tasks = [
        t for t in filtered_tasks if t["completed"]
    ]

if search_text:
    filtered_tasks = [
        t for t in filtered_tasks
        if search_text.lower() in t["name"].lower()
    ]

# ---------------- DISPLAY TASKS ----------------
if not filtered_tasks:
    st.info("No tasks found. Add a new task to get started! 🌈")

else:

    for task in filtered_tasks:

        with st.container(border=True):

            col1, col2, col3 = st.columns([5, 1, 1])

            with col1:

                checked = st.checkbox(
                    task["name"],
                    value=task["completed"],
                    key=f"check_{task['id']}"
                )

                # Update completion status
                for t in st.session_state.tasks:
                    if t["id"] == task["id"]:
                        t["completed"] = checked

                priority_class = task["priority"].lower()

                st.markdown(
                    f"""
                    <span class="badge {priority_class}">
                        {task['priority']} Priority
                    </span>
                    <span class="task-meta">
                        📅 Due: {task['due_date'].strftime('%d %b %Y')}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                if st.button(
                    "🗑️",
                    key=f"delete_{task['id']}",
                    help="Delete task"
                ):
                    st.session_state.tasks = [
                        t for t in st.session_state.tasks
                        if t["id"] != task["id"]
                    ]
                    st.rerun()

            with col3:
                if task["completed"]:
                    st.markdown("🎉")

# ---------------- FOOTER ----------------
st.write("")
st.divider()

st.markdown("""
<div style="text-align:center; color:#9999b5; padding:10px">
    Made with 💜 Streamlit | Stay productive, stay focused.
</div>
""", unsafe_allow_html=True)
