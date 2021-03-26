import os
import json


def get_regions(path):
    fp = open(path)
    regions = json.load(fp)
    return regions
