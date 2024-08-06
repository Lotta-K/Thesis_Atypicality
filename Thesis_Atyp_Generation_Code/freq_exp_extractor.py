import os
import pandas as pd
import glob
import re
from nltk.tag import StanfordPOSTagger
from nltk import pos_tag, word_tokenize

def build_pandas(path):
    print("entered")
    dfs = []
    for filename in os.listdir(path):
        if "probing" not in filename and "messages" not in filename and "likert" not in filename:
            print(filename)
            df= pd.read_csv(os.path.join(path, filename), usecols=['model', "setting", "prompt_method","A_clean", "Q", 'R'], encoding = "latin1")
            dfs.append(df)
    print("ABOUT TO CONCAT")
    result = pd.concat(dfs, ignore_index=True)
    return result


def tagger():
    st = StanfordPOSTagger('"C:\\Users\\charl\\Downloads\\stanford-tagger-4.2.0\\stanford-postagger-full-2020-11-17\\stanford-postagger-4.2.0.jar"')
    return st

def tag(sent):
    result = pos_tag(word_tokenize(sent))
    return result


freq_words = ["usually", "sometimes", "more often than not", "almost always", "almost every time",  "often", "frequently", "never", "always", "rarely", "seldom", "generally", "hardly ever", "occasionally", "normally", "every time", "typically"]
neg_words = ["not", "don't", "doesn't", "won't", "wouldn't"]


def find_things(message):
    print("in Find things")
    freq = None
    neg = None
    collect = []
    collecting = True
    #sentences = re.split(r'.|,', str(message))
    message = str(message).replace(",", ".")
    sentences = str(message).split(".")
    #print(sentences)
    sentences.reverse()
    for sentence in sentences:
        if "if" not in sentence:
            for word in freq_words:
                if word in sentence:
                    freq = word
                    for thing in neg_words:
                        if thing in sentence:
                            neg = thing
                            collect.append((freq, neg))
                            collecting = False
                    if collecting == True:
                        collect.append([freq, neg])
                if len(collect) > 0:
                    freq = None
                    neg = None
                    break
        if len(collect) > 0:
            freq = None
            neg = None
            break
    if len(collect) > 0:
        save = True
    else:
        save = False
    return save, collect

def find_things2(message):
    print("in Find things")
    freq = None
    neg = None
    collect = []
    collecting = True
    #sentences = re.split(r'.|,', str(message))
    message = str(message).replace(",", ".")
    sentences = str(message).split(".")
    #print(sentences)
    #sentences.reverse()
    for sentence in sentences:
        if "if" not in sentence:
            for word in freq_words:
                if word in sentence:
                    freq = word
                    for thing in neg_words:
                        if thing in sentence:
                            neg = thing
                            #collect.append((freq, neg))
                            #collecting = False
                    if collecting == True:
                        collect.append([freq, neg])
                #if len(collect) > 0:
                #    freq = None
                #    neg = None
                #    break
        #if len(collect) > 0:
        #    freq = None
        #    neg = None
         #   break
    if len(collect) > 0:
        save = True
    else:
        save = False
    return save, collect



def the_thing(df):
    new = pd.DataFrame(columns=["freq", "neg", "global_id", 'model', "prompt_method", "A_clean", "Q", 'R'])
    for index, row in df.iterrows():
        if (row["setting"] == 3 or row["setting"] == 5) and row["Q"] != 2:
            #print(row)
            message = row["R"]
            save, info = find_things2(message)
            if save:
                for thing in info:
                    temp = pd.DataFrame({"freq": thing[0], "neg": thing[1], "global_id": index, 'model': row["model"], "prompt_method":row["prompt_method"],"A_clean": row["A_clean"], "Q": row["Q"], 'R': row["R"]}, index=[index])
                    new = pd.concat([new, temp])
    return new


this = build_pandas("all_llama_for_f_new")
print(len(this))
#test = the_thing(this)
#test.to_csv("mixtral_by_freq_express_small.csv", index=True)
