
# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.express as px
# import os

# # Page configuration
# st.set_page_config(page_title="🎷 Spotify Listening Insights", layout="wide")
# st.title("🎷 Spotify Listening History Dashboard")

# # Correct file path (inside spotify_history folder)
# file_path = "spotify_history.csv"


# # Load data
# @st.cache_data
# def load_data(file_path):
#     df = pd.read_csv(file_path)
#     df.dropna(inplace=True)
#     df['ts'] = pd.to_datetime(df['ts'])
#     df['date'] = df['ts'].dt.date
#     df['hour'] = df['ts'].dt.hour
#     df['month'] = df['ts'].dt.to_period("M").astype(str)
#     return df

# # Check if the file exists
# if os.path.exists(file_path):
#     df = load_data(file_path)
#     st.success("✅ Data Loaded Successfully!")

#     # Preview
#     st.subheader("📌 Data Preview")
#     st.dataframe(df.head(20), use_container_width=True)

#     # Summary stats
#     st.subheader("📊 Summary Statistics")
#     st.write(df.describe(include='all'))

#     # Top Artists
#     st.subheader("🎤 Top 10 Most Played Artists")
#     top_artists = df['artist_name'].value_counts().head(10)
#     fig1, ax1 = plt.subplots()
#     sns.barplot(x=top_artists.values, y=top_artists.index, ax=ax1, palette="mako")
#     ax1.set_xlabel("Play Count")
#     ax1.set_ylabel("Artist")
#     st.pyplot(fig1)

#     # Top Tracks
#     st.subheader("🎶 Top 10 Most Played Tracks")
#     top_tracks = df['track_name'].value_counts().head(10)
#     fig2, ax2 = plt.subplots()
#     sns.barplot(x=top_tracks.values, y=top_tracks.index, ax=ax2, palette="rocket")
#     ax2.set_xlabel("Play Count")
#     ax2.set_ylabel("Track")
#     st.pyplot(fig2)

#     # Monthly Trend
#     st.subheader("📈 Monthly Listening Trend")
#     monthly_data = df.groupby("month")['track_name'].count().reset_index()
#     fig3, ax3 = plt.subplots(figsize=(10, 4))
#     sns.lineplot(x="month", y="track_name", data=monthly_data, marker="o", ax=ax3)
#     ax3.set_title("Monthly Track Plays")
#     ax3.set_xlabel("Month")
#     ax3.set_ylabel("Plays")
#     plt.xticks(rotation=45)
#     st.pyplot(fig3)

#     # Heatmap of Listening Patterns
#     st.subheader("🕓 Listening Pattern by Day & Hour")
#     heatmap_data = df.groupby([df['ts'].dt.date, df['hour']]).size().unstack(fill_value=0)
#     fig4, ax4 = plt.subplots(figsize=(12, 6))
#     sns.heatmap(heatmap_data.T, cmap="viridis", ax=ax4)
#     ax4.set_xlabel("Date")
#     ax4.set_ylabel("Hour of Day")
#     st.pyplot(fig4)

#     # Platform Usage Pie Chart
#     st.subheader("💻 Platform Usage Distribution")
#     platform_count = df['platform'].value_counts().reset_index()
#     platform_count.columns = ['Platform', 'Count']
#     fig5 = px.pie(
#         platform_count,
#         values='Count',
#         names='Platform',
#         title='Platform Usage',
#         hole=0.3
#     )
#     fig5.update_traces(textinfo='percent+label')
#     fig5.update_layout(width=700, height=500, title_font_size=20)
#     st.plotly_chart(fig5, use_container_width=True)

# else:
#     st.error("❌ File not found. Please check the path: spotify_history.csv")


# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.express as px

# # Page configuration
# st.set_page_config(page_title="🎷 Spotify Listening Insights", layout="wide")
# st.title("🎷 Spotify Listening History Dashboard")

# # File uploader
# uploaded_file = st.file_uploader("📁 Upload your 'spotify_history.csv' file", type="csv")

# # Load data
# @st.cache_data
# def load_data(file):
#     df = pd.read_csv(file)
#     df.dropna(inplace=True)
#     df['ts'] = pd.to_datetime(df['ts'])
#     df['date'] = df['ts'].dt.date
#     df['hour'] = df['ts'].dt.hour
#     df['month'] = df['ts'].dt.to_period("M").astype(str)
#     return df

# # Run app logic if file is uploaded
# if uploaded_file is not None:
#     df = load_data(uploaded_file)
#     st.success("✅ Data Loaded Successfully!")

#     # Preview
#     st.subheader("📌 Data Preview")
#     st.dataframe(df.head(20), use_container_width=True)

#     # Summary stats
#     st.subheader("📊 Summary Statistics")
#     st.write(df.describe(include='all'))

#     # Top Artists
#     st.subheader("🎤 Top 10 Most Played Artists")
#     top_artists = df['artist_name'].value_counts().head(10)
#     fig1, ax1 = plt.subplots()
#     sns.barplot(x=top_artists.values, y=top_artists.index, ax=ax1, palette="mako")
#     ax1.set_xlabel("Play Count")
#     ax1.set_ylabel("Artist")
#     st.pyplot(fig1)

#     # Top Tracks
#     st.subheader("🎶 Top 10 Most Played Tracks")
#     top_tracks = df['track_name'].value_counts().head(10)
#     fig2, ax2 = plt.subplots()
#     sns.barplot(x=top_tracks.values, y=top_tracks.index, ax=ax2, palette="rocket")
#     ax2.set_xlabel("Play Count")
#     ax2.set_ylabel("Track")
#     st.pyplot(fig2)

