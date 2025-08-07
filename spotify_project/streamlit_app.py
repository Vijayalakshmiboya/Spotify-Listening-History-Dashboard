
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Page configuration
st.set_page_config(page_title="🎷 Spotify Listening Insights", layout="wide")
st.title("🎷 Spotify Listening History Dashboard")

# Correct file path (inside spotify_history folder)
file_path = "spotify_history.csv"


# Load data
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df['ts'] = pd.to_datetime(df['ts'])
    df['date'] = df['ts'].dt.date
    df['hour'] = df['ts'].dt.hour
    df['month'] = df['ts'].dt.to_period("M").astype(str)
    return df

# Check if the file exists
if os.path.exists(file_path):
    df = load_data(file_path)
    st.success("✅ Data Loaded Successfully!")

    # Preview
    st.subheader("📌 Data Preview")
    st.dataframe(df.head(20), use_container_width=True)

    # Summary stats
    st.subheader("📊 Summary Statistics")
    st.write(df.describe(include='all'))

    # Top Artists
    st.subheader("🎤 Top 10 Most Played Artists")
    top_artists = df['artist_name'].value_counts().head(10)
    fig1, ax1 = plt.subplots()
    sns.barplot(x=top_artists.values, y=top_artists.index, ax=ax1, palette="mako")
    ax1.set_xlabel("Play Count")
    ax1.set_ylabel("Artist")
    st.pyplot(fig1)

    # Top Tracks
    st.subheader("🎶 Top 10 Most Played Tracks")
    top_tracks = df['track_name'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    sns.barplot(x=top_tracks.values, y=top_tracks.index, ax=ax2, palette="rocket")
    ax2.set_xlabel("Play Count")
    ax2.set_ylabel("Track")
    st.pyplot(fig2)

    # Monthly Trend
    st.subheader("📈 Monthly Listening Trend")
    monthly_data = df.groupby("month")['track_name'].count().reset_index()
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.lineplot(x="month", y="track_name", data=monthly_data, marker="o", ax=ax3)
    ax3.set_title("Monthly Track Plays")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Plays")
    plt.xticks(rotation=45)
    st.pyplot(fig3)

    # Heatmap of Listening Patterns
    st.subheader("🕓 Listening Pattern by Day & Hour")
    heatmap_data = df.groupby([df['ts'].dt.date, df['hour']]).size().unstack(fill_value=0)
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    sns.heatmap(heatmap_data.T, cmap="viridis", ax=ax4)
    ax4.set_xlabel("Date")
    ax4.set_ylabel("Hour of Day")
    st.pyplot(fig4)

    # Platform Usage Pie Chart
    st.subheader("💻 Platform Usage Distribution")
    platform_count = df['platform'].value_counts().reset_index()
    platform_count.columns = ['Platform', 'Count']
    fig5 = px.pie(
        platform_count,
        values='Count',
        names='Platform',
        title='Platform Usage',
        hole=0.3
    )
    fig5.update_traces(textinfo='percent+label')
    fig5.update_layout(width=700, height=500, title_font_size=20)
    st.plotly_chart(fig5, use_container_width=True)

else:
    st.error("❌ File not found. Please check the path:spotify_history.csv")
