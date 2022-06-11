from fileinput import filename
import pandas as pd 
import matplotlib.pyplot as plt

filename=["large_forward.csv"]
for i in filename:
    df = pd.read_csv(i, sep=";")
    # print(df.columns)
    plot=df.plot(x ='Features', y='Accuracy', kind = 'line')
    fig = plot.get_figure()
    fig.savefig(i.split(".")[0]+".png")