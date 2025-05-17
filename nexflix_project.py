import pandas as pd

# Load Netflix dataset
df = pd.read_csv('netflix_titles.csv')

# View shape and columns
"""
print("Rows & Columns:", df.shape)
print("\nColumn Names:")
print(df.columns)

# View first few rows
print("\nFirst 5 rows:")
print(df.head())
"""
import matplotlib.pyplot as plt
import seaborn as sns
"""
# Count of Movies vs TV Shows
sns.countplot(x='type', data=df)
plt.title('Number of Movies vs TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Convert release_year to numeric (in case it's not)
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# Plot number of titles per release year
df['release_year'].value_counts().sort_index().plot(kind='bar', figsize=(14,6))
plt.title('Number of Netflix Titles Released Per Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()

# Drop missing countries
country_data = df['country'].dropna()

# Split multiple countries and count frequency
from collections import Counter
countries = country_data.str.split(', ')
country_list = countries.explode()
top_countries = country_list.value_counts().head(10)

# Plot
top_countries.plot(kind='barh', color='coral')
plt.title('Top 10 Countries with Most Netflix Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Drop missing values in 'listed_in' (genres)
genre_data = df['listed_in'].dropna()
genres = genre_data.str.split(', ')
genre_list = genres.explode()
top_genres = genre_list.value_counts().head(10)

# Plot
top_genres.plot(kind='bar', color='skyblue')
plt.title('Top 10 Netflix Genres')
plt.xlabel('Genre')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()
"""
##Most frequent director
# Drop missing directors
director_data = df['director'].dropna()

# Count top 10 directors
top_directors = director_data.value_counts().head(10)

# Plot
top_directors.plot(kind='barh', color='purple')
plt.title('Top 10 Directors on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

#Most featured actor
# Drop missing values in cast column
cast_data = df['cast'].dropna()

# Split and explode the actor names
actors = cast_data.str.split(', ')
actor_list = actors.explode()
top_actors = actor_list.value_counts().head(10)

# Plot
top_actors.plot(kind='bar', color='green')
plt.title('Top 10 Actors on Netflix')
plt.xlabel('Actor')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()

#Duration pattern(movies only)
# Filter only movies
movie_df = df[df['type'] == 'Movie']

# Clean duration
movie_df['duration_cleaned'] = movie_df['duration'].str.replace(' min', '')
movie_df['duration_cleaned'] = pd.to_numeric(movie_df['duration_cleaned'], errors='coerce')

# Plot distribution
plt.figure(figsize=(12,6))
sns.histplot(movie_df['duration_cleaned'].dropna(), bins=30, color='tomato')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.show()
