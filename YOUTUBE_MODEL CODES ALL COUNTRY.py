## UNIOTED STATE YOUTUBE_CODE ##

import pandas as pd
import numpy as np
import json

# CSV file read
data = pd.read_csv(r'C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\INTERNSHIP PROJECTS\archive (2)\USvideos.csv')

# JSON file read
with open('C:/Users/Saujanya Gadge/OneDrive/Desktop/internship/INTERNSHIP PROJECTS/archive (2)/US_category_id.json') as f:
    category_data = json.load(f)

# Category ID to Name Mapping
category_mapping = {}
for item in category_data['items']:
    category_mapping[int(item['id'])] = item['snippet']['title']

data['category_name'] = data['category_id'].map(category_mapping)

# Missing values check
print(data.isnull().sum())

# Unnecessary columns drop (जर लागलं तर)
data.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'], axis=1, inplace=True)

data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')
data['publish_time'] = pd.to_datetime(data['publish_time'])

data.drop_duplicates(inplace=True)

from textblob import TextBlob

# Title Sentiment
data['title_sentiment'] = data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

data.to_csv('Cleaned_USvideos.csv', index=False)
print("DONE...!!!")

## RUSSSIA YOUTUBE_CODE##

import pandas as pd
import numpy as np
import json

# CSV file read
data = pd.read_csv(r'C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\INTERNSHIP PROJECTS\archive (2)\RUvideos.csv', encoding='latin1')

# JSON file read
with open('C:/Users/Saujanya Gadge/OneDrive/Desktop/internship/INTERNSHIP PROJECTS/archive (2)/RU_category_id.json') as f:
    category_data = json.load(f)

# Category ID to Name Mapping
category_mapping = {}
for item in category_data['items']:
    category_mapping[int(item['id'])] = item['snippet']['title']

data['category_name'] = data['category_id'].map(category_mapping)

# Missing values check
print(data.isnull().sum())

# Unnecessary columns drop (जर लागलं तर)
data.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'], axis=1, inplace=True)

data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')
data['publish_time'] = pd.to_datetime(data['publish_time'])

data.drop_duplicates(inplace=True)

from textblob import TextBlob

# Title Sentiment
data['title_sentiment'] = data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

data.to_csv('Cleaned_RUvideos.csv', index=False)
print("DONE...!!!")




## INDIA YOUTUBE_CODE ###

import pandas as pd
import numpy as np
import json

# CSV file read
data = pd.read_csv(r'C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\INTERNSHIP PROJECTS\INvideos.csv')

# JSON file read
with open('C:/Users/Saujanya Gadge/OneDrive/Desktop/internship/INTERNSHIP PROJECTS/IN_category_id.json') as f:
    category_data = json.load(f)

# Category ID to Name Mapping
category_mapping = {}
for item in category_data['items']:
    category_mapping[int(item['id'])] = item['snippet']['title']

data['category_name'] = data['category_id'].map(category_mapping)

# Missing values check
print(data.isnull().sum())

# Unnecessary columns drop (जर लागलं तर)
data.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'], axis=1, inplace=True)

data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')
data['publish_time'] = pd.to_datetime(data['publish_time'])

data.drop_duplicates(inplace=True)

from textblob import TextBlob

# Title Sentiment
data['title_sentiment'] = data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

data.to_csv('Cleaned_INvideos.csv', index=False)
print("DONE...!!!")




#### MAXICO YOUTUBE_CODE##

import pandas as pd
import numpy as np
import json


# CSV file read
data = pd.read_csv(r'C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\INTERNSHIP PROJECTS\archive (2)\MXvideos.csv' , encoding='latin1')

# JSON file read
with open('C:/Users/Saujanya Gadge/OneDrive/Desktop/internship/INTERNSHIP PROJECTS/archive (2)/MX_category_id.json') as f:
    category_data = json.load(f)

# Category ID to Name Mapping
category_mapping = {}
for item in category_data['items']:
    category_mapping[int(item['id'])] = item['snippet']['title']

