import os


def read_stimuli(exclude: list, settings: list, prompt_method: str, prompt: str, directory: str = 'Stimuli'):
    """

    :param settings:
    :param prompt_method:
    :param exclude:
    :param directory:
    :return:

    """

    stimuli: list[list[str,list[str]]] = []
    #stimuli: dict = {}

    for folder in os.listdir(directory):
        name = folder
        if name not in exclude:
            stimulus_set = read_stimuli_set_from_file(directory, folder, prompt_method, settings, prompt)
            stimuli.append([name, stimulus_set])

    return stimuli


context_prefix = "C:"

probing2 = "The second sentence in the direct speech conveys seemingly redundant information. Providing redundant information can be unnecessary and inefficient for communication. However, the speaker made the effort of conveying this information. Since they have no reason to be inefficient, this information must actually be new or important. What new or relevant information can you infer from the second sentence?"

def read_stimuli_set_from_file(directory, folder, prompt_method, settings, prompt):
    """

    :param settings:
    :param prompt_method:
    :param directory:
    :param folder:
    :return:

    order:
    1: ordinary + story
    2: wonky + story
    3: ordinary + story + intro + habitual
    4: wonky + story + intro + habitual
    5: ordinary + story + intro + non_habitual
    6: wonky + story + intro + non_habitual
     append to all
    """
    #stimuli: list[str] = []

    for filename in os.listdir(directory + "\\" + folder):
        if str(filename) == "habitual.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                habitual = f.read()
                habitual = habitual.strip()
        elif str(filename) == "intro.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                intro = f.read()
                intro = intro.strip()
        elif str(filename) == "non_habitual.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                non_habitual = f.read()
                non_habitual = non_habitual.strip()
        elif str(filename) == "ordinary.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                ordinary = f.read()
                ordinary = ordinary.strip()
        elif str(filename) == "story.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                story = f.read()
                story = story.strip()
        elif str(filename) == "wonky.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                wonky = f.read()
                wonky = wonky.strip()
        elif str(filename) == "question.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                question = f.read()
                question = question.strip()
        elif str(filename) == "question_probe.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                qs = list(f)
                question_probe_1 = qs[0].strip()
                question_probe_2 = qs[1].strip()
        elif str(filename) == "knowledge_generation.txt":
            with open(os.path.join(directory, folder, filename)) as f:
                know_gen = f.read()
                know_gen = know_gen.strip()
        else:
            raise FileExistsError


    if prompt_method == "probing":
        stimuli: list[list[str]] = []

        with open("probing/appendix_probing_Qs.txt", "r") as f:
            qs = list(f)
        for q in qs:
            stimuli.append([str(q), f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{q}"])

    elif prompt_method == "base_few_shot":
        question = question.split("\n")[0]
        stimuli: list[list[str, str]] = []
        stimuli.append(["1", f"{context_prefix} {ordinary} {story}\n{question}"])
        #stimuli.append(["2", f"{context_prefix} {wonky} {story}\n{question}"])

    #TODO what the eff is this, why does it look different from the others??
    elif prompt_method == "probing2":
        #stimuli: list[list[str, [str, str]]] = ["prob2",[f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{probing2}", question]]
        stimuli: list[list[str]] = []

        stimuli.append(["prob2",[f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{probing2}", question]])

    elif prompt_method == "individual_probing":
        stimuli: list[list[str]] =[]

        stimuli.append(["probe1", f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{question_probe_1}"])
        stimuli.append(["probe2", f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{question_probe_2}"])
    #TODO either no longer include 5 and 6 or include the optional choice as in else
    elif prompt_method == "few_shot":
        question = question.split("\n")[0]
        stimuli: list[list[str]] = []
        stimuli.append(["3", f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{question}"])
        #stimuli.append(["4", f"{context_prefix} {wonky} {story} {intro} {habitual}\n{question}"])
        stimuli.append(["5", f"{context_prefix} {ordinary} {story} {intro} {non_habitual}\n{question}"])
        #stimuli.append(["6", f"{context_prefix} {wonky} {story} {intro} {non_habitual}\n{question}"])
    elif prompt_method == "calib_zero_shot":
        question = question.split("\n")[0]
        stimuli: list[list[str]] = []
        stimuli.append(["1", f"{context_prefix} {ordinary} {story}\n{question}"])
        stimuli.append(["3", f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{question}"])
        #stimuli.append(["5", f"{context_prefix} {ordinary} {story} {intro} {non_habitual}\n{question}"])

    elif prompt_method == "calib_conv":
        question = question.split("\n")[0]
        stimuli: list[list[str]] = []
        stimuli.append(["1", f"{context_prefix} {ordinary} {story}\n{question}"])
        stimuli.append(["3", f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{question}"])
        #stimuli.append(["5", f"{context_prefix} {ordinary} {story} {intro} {non_habitual}\n{question}"])

    elif prompt_method == "conversation" and prompt == "know_gen":
        question = question.split("\n")[0]
        stimuli: list[list[str]] = []
        stimuli.append(["1", f"{context_prefix} {ordinary} {story}", f"{question}", know_gen])
        stimuli.append(["3", f"{context_prefix} {ordinary} {story} {intro} {habitual}", f"{question}", know_gen])
        stimuli.append(["5", f"{context_prefix} {ordinary} {story} {intro} {non_habitual}", f"{question}", know_gen])


    elif prompt_method == "conversation":
        question = question.split("\n")[0]
        stimuli: list[list[str]] = []
        stimuli.append(["3", f"{context_prefix} {ordinary} {story} {intro} {habitual}", f"{question}", know_gen])
        #stimuli.append(["5", f"{context_prefix} {ordinary} {story} {intro} {non_habitual}", f"\n{question}", know_gen])


    else:
        stimuli: list[list[str]] = []
        if 1 in settings:
            stimuli.append(["1", f"{context_prefix} {ordinary} {story}\n{question}"])
        if 2 in settings:
            stimuli.append(["2", f"{context_prefix} {wonky} {story}\n{question}"])
        if 3 in settings:
            stimuli.append(["3", f"{context_prefix} {ordinary} {story} {intro} {habitual}\n{question}"])
        if 4 in settings:
            stimuli.append(["4", f"{context_prefix} {wonky} {story} {intro} {habitual}\n{question}"])
        if 5 in settings:
            stimuli.append(["5", f"{context_prefix} {ordinary} {story} {intro} {non_habitual}\n{question}"])
        if 6 in settings:
            stimuli.append(["6", f"{context_prefix} {wonky} {story} {intro} {non_habitual}\n{question}"])

    return stimuli
