import pandas as pd

df_figaro=pd.read_csv("outputs/figaro_df.csv")
df_figaro["source"]="Le figaro"
df_gorafi=pd.read_csv("outputs/gorafi_df.csv")
df_gorafi["source"]="Le gorafi"
df_monde=pd.read_csv("outputs/monde_df.csv")
df_monde["source"]="Le monde"
df_canard=pd.read_csv("outputs/canard_df.csv")
df_canard["source"]="Le canard enchainé"

#print(df_figaro.head())
df_news_fin=pd.concat([df_monde,df_canard,df_figaro,df_gorafi],join="inner",ignore_index="True")
df_news_fin.to_csv("outputs/df_news.csv")