#     # Monthly Trend
#     st.subheader("📈 Monthly Listening Trend")
#     monthly_data = df.groupby("month")['track_name'].count().reset_index()
#     fig3, ax3 = plt.subplots(figsize=(10, 4))
#     sns.lineplot(x="month", y="track_name", data=monthly_data, marker="o", ax=ax3)
#     ax3.set_title("Monthly Track Plays")
#     ax3.set_xlabel("Month")
#     ax3.set_ylabel("Plays")
#     plt.xticks(rotation=45)
#     st.pyplot(fig3)

#     # Heatmap of Listening Patterns
#     st.subheader("🕓 Listening Pattern by Day & Hour")
#     heatmap_data = df.groupby([df['ts'].dt.date, df['hour']]).size().unstack(fill_value=0)
#     fig4, ax4 = plt.subplots(figsize=(12, 6))
#     sns.heatmap(heatmap_data.T, cmap="viridis", ax=ax4)
#     ax4.set_xlabel("Date")
#     ax4.set_ylabel("Hour of Day")
#     st.pyplot(fig4)

#     # Platform Usage Pie Chart
#     st.subheader("💻 Platform Usage Distribution")
#     platform_count = df['platform'].value_counts().reset_index()
#     platform_count.columns = ['Platform', 'Count']
#     fig5 = px.pie(
#         platform_count,
#         values='Count',
#         names='Platform',
#         title='Platform Usage',
#         hole=0.3
#     )
#     fig5.update_traces(textinfo='percent+label')
#     fig5.update_layout(width=700, height=500, title_font_size=20)
#     st.plotly_chart(fig5, use_container_width=True)

# else:
#     st.warning("📂 Please upload your 'spotify_history.csv' file to view insights.")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ---- Page config ----
st.set_page_config(page_title="🎷 Spotify Listening Insights", layout="wide", initial_sidebar_state="auto")

# ---- Custom CSS ----
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #121212;
            color: #f0f0f0;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTitle, .stHeader, .stSubheader {
            color: #1DB954 !important;
        }
        .block-container {
            padding: 1rem 2rem;
        }
        .stMetric {
            background: #1f1f1f;
            border-radius: 0.5rem;
            padding: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Header ----
st.title("🎷 Spotify Listening History Dashboard")

# ---- Load CSV ----
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df.dropna(inplace=True)
    df['ts'] = pd.to_datetime(df['ts'])
    df['date'] = df['ts'].dt.date
    df['hour'] = df['ts'].dt.hour
    df['month'] = df['ts'].dt.to_period("M").astype(str)
    return df

# ---- File uploader ----
uploaded_file = st.file_uploader("📁 Upload your spotify_history.csv file", type="csv")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # ---- Dataset Preview ----
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    # ---- Metrics ----
    st.subheader("📊 Summary Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("🎧 Total Songs Played", len(df))
    col2.metric("🎵 Unique Tracks", df['track_name'].nunique())
    col3.metric("⏱️ Total Listening Time (min)", int(df['ms_played'].sum() / 60000))

    # ---- Hourly Listening Activity ----
    st.subheader("⏰ Listening Activity by Hour")
    hour_data = df.groupby("hour")["ms_played"].sum().reset_index()
    hour_data["Minutes Played"] = hour_data["ms_played"] / 60000

    fig1 = px.bar(hour_data, x="hour", y="Minutes Played",
                  title="Listening Minutes by Hour",
                  template="plotly_dark", color_discrete_sequence=["#1DB954"])
    st.plotly_chart(fig1, use_container_width=True)

    # ---- Top Artists ----
    st.subheader("🎤 Top Artists")
    top_artists = df.groupby("artist_name")["ms_played"].sum().reset_index()
    top_artists["Minutes Played"] = top_artists["ms_played"] / 60000
    top_artists = top_artists.sort_values("Minutes Played", ascending=False).head(10)

    fig2 = px.bar(top_artists, x="Minutes Played", y="artist_name", orientation='h',
                  title="Top 10 Artists", template="plotly_dark", color_discrete_sequence=["#03DAC6"])
    st.plotly_chart(fig2, use_container_width=True)

    # ---- Top Tracks ----
    st.subheader("🎶 Top Tracks")
    top_tracks = df.groupby("track_name")["ms_played"].sum().reset_index()
    top_tracks["Minutes Played"] = top_tracks["ms_played"] / 60000
    top_tracks = top_tracks.sort_values("Minutes Played", ascending=False).head(10)

    fig3 = px.bar(top_tracks, x="Minutes Played", y="track_name", orientation='h',
                  title="Top 10 Tracks", template="plotly_dark", color_discrete_sequence=["#BB86FC"])
    st.plotly_chart(fig3, use_container_width=True)

    # ---- Monthly Listening ----
    st.subheader("📅 Monthly Listening Trends")
    monthly = df.groupby("month")["ms_played"].sum().reset_index()
    monthly["Minutes Played"] = monthly["ms_played"] / 60000

    fig4 = px.line(monthly, x="month", y="Minutes Played",
                   title="Monthly Listening Time",
                   markers=True, template="plotly_dark",
                   line_shape='spline', color_discrete_sequence=["#FF6F61"])
    st.plotly_chart(fig4, use_container_width=True)

else:
    st.warning("👆 Please upload your `spotify_history.csv` file to begin.")
