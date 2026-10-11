"""Fit a per-station daily harmonic regression from historical observations."""
import math
def features(hour):
    return [1.0,math.sin(hour*math.pi/12),math.cos(hour*math.pi/12)]
def solve(matrix,vector):
    a=[list(row)+[vector[i]] for i,row in enumerate(matrix)]
    for col in range(3):
        pivot=max(range(col,3),key=lambda i:abs(a[i][col]))
        a[col],a[pivot]=a[pivot],a[col]
        scale=a[col][col]
        if abs(scale)<1e-10:raise ValueError("Training data cannot fit the daily model.")
        a[col]=[v/scale for v in a[col]]
        for row in range(3):
            if row!=col:
                multiple=a[row][col]
                a[row]=[v-multiple*w for v,w in zip(a[row],a[col])]
    return [row[-1] for row in a]
def fit(samples):
    x=[features(sample["hour"]) for sample in samples]
    y=[sample["count"] for sample in samples]
    matrix=[[sum(row[i]*row[j] for row in x)+(0.001 if i==j else 0) for j in range(3)] for i in range(3)]
    coefficients=solve(matrix,[sum(row[i]*value for row,value in zip(x,y)) for i in range(3)])
    residuals=[value-sum(a*b for a,b in zip(row,coefficients)) for row,value in zip(x,y)]
    rmse=math.sqrt(sum(v*v for v in residuals)/len(residuals))
    return {"coefficients":[round(v,8) for v in coefficients],"rmse":round(rmse,4),"scale":max(4.0,rmse),"samples":len(samples)}
def predict(model,hour):
    return max(0,sum(a*b for a,b in zip(features(hour),model["coefficients"])))
