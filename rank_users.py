import os
import pandas as pd
import scipy.spatial
import json

dataset_dir = './dataset'
filepath = os.path.join(dataset_dir, 'users.csv')
file_dst = os.path.join(dataset_dir, 'ranked_users.json')

# Calculate users similarity
users_df = pd.read_csv(filepath, index_col = 0)
users_distance = scipy.spatial.distance.cdist(users_df, users_df, metric='jaccard')

distance_df = pd.DataFrame(users_distance, index=users_df.index.values,
						columns=users_df.index.values)


# Rank the users

user_rankings = {}

for user in distance_df.columns:
	distance = distance_df[user].nsmallest(3)
	data = {user: [i for i in distance.index if i!=user]}
	user_rankings.update(data)
	
with open(file_dst, 'w') as f:
	json.dump(user_rankings, f, indent = 4)
