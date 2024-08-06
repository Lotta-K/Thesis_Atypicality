import csv, re


def write_result(results:list, name:str, folder="Test_Results"):
    """
    writes the results returned by the model for a full stimulus set (6 requests/settings) to txt
    :param results: list of str
    :param name: str: name of the file/stimulus numbe
    :param folder: str: specify folder the txt should be saved FOLDER MUST EXIST
    :return: None
    this function writes the result fully as returned and the output functions as a backup in
    case write_result_csv returns illegible/incomplete results
    """

    with open(folder +"\\"+"backup_"+name+".txt", 'w', encoding="utf-8") as f:
        for result in results:
            f.write(f"\nBegin setting: {result[0]} \n")
            f.write(result[1])
            f.write(f"\nEnd setting: {result[0]} \n")
    print("A result has been noted in txt format.")


def write_result_csv(results:list, name:str, model:str, run_id: str, prompt_method: str, temperature: float, folder="Test_Results"):
    """
    writes the results returned by the model for a full stimulus set (6 requests/settings) to csv
    :param temperature:
    :param prompt_method:
    :param results: list of str
    :param name: str: name of the file/stimulus number
    :param model: str: model that was used to obtain results
    :param run_id: str: id assigned to each full run to keep entries identifiable
    :param folder: str: specify folder the txt should be saved FOLDER MUST EXIST
    :return: none
    after initial processing the function calls on dictionary_maker to get dictionaries
        that can be written into the csv file
    """
    with open(folder +"\\"+name+".csv", 'a') as f:
        fields = ["run_ID", "model", "prompt_method", "t", "stimulus", "setting", "X", "Q", "A", "A_clean", "R", "failsafe"] # fields used in scv file/respective possible dictionary keys
        entries = []    #list of dictionaries to be written to csv, empty, passed on o dictionary maker
        for result in results: # result is full output string for one setting
            setting = result[0]     # record what setting the answer is for
            items = result[1].splitlines()  # split into items
            #TODO think about below line - technically it do be true but maybe something can be done
            # I mean something was indeed done but is it a correct fix?
            #f(x) if condition else g(x) for x in sequence]
            items = [i for i in items if i.strip()]
            items = [i if (":" in i) else (str(i)+":") for i in items]
            #items = [i for i in items if ":" in i] # remove unuasable items
            #call on dictionary maker, returns list of entries
            entries, items = dictionary_maker(items, name, model, prompt_method, temperature, run_id, setting, fields, entries)
        #print(entries)
        writer = csv.DictWriter(f, fieldnames = fields)
        writer.writeheader()
        writer.writerows(entries)

    print("A result has been noted in csv format.")

def save_messages_csv(messages:list, name:str, model:str, run_id: str, folder: str):
    """
    writes the results returned by the model for a full stimulus set (6 requests/settings) to csv
    :param temperature:
    :param prompt_method:
    :param results: list of str
    :param name: str: name of the file/stimulus number
    :param model: str: model that was used to obtain results
    :param run_id: str: id assigned to each full run to keep entries identifiable
    :param folder: str: specify folder the txt should be saved FOLDER MUST EXIST
    :return: none
    after initial processing the function calls on dictionary_maker to get dictionaries
        that can be written into the csv file
    """
    with open(folder +"\\"+"messages_"+name+".csv", 'a') as f:
        fields = ["run_ID", "model", "stimulus", "setting", "role", "content"] # fields used in scv file/respective possible dictionary keys
        entries = []    #list of dictionaries to be written to csv, empty, passed on o dictionary maker
        for result in messages: # result is full output string for one setting
            setting = result[0]     # record what setting the answer is for
            items = result[1]  # split into items
            entries, items = message_dictionary_maker(items, name, model, run_id, setting, fields, entries)
            #entries, items = dictionary_maker(items, name, model, prompt_method, temperature, run_id, setting, fields, entries)
        #print(entries)
        writer = csv.DictWriter(f, fieldnames = fields)
        writer.writeheader()
        writer.writerows(entries)

    print("A result has been noted in csv format.")

