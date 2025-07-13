import streamlit as st
import pandas as pd
import joblib

# Load model and column encodings
model = joblib.load("toss_win_model.pkl")
columns = joblib.load("columns.pkl")

# Set custom page config
st.set_page_config(page_title="IPL Toss Win Predictor", page_icon="🏏", layout="centered")

# ------------------------- UI Elements -------------------------

st.title("🏆 IPL Toss Win Predictor")
st.markdown(
    """
    ### 🧠 What Does It Do?
    This ML-powered app predicts whether the **toss winner is likely to win** the match or not
    based on the **toss decision** and **venue**.

    👉 Choose values below to simulate an IPL match scenario and get real-time predictions!
    """
)

# ------------------------- Input Section -------------------------

# Dropdown values
toss_winner = st.selectbox("🏏 Select Toss Winner", sorted(set(col.replace("toss_winner_", "") for col in columns if "toss_winner_" in col)))
toss_decision = st.selectbox("⚖️ Select Toss Decision", ["bat", "field"])
venue = st.selectbox("📍 Select Venue", sorted(set(col.replace("venue_", "") for col in columns if "venue_" in col)))

# ------------------------- Prediction -------------------------

if st.button("🔮 Predict Match Outcome"):
    # Prepare input vector
    input_df = pd.DataFrame(columns=columns)
    input_df.loc[0] = 0
    input_df.at[0, f"toss_winner_{toss_winner}"] = 1
    input_df.at[0, f"toss_decision_{toss_decision}"] = 1
    input_df.at[0, f"venue_{venue}"] = 1

    # Predict
    result = model.predict(input_df)[0]

    st.markdown("---")
    st.subheader("📢 Prediction Result:")
    
    if result == 1:
        st.success("🎉 The toss winner is **likely to win** the match!")
    else:
        st.error("❌ The toss winner **might not win** the match.")

# ------------------------- Footer -------------------------

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        Built with ❤️ by <a href="https://github.com/adarsh-1262" target="_blank">Adarsh Singh</a> ·
        <a href="https://www.linkedin.com/in/adarsh-singgh" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)
