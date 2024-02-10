# TASK 2 (abbreviated):
# Load the .tsv file, extract some data from it and save it in JSON format. 
# We are interested in the following information from each row:

# PRIMARYTITLE (title),
# DIRECTOR (director/directors),
# CAST (actors),
# GENRES (list of genres),
# STARTYEAR (release year).

# Convert the movie data into a list, where each movie is represented as a dictionary 
# containing the following items:

# title (movie title),
# directors (list of all directors or an empty list if no director is listed),
# cast (list of all actors or an empty list if no actor is listed),
# genres (list of all genres the movie belongs to),
# decade (decade in which the movie was made).
# Because the TSV format does not allow representing lists, 
# actors and directors are provided as a single string with individual values separated by commas. 
# Use a list in the JSON format for clarity, for example, to see how many actors or directors are in the list. 
# It is possible that a movie does not contain information about directors or actors, 
# but the others are always provided. 
# The decade is always the first year of the decade, for example, 
# the year 1987 belongs to the 1980s decade, and the year 2017 belongs to the 2010s decade.



# Save the created list of dictionaries to a json file. 

# If no director or actor is listed, the respective item must be an empty list [], 
# not a list with a string of zero length [""].
# Don't forget to convert the year to a number before determining the decade. 
# Determining the decade is easiest using arithmetic operations (multiplication, division).
# The json.dump function (as well as json.dumps) takes an optional parameter indent, 
# which allows you to set the number of spaces by which each nested line should be indented. 
# This can achieve a nicely formatted output, as shown in the example below (4 spaces are used there).

#--------------------------------------------------

import json
import pandas as pd

# Load the tsv file while defining the separator as tabulator
netflix_titles = pd.read_csv("netflix_titles.tsv",sep='\t')

# Select the columns of interest and rename them accordingly
netflix_titles=(netflix_titles[['PRIMARYTITLE', 'DIRECTOR', 'CAST','GENRES', 'STARTYEAR']])
netflix_titles.rename(columns={"PRIMARYTITLE": "title", "DIRECTOR": "directors", "CAST": "cast", "GENRES": "genres", "STARTYEAR": "decade"}, inplace=True)


# Transform pandas df into a dictionary, using to_dict method with parameter orient= ‘records’,
#which creates lists like [{column -> value}, … , {column -> value}]
movies_dictionaries= netflix_titles.to_dict(orient='records') 

# Iterate through the dictionary, replace NaN values with empty lists
# For multiple value entries (more directors or actors or genres) split them using ','

for movie in movies_dictionaries:
    if pandas.isnull(movie['directors']):
        movie['directors'] = []
    else:
        movie['directors'] = (movie['directors']).split(", ") 

    if pandas.isnull(movie['cast']):
        movie['cast'] = []
    else:
        movie['cast'] = (movie['cast']).split(", ")
    
    movie['genres'] = (movie['genres']).split(",")
    movie['decade'] = (movie['decade']//10)*10 #calculate the decade by using Floor Division

# Dump the dictionary to a JSON file using indent 4 for better readability
with open ('movies_2.json', 'w', encoding='utf-8') as outfile:
    json.dump(movies_dictionaries, outfile, ensure_ascii=False, indent=4)
