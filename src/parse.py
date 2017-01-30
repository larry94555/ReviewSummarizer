import json

json_file = "/mnt/c/machine-learning/ReviewSummarizer/data/yelp_academic_dataset_review.json"

json_data = open(json_file)

data = json.load(json_data)

