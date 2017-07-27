import psycopg2
import pandas as pd

def access(dbname, user, edge_id):
    conn = psycopg2.connect("dbname="+dbname+" user="+user)
    curs = conn.cursor()
    curs.execute("SELECT * FROM public.speed_observations where avg_speed_ms < 100 and edge_id_gh="+edge_id+" order by edge_id_gh")
    x= curs.fetchall()
    df = pd.DataFrame(x, columns=['edge','date','speed','from','to'])
    return df




