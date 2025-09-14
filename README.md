# 🎷 Spotify Listening Insights Dashboard  

## 📌 Problem Statement  
With the massive amount of music people stream daily, it becomes difficult to **track, analyze, and understand personal listening habits**. Spotify provides raw listening history data, but it’s not user-friendly or insightful in its raw format. Users need an **interactive dashboard** that converts this data into meaningful insights about their music preferences, daily patterns, and overall listening behavior.  

---

## 🎯 Why This Project?  
- To **visualize personal music consumption** and uncover patterns like when you listen the most (day vs. night).  
- To discover your **top artists and songs** over time.  
- To monitor **listening trends monthly or yearly**.  
- To help music enthusiasts **connect data with lifestyle habits** (study time, workouts, travel, etc.).  

This project is not just about charts—it’s about **turning raw data into personal stories about music**.  

---

## 🚀 Features  
- 📂 Upload your Spotify streaming history (`spotify_history.csv`)  
- 🔍 Dataset preview (first 10 rows)  
- 📊 Key stats: total songs played, unique tracks, total listening time  
- ⏰ Hourly listening activity chart  
- 🎤 Top 10 artists (minutes played)  
- 🎶 Top 10 tracks (minutes played)  
- 📅 Monthly listening trends (interactive line chart)  
- 🎨 Dark Spotify-inspired theme for better visuals  

---

## 🛠️ Tech Stack  
- **Streamlit** – interactive UI  
- **Pandas** – data wrangling  
- **Plotly Express** – modern visualizations  
- **Matplotlib** – additional plotting support  

---

## 📂 Dataset Format  
The CSV should contain the following columns:  
- `spotify_track_uri`  
- `ts` (timestamp of playback)  
- `platform`  
- `ms_played` (milliseconds played)  
- `track_name`  
- `artist_name`  
- `album_name`  
- `reason_start`  
- `reason_end`  
- `shuffle`  
- `skipped`

  
**Install dependencies:**

pip install -r requirements.txt

## ▶️ How to Run  
```bash
# Clone the repository
git clone https://github.com/your-username/spotify-insights.git
cd spotify-insights

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
