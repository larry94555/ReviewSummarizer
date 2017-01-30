import json
import time

json_file = "/mnt/c/machine-learning/ReviewSummarizer/data/yelp_academic_dataset_review.json"

def time_passed(start_time):
    return time.time() - start_time

num=0
start_time = time.time()
with open(json_file) as f:
    for line in f:
        data = json.loads(line)
        #reviews = pd.DataFrame(list(data))
        num += 1
        if num % 100000 == 0:
            print "num = ",num,time_passed(start_time)
            #print len(reviews)
            #print data['text']

print "duration:",time_passed(start_time)



