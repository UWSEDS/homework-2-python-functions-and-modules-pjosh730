import pandas as pd
import numpy as np

df = pd.read_csv("https://inventory.data.gov/dataset/8bf56e54-1a05-4726-9c20-cfd22a20c48d/resource/474b78a0-37c2-4d79-877f-05025428ae57/download/userssharedsdfpromiseneighborhoods2011applications.csv")

def test_create_dataframe (frame, columes):
    if set(frame.columns)!= set(columes):
        print('False, columns do not fit')
        return
    if len(set(frame.dtypes))>=2:
        print('False, more than 1 type')
        return
    if frame.shape[0]<10:
        print('False, row less then 10')
        return
    print('True')
    return
