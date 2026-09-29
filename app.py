import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stuff+ Model", layout="centered")
st.title("⚾ Stuff+ Pitch Quality Model")
st.caption("Physical pitch characteristics (velocity, movement, spin) scaled so 100 = league average.")

df = pd.read_csv("stuffplus_scores.csv")

pitcher_name = st.selectbox("Pick a pitcher", sorted(df["player_name"].dropna().unique()))
pitcher_df = df[df["player_name"] == pitcher_name].sort_values("stuff_plus", ascending=False)

st.subheader(f"{pitcher_name}'s Arsenal")
st.dataframe(
    pitcher_df[["pitch_type", "n_pitches", "stuff_plus"]]
        .rename(columns={"pitch_type": "Pitch", "n_pitches": "Pitches Thrown", "stuff_plus": "Stuff+"})
        .style.format({"Stuff+": "{:.1f}"}),
    hide_index=True,
)

st.divider()
st.subheader("League Leaderboard")
pitch_type_filter = st.selectbox("Pitch type", sorted(df["pitch_type"].unique()))
leaderboard = df[df["pitch_type"] == pitch_type_filter].sort_values("stuff_plus", ascending=False).head(15)
st.dataframe(
    leaderboard[["player_name", "n_pitches", "stuff_plus"]]
        .rename(columns={"player_name": "Pitcher", "n_pitches": "Pitches", "stuff_plus": "Stuff+"})
        .style.format({"Stuff+": "{:.1f}"}),
    hide_index=True,
)
