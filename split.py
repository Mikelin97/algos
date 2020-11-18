import pandas as pd
import numpy as np


# def split(df, column, chunk):
#     df = df.reset_index(drop=True)
#     tem = df[column].unique()
#     res = np.array_split(tem, chunk)
#     results = []
#
#     for r in res:
#         start_pos = r[0]
#         end_pos = r[-1]
#
#         start = df[df['CARDNO2'] == start_pos].index[0]
#         end = df[df['CARDNO2'] == end_pos].index[-1] + 1
#
#         result = df[start:end]
#         result = result.reset_index(drop=True)
#         results.append(result)
#     return results



def split_two(df, column):
    df = df.reset_index(drop = True)
    tem = df[column].unique()
    res = np.array_split(tem, 2)

    end1_pos = res[0][-1]
    end = df[df[column] == end1_pos].index[-1] + 1

    results = [df[:end].reset_index(drop=True), df[end:].reset_index(drop=True)]
    return results



def split_dp(df, column, chunk):
    if chunk == 2:
        return split_two(df, column)
    else:
        res = split_dp(df, column, chunk // 2)
        results = []
        for r in res:
            result = split_two(r, column)
            results.extend(result)
        return results