def dictionary_maker(items: list, name:str, model:str, prompt_method:str, temperature:float, run_id: str,setting: int, fields: list, entries: list):
    """

    :param temperature:
    :param prompt_method:
    :param items: list of strings that are to be converted into entries of a dictionary
    :param name: name i.e number of the stimulus
    :param model: model that was used to obtain results
    :param run_id: unique id assigned to the run
    :param setting: setting (number) that is currently used
    :param fields: firled of the csv/dictionary keys
    :param entries: list of already existing entries the new ones can be appended to
    :return: remaining items and current list of entries
    """
    #print(f"ENTERED DICT MAKER WITH {items}")
    entry = {"run_ID": run_id, "model": model, "prompt_method": prompt_method,"stimulus": name, "setting": setting, "t":temperature}  # dictionary for this result
    alt_q_fields = ["Q1", "Q2"]  # most common alt_fields hardcoded for string replacement Q1->Q etc
    alt_a_fields = ["A1", "A2"]
    alt_r_fields = ["R1", "R2"]
    while items:
        item = items[0]  # the singular item "X: AI"
        #print(f"NOW LOOKING AT {item}")
        #MAYBE FIXED HIGHER UP IN THE INPUT CREATION: check if there is more than one ':' in string/slash make sure it is split at he correct one
        final = item.split(":", 1)  # split into "X" and "AI"
        clean_final = []  # clean trailing \n
        for word in final:
            word = word.strip()
            clean_final.append(word)
        #MAyYBE FIXED: via brute force :this causes AI assigment to human response quite frequently due to 3.5output that drops the second X:
        # maybe implement some counter method or something to make sure we get at most two responses each
        this_bitch =  clean_final[0]
        if clean_final[0] != "X" and "X" not in entry.keys() and (len(entries)%2!=0):
        #if clean_final[0] != "X" and "X" not in entry.keys() and (len(entries)==1 or len(entries)==3) : #covers cases where the output does not state X twice with a failsafe only
            old_x = entries[-1].get("X")                                    # to do it if there have been previous entries to draw from
            entry["X"] = old_x
            #print ("THE X THING WAS TRIGGERED")
            #print(entry)

        # perform common replacements
        if clean_final[0] in alt_q_fields:
            clean_final[1] = clean_final[0]     # move Q1/Q2 to value instead of key
            clean_final[0] = "Q"                # re-assign key
        elif clean_final[0] in alt_a_fields:
            clean_final[0] = "A"
        elif clean_final[0] in alt_r_fields:
            clean_final[0] = "R"

        if clean_final[0] not in fields:  # failsafe in case the model generated incorrctly formatted output that is not caugh tby the hardcoded alternatives
            if "failsafe" in entry.keys():  # failsafe in case that happened more than once
                temp = entry.get("failsafe")
                entry["failsafe"] = str(clean_final[0])+" // " + str(clean_final[1]) + ": " + temp
                #print(f"IN THE FAILSAFE; ENTRY LOOKS LIKE {entry}")
                del items[0]

            else:
                entry["failsafe"] = str(clean_final[0])+" // " + str(clean_final[1])
                del items[0]
        #TODO implement better check that it is actually and not just probably a new answer
        elif clean_final[0] in entry.keys():  # append entry and reset before adding bc it's probably a new answer
            #print("______ duplicate identified")
            #print (entry.keys())
            #print(clean_final[0])
            entries.append(entry)
            #print("JUST ADDED AN ENTRY:")
            #print(entry)
            #items, name, model, prompt_method, run_id, setting, fields, entries
            entries, items_new = dictionary_maker(items, name, model, prompt_method, temperature, run_id, setting, fields, entries )
            items = items_new

        else:
            #TODO Implement much better regex function for extracting number responses!!!
            if clean_final[0] == "A":
                #clean = re.sub("\D", "", clean_final[1])
                clean = clean_a(clean_final[1])
                entry["A_clean"] = clean
            entry[clean_final[0]] = clean_final[1]  # add to dict
            del items[0]
    if entry not in entries:    # make sure the final remaining entry was added
        entries.append(entry)

    return entries, items

def message_dictionary_maker(items: list, name:str, model:str, run_id: str,setting: int, fields: list, entries: list):
    """

    :param temperature:
    :param prompt_method:
    :param items: list of strings that are to be converted into entries of a dictionary
    :param name: name i.e number of the stimulus
    :param model: model that was used to obtain results
    :param run_id: unique id assigned to the run
    :param setting: setting (number) that is currently used
    :param fields: firled of the csv/dictionary keys
    :param entries: list of already existing entries the new ones can be appended to
    :return: remaining items and current list of entries
    """
    #print(f"ENTERED DICT MAKER WITH {items}")
    entry = {"run_ID": run_id, "model": model, "stimulus": name, "setting": setting}  # dictionary for this result  # most common alt_fields hardcoded for string replacement Q1->Q etc
    for item in items:
        entry["role"] = item["role"]
        entry["content"] = item["content"]
        entries.append(entry)
        entry = {"run_ID": run_id, "model": model, "stimulus": name, "setting": setting}

    return entries, items

