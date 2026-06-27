import pandas as pd
import random

response_df = pd.read_csv("dataset/lucy_responses.csv")

response_df["emotion"] = response_df["emotion"].str.lower()
response_df["language"] = response_df["language"].str.lower()

def get_response(emotion , language) :
    filtered = response_df[
        (response_df["emotion"] == emotion) & 
        (response_df["language"] == language)
    ]

    if filtered.empty :
        return (
            "I am here for you",
            "Would you like to tell me more ?"
            )

    row = filtered.sample(1).iloc[0]

    return (
        row["response"],
        row["follow_up"],
    )   
