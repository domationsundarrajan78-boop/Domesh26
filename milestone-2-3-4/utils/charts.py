import pandas as pd
import matplotlib.pyplot as plt

def service_chart(logs):
    df = pd.DataFrame(logs)
    counts = df["service"].value_counts()

    fig, ax = plt.subplots()
    counts.plot(kind="bar", ax=ax)
    return fig


def level_chart(logs):
    df = pd.DataFrame(logs)
    counts = df["level"].value_counts()

    fig, ax = plt.subplots()
    counts.plot(kind="pie", autopct='%1.1f%%', ax=ax)
    return fig