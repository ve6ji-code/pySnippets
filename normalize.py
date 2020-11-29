#!/usr/bin/python3
# Normalize a list of data
# Xnorm = (Xi - Xmin)/(Xmax -Xmin)

xData = [1, 2, 3, 4, 5]  # Your Data List


def normData(xData):
    normalized = []
    Xmax = max(xData)
    Xmin = min(xData)
    for xi in xData:
      X = (xi - Xmin)/(Xmax - Xmin)
      normalized.append(X)
    return normalized

print(normData(xData))