data['category_name'] = data['category_id'].map(category_mapping)

# Missing values check
print(data.isnull().sum())

# Unnecessary columns drop (जर लागलं तर)
data.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'], axis=1, inplace=True)

data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')
data['publish_time'] = pd.to_datetime(data['publish_time'])

data.drop_duplicates(inplace=True)

from textblob import TextBlob

# Title Sentiment
data['title_sentiment'] = data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

data.to_csv('Cleaned_MXvideos.csv', index=False)
print("DONE...!!!")




#### SOUTHKOREA YOUTUBE_CODE##

import pandas as pd
import numpy as np
import json


# CSV file read
data = pd.read_csv(r'C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\INTERNSHIP PROJECTS\archive (2)\KRvideos.csv' , encoding='latin1')

# JSON file read
with open('C:/Users/Saujanya Gadge/OneDrive/Desktop/internship/INTERNSHIP PROJECTS/archive (2)/KR_category_id.json') as f:
    category_data = json.load(f)

# Category ID to Name Mapping
category_mapping = {}
for item in category_data['items']:
    category_mapping[int(item['id'])] = item['snippet']['title']

data['category_name'] = data['category_id'].map(category_mapping)

# Missing values check
print(data.isnull().sum())

# Unnecessary columns drop (जर लागलं तर)
data.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'], axis=1, inplace=True)

data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')
data['publish_time'] = pd.to_datetime(data['publish_time'])

data.drop_duplicates(inplace=True)

from textblob import TextBlob

# Title Sentiment
data['title_sentiment'] = data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

data.to_csv('Cleaned_KRvideos.csv', index=False)
print("DONE...!!!")



##JAPAN YOUTUBE_CODE ###

import pandas as pd
import numpy as np
import json


# CSV file read
data = pd.read_csv(r'C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\INTERNSHIP PROJECTS\archive (2)\JPvideos.csv', encoding='latin1')

# JSON file read
with open('C:/Users/Saujanya Gadge/OneDrive/Desktop/internship/INTERNSHIP PROJECTS/archive (2)/JP_category_id.json') as f:
    category_data = json.load(f)

# Category ID to Name Mapping
category_mapping = {}
for item in category_data['items']:
    category_mapping[int(item['id'])] = item['snippet']['title']

data['category_name'] = data['category_id'].map(category_mapping)

# Missing values check
print(data.isnull().sum())

# Unnecessary columns drop (जर लागलं तर)
data.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'], axis=1, inplace=True)

data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')
data['publish_time'] = pd.to_datetime(data['publish_time'])

data.drop_duplicates(inplace=True)

from textblob import TextBlob

# Title Sentiment
data['title_sentiment'] = data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

data.to_csv('Cleaned_JPvideos.csv', index=False)
print("DONE...!!!")




##### CANADA YOUTUBE_CODE ####

import pandas as pd
import numpy as np
import json

# CSV file read
data = pd.read_csv(r'C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\INTERNSHIP PROJECTS\archive (2)\CAvideos.csv')

# JSON file read
with open('C:/Users/Saujanya Gadge/OneDrive/Desktop/internship/INTERNSHIP PROJECTS/archive (2)/CA_categ' \
'ory_id.json') as f:
    category_data = json.load(f)

# Category ID to Name Mapping
category_mapping = {}
for item in category_data['items']:
    category_mapping[int(item['id'])] = item['snippet']['title']

data['category_name'] = data['category_id'].map(category_mapping)

# Missing values check
print(data.isnull().sum())

# Unnecessary columns drop (जर लागलं तर)
data.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'], axis=1, inplace=True)

data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')
data['publish_time'] = pd.to_datetime(data['publish_time'])

data.drop_duplicates(inplace=True)

from textblob import TextBlob

# Title Sentiment
data['title_sentiment'] = data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

data.to_csv('Cleaned_CAvideos.csv', index=False)
print("DONE...!!!")



