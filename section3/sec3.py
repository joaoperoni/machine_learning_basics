import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('section3/credit_data.csv')

def database():
    print(base_credit.head())
    print(base_credit.describe())
    print(base_credit[base_credit['income']>=69995.685578])
    print(base_credit[base_credit['loan']<=1.377630])

def visualize():
    print(np.unique(base_credit['default'],return_counts=True))
    # sns.countplot(x=base_credit['default'])
    # sns.histplot(x=base_credit['age'])
    # plt.hist(x=base_credit['income'])
    # sns.histplot(x=base_credit['loan'])

    grafico = px.scatter_matrix(base_credit,dimensions=['age','income','loan'],color='default')
    grafico.show()

if __name__=="__main__":
    visualize()

