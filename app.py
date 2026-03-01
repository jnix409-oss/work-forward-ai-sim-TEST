import streamlit as st
import matplotlib.pyplot as plt

st.title("WorkForward AI — Organizational Restructure Simulation")

# --- Sliders ---
managers = st.slider("Number of Managers", 3, 40, 10)
employees = st.slider("Number of Employees", 20, 300, 80, step=5)
steps = st.slider("Simulation Steps", 20, 200, 60, step=10)

# --- Simulation function (TEMP) ---
# This is a placeholder so your app deploys cleanly.
# Next, we’ll replace this with your full OrgSim engine.
def run_compare(managers: int, employees: int, steps: int):
    reorg_mgrs = max(3, int(managers * 0.6))

    tasks_base = employees * steps * (0.15 + managers * 0.003)
    tasks_reorg = employees * steps * (0.12 + reorg_mgrs * 0.0025)

    baseline = {
        "steps": float(steps),
        "active_headcount": float(managers + employees),
        "tasks_completed": float(tasks_base),
        "avg_decision_latency_steps": float(max(0.5, 4.0 - managers * 0.08)),
        "avg_engagement": float(min(0.95, 0.82 + managers * 0.004 - employees * 0.0006)),
        "avg_burnout": float(min(0.95, 0.18 + employees * 0.0012)),
        "attrition_events": float(max(0.0, employees * 0.015 - managers * 0.08)),
    }

    reorg = {
        "steps": float(steps),
        "active_headcount": float(reorg_mgrs + employees),
        "tasks_completed": float(tasks_reorg),
        "avg_decision_latency_steps": float(max(0.5, 4.0 - reorg_mgrs * 0.08) + 0.8),
        "avg_engagement": float(max(0.05, baseline["avg_engagement"] - 0.07)),
        "avg_burnout": float(min(0.99, baseline["avg_burnout"] + 0.09)),
        "attrition_events": float(min(float(employees), baseline["attrition_events"] + 4.0)),
    }

    return baseline, reorg, reorg_mgrs


# --- Run button ---
if st.button("Run Simulation"):
    baseline, reorg, reorg_mgrs = run_compare(managers, employees, steps)
st.write("Inputs:", {"managers": managers, "employees": employees, "steps": steps})    st.subheader("Results")
    c1, c2 = st.columns(2)
    with c1:
        st.write("Baseline", baseline)
    with c2:
        st.write(f"Reorg (Managers = {reorg_mgrs})", reorg)

    st.subheader("Productivity Comparison")
    labels = ["Baseline", "Reorg"]
    values = [baseline["tasks_completed"], reorg["tasks_completed"]]

    fig = plt.figure()
    plt.bar(labels, values)
    plt.ylabel("Tasks Completed")
    st.pyplot(fig)

    st.subheader("Delta (Reorg - Baseline)")
    deltas = {k: reorg[k] - baseline[k] for k in baseline.keys()}
    st.write(deltas)
