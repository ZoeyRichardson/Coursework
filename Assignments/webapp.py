import streamlit as st # Streamlit library for building the app

# --- TITLE PAGE ---
st.title("🍿 Binge Dashboard")
st.write("Your personal TV show tracker!")

# --- SHOW DATA ---
# Shows are already added with the number of episodes
default_shows = {
    "Pretty Little Liars": {"episodes": 160},
    "Game of Thrones": {"episodes": 73},
    "The Walking Dead": {"episodes": 177},
    "The Office": {"episodes": 201},
    "Supernatural": {"episodes": 327}
}

st.markdown("---") # Fun way to be more organized
st.subheader("➕ Add Your Own Show")

new_show = st.text_input("📺 Show Name") # Input show name

new_episodes = st.number_input("🎬 Number of Episodes", 1, 1000, 10) # Input number of episodes

if st.button("➕ Add Show to List"):
    if new_show:
        st.session_state.shows[new_show] = {"episodes": new_episodes}
        st.write(f"{new_show} added!")
    else:
        st.write("Please enter a show name!")

# --- STORE INFO ---
# Tracks calculated binge times
if "history" not in st.session_state:
    st.session_state.history = []

# This keeps shows currently being watched
if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

# This keeps data saved while streamlit is running
if "shows" not in st.session_state:
    st.session_state.shows = default_shows

# --- USER INPUT ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📺 Choose Your Show")

# Dropdown to selct a show from the list
    show = st.selectbox("Select a show:", list(st.session_state.shows.keys()))

# User input for how much they watch and how long the episodes are
    hours_per_day = st.slider("⏱ Hours watched per day:", 1, 10, 3)
    minutes_per_episode = st.slider("⏳ Minutes per episode:", 20, 90, 45)

# --- ADD TO WATCHLIST + CALCULATE BINGE TIME ---
if st.button("🍿 Add to Watch Plan"):

# Number of episodes from the selected show
    episodes = st.session_state.shows[show]["episodes"]

# Calculate total binge time
    total_hours = (episodes * minutes_per_episode) / 60
    days = total_hours / hours_per_day

# Save in history
    st.session_state.history.append({
        "show": show,
        "days": round(days, 1)
    })

# Add show to watchlist for tracking
    st.session_state.watchlist.append({
        "name": show,
        "episodes": episodes,
        "length": minutes_per_episode,
        "watched": 0,
        "hours_per_day": hours_per_day
    })

    st.write(f"Added {show} to your plan!")

with col2:
    st.subheader("🎬 Show Preview")

    selected = st.session_state.shows[show]
    st.write(f"📊 Episodes: {selected['episodes']}")

    st.markdown("---")

    st.subheader("📈 Watch History")

# Display calculations
    if st.session_state.history:
        for item in st.session_state.history:
            st.write(f"🍿 {item['show']} → {item['days']} days to finish")
    else:
        st.info("No shows added yet!")

# --- CONTINUE WATCHING ---
st.markdown("---")
st.subheader("📺 Continue Watching")

if st.session_state.watchlist:
    for i, show in enumerate(st.session_state.watchlist):

        st.write(f"🎬 {show['name']}")

# Slider to track how many episodes watched
        watched = st.slider(
            f"Episodes watched for {show['name']}",
            0,
            show["episodes"],
            show["watched"],
            key=f"watch_{i}"
        )

        show["watched"] = watched

# Calculate progress and reamining time
        progress = watched / show["episodes"]
        st.progress(progress)

        remaining = show["episodes"] - watched
        total_minutes = remaining * show["length"]
        total_hours = total_minutes / 60
        days_left = total_hours / show["hours_per_day"]

        st.write(f"⏳ {remaining} episodes left")
        st.write(f"📅 Finish in ~{days_left:.1f} days")

# Fun messages based on progress
        if progress == 1:
            st.write("🎉 Finished!")
        elif progress > 0.7:
            st.write("🔥 Almost done!")
        elif progress > 0.3:
            st.write("😎 Making good progress!")
        else:
           st.write("🍿 Just getting started!")

        st.markdown("---")
    else:
        st.info("Add a show above to start tracking!") 

# --- INSIGHTS ---
st.markdown("---")
st.subheader("🔥 Your Streaming Insight")

# Calculate average binge time across all shows added to history
if st.session_state.history:

    avg_days = sum(item["days"] for item in st.session_state.history) / len(st.session_state.history)

    st.metric("📊 Average Binge Time", f"{avg_days:.1f} days")

# Fun messages based on average binge time
    if avg_days <= 3:
        st.write("🔥 You’re a binge MASTER!")
    elif avg_days <= 7:
        st.write("😎 Pretty balanced watcher!")
    else:
        st.write("💀 You are in deep binge territory...")
else:
    st.write("Add shows to see your stats!")