def clean_a(a:str):
    #TODO this is not fully correct yet but I think it's close enough for now
    # basically "10, 20 or maybe 30" would return as 10 whichhhh not great
    if not bool(re.search("\d", a)):
        result = None
    else:
        # maybe I do still need a regex that get's all digits?? For now I ll keep it as such
        match = re.search("(((\d{1,3}%?\s?-\s?)?|(>|<)?)\d{1,3}%?)", a)
        if match:
            clean = match.group()
            clean = re.sub("%", "", clean)
            clean = re.sub("\s",  "", clean)
            #print(f"Clean is :{clean}")
            if "<" in clean or ">" in clean:
                #TODO implement handling? maybe +5 and -5
                clean = re.sub("<|>", "", clean)
                if clean.isdigit():
                    result = int(clean)
                else:
                    result = -1
            elif "-" in clean:
                parts = clean.split("-")
                if len(parts) == 2:     # uncessary? i don't think my regex allows it to be longer
                    if parts[0].isdigit() and parts[1].isdigit():
                        part1 = int(parts[0])
                        part2 = int(parts[1])
                        result = (part1+part2)/2
                    else:
                        result = -1
                else:
                    result = -1
            else:
                result = clean
        else:
            result = -1

    return result



#### Deprecated Functions
def deprecated_write_result_csv(results:list, name:str, model:str, run_id: str, folder="Test_Results"):

    """ deprecated csv writer to be deleted eventually
    (But I'm currently afraid I might need it for some reason)
    """
    with open(folder +"\\"+name+".csv", 'w') as f:
        fields = ["run_ID", "model", "stimulus", "setting", "X", "Q", "A", "R", "failsafe"] # fields we use
        alt_q_fields = ["Q1", "Q2"]     # most common alt_fields hardcoded for string replacement Q1->Q etc
        alt_a_fields = ["A1", "A2"]
        alt_r_fields = ["R1", "R2"]
        entries = []    #list of dictionaries to be written to csv
        for result in results: # result is full output string for one setting
            setting = results.index(result)+1     # record what setting the answer is for
            sub_res = result.split('\n\n') # list of full responses "X:AI; Q: ..."
            for thing in sub_res:
                entry = {"run_ID": run_id, "model": model, "stimulus": name,"setting": setting}  # dictionary for this result
                items = thing.strip().split(";")    #split into items
                items = [i for i in items if i] #remove empty items
                for item in items:  #the singular item "X: AI"
                    final = item.split(":", 1)  #split into "X" and "AI"
                    clean_final=[]  # clean trailing \n
                    for word in final:
                        while "\n" in word:
                            word = word.replace("\n", "")
                        clean_final.append(word)

                    if clean_final[0] in alt_q_fields:  # perform common replacements
                        clean_final[0]="Q"
                    elif clean_final[0] in alt_a_fields:
                        clean_final[0] = "A"
                    elif clean_final[0] in alt_r_fields:
                        clean_final[0] = "R"

                    if clean_final[0] not in fields:  # failsafe in case the model generated incorrctly formatted output that is not caugh tby the hardcoded alternatives
                        if "failsafe" in entry.keys(): # failsafe in case that happened more than once
                            temp = entry.get("failsafe")
                            entry["failsafe"] = clean_final[1]+": "+temp
                        else:
                            entry["failsafe"]=clean_final[1]
                    elif clean_final[0] in entry.keys(): # append entry and reset before adding bc it's probably a new answer
                        entries.append(entry)
                        entry = {"run_ID": run_id, "model": model, "stimulus": name,"setting": setting}
                        entry[clean_final[0]] = clean_final[1]
                    else:
                        entry[clean_final[0]]= clean_final[1]   # add to dict

                entries.append(entry)   #add dict to list
        writer = csv.DictWriter(f, fieldnames = fields)
        writer.writeheader()
        writer.writerows(entries)

    print("A result has been noted.")