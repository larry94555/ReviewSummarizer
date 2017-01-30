from collections import defaultdict
import json
import pandas as pd
import time

business_json_file = "/mnt/c/machine-learning/ReviewSummarizer/data/yelp_academic_dataset_business.json"
review_json_file = "/mnt/c/machine-learning/ReviewSummarizer/data/yelp_academic_dataset_review.json"

def time_passed(start_time):
    return time.time() - start_time

tally = defaultdict(int)

def parse_data(businesses,review_data):
    categories = businesses[review_data['business_id']]['categories']
    if categories is not None:
        for category in businesses[review_data['business_id']]['categories']:
            tally[category] += 1
    #print review_data
    #print businesses[review_data['business_id']]
    #if 1 == 2:
    #    print "Should not happen"

start_time = time.time()

num=0
businesses = {}

with open(business_json_file) as f:
    for line in f:
        data = json.loads(line)
        businesses[data['business_id']] = data


with open(review_json_file) as f:
    for line in f:
        data = json.loads(line)
        business_id=data['business_id']
        #print data['text']
        parse_data(businesses,data)

#print tally
for key,value in sorted(tally.items()):
    print (key,value)

print "duration:",time_passed(start_time)



