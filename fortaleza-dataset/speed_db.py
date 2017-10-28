import psycopg2
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

def access(dbname, user, edge_id, week_day):
    conn = psycopg2.connect("dbname="+dbname+" user="+user)
    curs = conn.cursor()
    curs.execute("SELECT * FROM public.speed_observations_june where avg_speed_ms < 100 and edge_id_gh="+edge_id+" and day_of_week="+week_day+" order by edge_id_gh")
    x= curs.fetchall()
    df = pd.DataFrame(x, columns=['traj_id','edge','date','speed','week_day'])
    return df

def access_hour(dbname, user, edge_id, week_day, min_hour, max_hour):
    conn = psycopg2.connect("dbname="+dbname+" user="+user)
    curs = conn.cursor()
    curs.execute("SELECT * FROM public.speed_observations_june where avg_speed_ms < 100 and edge_id_gh="+edge_id+" and day_of_week="+week_day+" and date_part('hour' , start_time) <"+max_hour+" and date_part('hour' , start_time)>="+min_hour+" order by edge_id_gh")
    x= curs.fetchall()
    df = pd.DataFrame(x, columns=['traj_id','edge','date','speed','week_day'])
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
    
   





