import psycopg2
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

def access(dbname, user, edge_id):
    conn = psycopg2.connect("dbname="+dbname+" user="+user)
    curs = conn.cursor()
    curs.execute("SELECT * FROM public.speed_observations where avg_speed_ms < 100 and edge_id_gh="+edge_id+" order by edge_id_gh")
    x= curs.fetchall()
    df = pd.DataFrame(x, columns=['edge','date','speed','from','to'])
    return df


def plot_pdf(speed_df):
    mean = np.mean(speed_df.speed)
    std = np.std(speed_df.speed)
    r = speed_df.speed
    norm.pdf(r.unique(), loc=mean, scale=std)
    count, bins, ignored = plt.hist(r, normed=True, bins=100)
    plt.show()
    plt.plot(bins, norm.pdf(bins, loc=mean, scale=std), 'r-', alpha=0.6, label='norm pdf')
    plt.show()
    
    
def plot_pdf2(mean, std, bins):
    plt.plot(bins, norm.pdf(bins, loc=mean, scale=std), alpha=0.6, label='norm pdf')
    plt.show()
    
   





