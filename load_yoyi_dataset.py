
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#str_file = "/media/onetbssd/bidding_simulator/yoyi/train_set_example.txt"
str_file = "/media/onetbssd/bidding_simulator/yoyi/train_set"

map_features = {}
map_market_price = {}
count = 0
with open(str_file, 'r') as f:
    for line in f:
        count += 1
        tokens = line.split("\t")
        if tokens[1] in map_market_price:
            map_market_price[tokens[1]] += 1
        else:
            map_market_price[tokens[1]] = 1

        for i in range(2, len(tokens)):
            tok_and_count = tokens[i]
            feature_id = tok_and_count.split(":")[0]
            if tokens[i] in map_features:
                map_features[tokens[i]] += 1
            else:
                map_features[tokens[i]] = 1

# Print results
def print_map_stats(name_of_map, map):
    print("MAP: " + name_of_map)
    print("\tNum keys: " + str(len(list(map.keys()))))

print_map_stats("map_features", map_features)
print_map_stats("map_market_price", map_market_price)
print("number of lines is : " + str(count))