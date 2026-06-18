import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="NGO Resource Planner", layout="wide")

# ---------------- UI ----------------
st.markdown("""
<style>
html, body, .stApp {
    background-color: #DED1BD;
    font-family: "Times New Roman";
    color: #683B2B;
    font-weight: bold;
}
h1 { font-size: 26px !important; text-align: center; }
label, div, p { font-size: 17px !important; }

.stSelectbox > div,
.stNumberInput > div {
    background-color: #683B2B !important;
    border-radius: 12px;
    padding: 6px;
}
input { color: #DED1BD !important; }

.stButton>button {
    background-color: #683B2B;
    color: #DED1BD;
    border-radius: 25px;
}

[data-testid="stFileUploader"] {
    background-color: #683B2B;
    border-radius: 12px;
    padding: 25px;
}

.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 80px;
}
</style>
""", unsafe_allow_html=True)

st.title("NGO Smart Resource Planner 🤎🌿")

file = st.file_uploader("Upload Dataset")

# ---------------- MAIN ----------------
if file:

    st.markdown("""
    <style>
    .block-container { max-width: 95% !important; padding-top: 20px;}
    </style>
    """, unsafe_allow_html=True)

    data = pd.read_csv(file)

    # Overview
    st.markdown("### Overview 📊")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Activities", len(data))
    c2.metric("Avg Success Rate", f"{data['Success_Rate'].mean():.2f}%")
    c3.metric("Total Budget", int(data["Budget"].sum()))

    # Table
    st.markdown("### Dataset Preview 📁")
    st.dataframe(data, use_container_width=True)

    # Graphs
    st.markdown("### Insights 📊")
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots()
        grp = data.groupby("Activity_Type")["Success_Rate"].mean()
        ax.bar(grp.index, grp.values, color="#683B2B")
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        grp = data.groupby("Region")["Budget"].mean()
        ax.barh(grp.index, grp.values, color="#683B2B")
        st.pyplot(fig)

    # ---------------- PLANNER ----------------
    st.markdown("### Smart Planning Tool 🤎🚀")

    col5, col6, col7 = st.columns(3)

    with col5:
        activity = st.selectbox("Activity Type", data["Activity_Type"].unique())
        team = st.number_input("Team Size", value=0.0)

    with col6:
        region = st.selectbox("Region", data["Region"].unique())
        resources = st.number_input("Resources Allocated", value=0.0)

    with col7:
        budget = st.number_input("Budget", value=0.0)

    if st.button("Generate Plan 🚀"):

        # 🔥 Improved scoring formula
        score = (team * 1.5) + (resources * 1.0) - (budget / 2000)

        st.subheader("🧠 Your Plan Analysis")
        st.write(f"• Team: {team} 👥")
        st.write(f"• Resources: {resources} ⚙")
        st.write(f"• Budget: ₹{budget} 💰")
        st.write(f"• Score: {round(score,2)} 📊")

        # ---------------- GOOD ----------------
        if score > 80:
            st.success("🌟 This is a GOOD plan! 🎉🔥")

        # ---------------- MODERATE ----------------
        elif score > 60:
            st.warning("⚠ This is a MODERATE plan 😐")

            best = {
                "Team": team + 10,
                "Resources": resources + 20,
                "Budget": budget + 10000
            }

            best_score = (best["Team"]*1.5)+(best["Resources"]*1.0)-(best["Budget"]/2000)

            st.subheader("🚀 Best Upgrade Plan 🌟")
            st.write(f"• Team: {best['Team']} 👥")
            st.write(f"• Resources: {best['Resources']} ⚙")
            st.write(f"• Budget: ₹{best['Budget']} 💰")
            st.write(f"• Score: {round(best_score,2)} 📈")

        # ---------------- BAD ----------------
        else:
            st.error("❌ This is a BAD plan 😬")

            # 🔥 FIXED LOGIC (NO MORE SAME VALUES)
            moderate = {
                "Team": team + 5,
                "Resources": resources + 10,
                "Budget": budget + 5000
            }

            best = {
                "Team": team + 10,
                "Resources": resources + 20,
                "Budget": budget + 10000
            }

            moderate_score = (moderate["Team"]*1.5)+(moderate["Resources"]*1.0)-(moderate["Budget"]/2000)
            best_score = (best["Team"]*1.5)+(best["Resources"]*1.0)-(best["Budget"]/2000)

            st.subheader("⚠ Moderate Plan Option")
            st.write(f"• Team: {moderate['Team']} 👥")
            st.write(f"• Resources: {moderate['Resources']} ⚙")
            st.write(f"• Budget: ₹{moderate['Budget']} 💰")
            st.write(f"• Score: {round(moderate_score,2)} 📊")

            st.subheader("🌟 Best Plan Option 🚀")
            st.write(f"• Team: {best['Team']} 👥")
            st.write(f"• Resources: {best['Resources']} ⚙")
            st.write(f"• Budget: ₹{best['Budget']} 💰")
            st.write(f"• Score: {round(best_score,2)} 📈")

else:
    st.write("Upload dataset to begin 📂✨")