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
    baseline = {
        "steps": float(steps),
        "active_headcount": float(managers + employees),
        "tasks_completed": float(employees * steps * 0.22),
        "avg_decision_latency_steps": float(max(0.5, 3.0 - managers * 0.05)),
        "avg_engagement": float(min(0.95, 0.78 + managers * 0.002 - employees * 0.0002)),
        "avg_burnout": float(min(0.95, 0.25 + employees * 0.0008)),
        "attrition_events": float(max(0.0, employees * 0.01 - managers * 0.05)),
    }

    # "Reorg" example: fewer managers (stress)
    reorg_mgrs = max(3, int(managers * 0.6))
    reorg = {
        "steps": float(steps),
        "active_headcount": float(reorg_mgrs + employees),
        "tasks_completed": float(employees * steps * 0.20),
        "avg_decision_latency_steps": float(max(0.5, 3.0 - reorg_mgrs * 0.05) + 0.6),
        "avg_engagement": float(max(0.1, baseline["avg_engagement"] - 0.04)),
        "avg_burnout": float(min(0.99, baseline["avg_burnout"] + 0.05)),
        "attrition_events": float(min(float(employees), baseline["attrition_events"] + 2.0)),
    }

    return baseline, reorg, reorg_mgrs


# --- Run button ---
if st.button("Run Simulation"):
    baseline, reorg, reorg_mgrs = run_compare(managers, employees, steps)

    st.subheader("Results")
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
