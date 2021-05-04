#!/usr/bin/env python3
""" NOSQL aggregation framework examples """


def top_students(mongo_collection):
    """ get average and sort the results """
  
    sorted_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return sorted_students