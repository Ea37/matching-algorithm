import random
import uuid
import csv
import os


TAGS = ['music', 'songs', 'movies', 'dance', 'food', 'sports', 'gaming']
DATASET_NAME = 'users.csv'
DATASET_DIR = './dataset'
MAX_INTRESTS = len(TAGS)


def generate_intrests(count):
	intrests = random.choices(TAGS, k = count)
	return list(set(intrests))
	
		
def create_users(count = 1000, max_intrests = 6):
	users = []
	user = {}
	
	for i in range(count):
		intrests_count = random.randint(0, max_intrests)
		user['id'] = 'User_' + str(i+1)
		user['intrests'] = generate_intrests(intrests_count)
		users.append(user.copy())
		
	return users

	
def create_dataset(data, filename = DATASET_NAME):
	file_path = os.path.join(DATASET_DIR, filename)
	with open(file_path, 'w', newline = '') as f:
		dataset = csv.writer(f, dialect = 'excel', quotechar = '|', delimiter = ',', 
							quoting = csv.QUOTE_MINIMAL)
		headers = TAGS.copy()
		headers.insert(0, 'user_id')
		dataset.writerow(headers)
		
		for user in data:
			row = [0] * len(TAGS)
			row.insert(0, user['id'])
			for intrest in user['intrests']:
				try:
					index = TAGS.index(intrest)
					row[index+1] = 1
				except ValueError:
					pass
			dataset.writerow(row)
		

if __name__ == '__main__':
	users = create_users()
	create_dataset(users)
		
