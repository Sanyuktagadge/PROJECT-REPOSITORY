import sqlite3
import pandas as pd

# CSV फाइल वाचा
data = pd.read_csv(r"C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\INTERNSHIP PROJECTS\Cleaned_JPvideos.csv")

# SQLite DB कनेक्ट करा (DB फाइल तयार होईल)
conn = sqlite3.connect('youtube_trending.db')

# DataFrame SQL table मध्ये लावा
data.to_sql('IN_trending', conn, if_exists='replace', index=False)

print("Data loaded into SQLite database successfully!")

# Top 10 categories by average views
query_avg_views = """
SELECT category_name, AVG(views) as avg_views
FROM IN_trending
GROUP BY category_name
ORDER BY avg_views DESC
LIMIT 10;
"""

df_avg_views = pd.read_sql_query(query_avg_views, conn)
print("\nTop 10 Categories by Average Views:")
print(df_avg_views)

#Count of videos by sentiment category
query_sentiment_count = """
SELECT 
    CASE 
        WHEN title_sentiment > 0 THEN 'Positive'
        WHEN title_sentiment < 0 THEN 'Negative'
        ELSE 'Neutral'
    END as sentiment,
    COUNT(*) as video_count
FROM IN_trending
GROUP BY sentiment;
"""

df_sentiment_count = pd.read_sql_query(query_sentiment_count, conn)
print("\nVideo Count by Sentiment:")
print(df_sentiment_count)

# Top video by views per trending date
query_top_video = """
SELECT trending_date, title, MAX(views) as max_views
FROM IN_trending
GROUP BY trending_date;
"""

df_top_video = pd.read_sql_query(query_top_video, conn)
print("\nTop Video per Trending Date:")
print(df_top_video.head())

# Close connection
conn.close()