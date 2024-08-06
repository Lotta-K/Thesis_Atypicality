import csv, os, glob
import numpy as np
import pandas as pd
import re


### Execute file in console
### print(data.X.unique()) to check if any wrong responders are left (replace manually
### save_csv(data)

def combine_csvs(folder):
    csv_files = [f for f in glob.glob(folder+"\\*.csv") if re.search(r'\W\d+.csv', f)]
    #csv_files = glob.glob(folder+"\\*.csv")

    df = pd.concat((pd.read_csv(filename, encoding="windows-1252") for filename in csv_files))
    df = df.reset_index(drop=True)
    #print(df.to_string())
    return df


def combine_message_csvs(folder):
    csv_files = [f for f in glob.glob(folder+"\\*.csv") if re.search(r'messages_\d+.csv', f)]
    df = pd.concat((pd.read_csv(filename, encoding="windows-1252") for filename in csv_files))
    df = df.reset_index(drop=True)
    #print(df.to_string())
    return df

def fix_questions(df: pd.DataFrame):
    q1 = []
    q2 = []
    with open("Clean_CSV_References/Q1.txt", 'r') as f:
        lines = list(f)
        q1 = " ".join(line.rstrip() for line in lines)
    with open("Clean_CSV_References/Q2.txt", 'r') as f:
        lines = list(f)
        q2 = " ".join(line.rstrip() for line in lines)



    df.Q = df.Q.apply(lambda x: "1" if str(x) in q1 else str(x))
    df.Q = df.Q.apply(lambda x: "1" if "Q1" in str(x) else str(x))
    df.Q = df.Q.apply(lambda x: "2" if str(x) in q2 else str(x))
    df.Q = df.Q.apply(lambda x: "2" if "Q2" in str(x) else str(x))


    with open("Clean_CSV_References/Q1_keywords.txt", 'r') as f:
        key_1 = list(f)
    with open("Clean_CSV_References/Q2_keywords.txt", "r") as f:
        key_2= list(f)
    counter = 0
    assholes = list(np.where((df["Q"] != "1") & (df["Q"] !="2")))
    #print(len(assholes[0]))
    for ass in assholes[0]:
        #print(ass)
        for item in key_1:
            #print(item)
            #print(df.iloc[ass]["Q"])
            if item.strip() in df.iloc[ass]["Q"]:
                counter +=1
                #print(counter)
                df.loc[ass, "Q"] = "1"
                #print(df.iloc[ass]["Q"])
                break

    for ass in assholes[0]:
        for item in key_2:
            if item.strip() in df.iloc[ass]["Q"]:
                counter +=1
                #print(counter)
                df.loc[ass, "Q"] = "2"
                #print(df.iloc[ass]["Q"])
                break
    #print(counter)
    #n_assholes = list(np.where((df["Q"] != "1") & (df["Q"] != "2")))
    #print(len(n_assholes[0]))
    return df

def fix_responders(df: pd.DataFrame):

    df.X = df.X.apply(lambda x: "AI" if "AI" in str(x) else str(x))
    df.X = df.X.apply(lambda x: "AI" if "You" in str(x) else str(x))
    df.X = df.X.apply(lambda x: "Human" if "Human" in str(x) else str(x))
    df.X = df.X.apply(lambda x: "Human" if "human" in str(x) else str(x))
    df.X = df.X.apply(lambda x: "Human" if "person" in str(x) else str(x))
    df.X = df.X.apply(lambda x: "Human" if "Person" in str(x) else str(x))
    df.X = df.X.apply(lambda x: "Human" if "someone" in str(x) else str(x))
    df.X = df.X.apply(lambda x: "Human" if "Someone" in str(x) else str(x))

    return df


def save_csv(df: pd.DataFrame, path = ""):
    filename = "clean_"+str(df.iloc[4]["run_ID"])+".csv"
    df.to_csv(path+filename, index=True)

def save_message_csv(df: pd.DataFrame, path = ""):
    filename = "messages"+str(df.iloc[4]["run_ID"])+".csv"
    df.to_csv(path+filename, index=True)



def convert_p(df: pd.DataFrame):
    df.failsafe = df.failsafe.str.extract(r'(\d+[.]?\d*)')
    df.rename(columns = {'failsafe':'P'}, inplace = True)
    # used to drop the first results in conv calib
    df.dropna(subset=["P"], inplace=True)

    return df


file_name = "Full_Runs/mixtral/2024-07-01_21-06_mixtral_t-0.6_calib_zero_shot_fr"
path = "clean_mixtral/"

data = combine_csvs(file_name)
data = fix_questions(data)
data = fix_responders(data)
data = convert_p(data)
print(data.X.unique())
print(data.Q.unique())
save_csv(data, path)
#message = combine_message_csvs(file_name)
#save_message_csv(message, path)
