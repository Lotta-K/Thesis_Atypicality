import os
#helper functions

def load_text(filename):
    text = ""
    with open(filename, "r", encoding='cp1252') as f:
        lines = list(f)
        for line in lines:
            text += line

    return text

def load_Q1(filename):
    with open(filename, "r") as f:
        question = f.read()
        question = question.strip()
        question = question.split("\n")[0]

    return question


#fs_prompt_directory = "Few_Shot_Prompts_1303_misleading_zero" --> set in main

## different prompts

def zero_shot_prompt(prompt, system):# prompt = prompt1_b_zero_shot):
    if system:
        return [{"role": "system", "content": prompt}]

    return [{"role": "user", "content": prompt}]


#TODO literally anything to make this code less awful
def few_shot_prompt(
        few_shot_version: str,
        prompt: str, #3b_few-shot
        fs_prompt_directory: str
):
    system = prompt


    # load two stimuli in control condiion if we do crit/non_crit few shot
    if fs_prompt_directory == "Few_Shot_Prompts_1303_not_all_crit":
        few_shot_stim1 = ("C: " + load_text("Stimuli/1/ordinary.txt").strip() + " " + load_text(
            "Stimuli/1/story.txt").strip() + " "
                            + load_text("Stimuli/1/intro.txt").strip() + " " + load_text(
                    "Stimuli/1/non_habitual.txt").strip() + "\n" + load_Q1("Stimuli/1/question.txt"))

        few_shot_stim3 = ("C: " + load_text("Stimuli/3/ordinary.txt").strip() + " " + load_text(
            "Stimuli/3/story.txt").strip() + " "
                            + load_text("Stimuli/3/intro.txt").strip() + " " + load_text(
                    "Stimuli/3/non_habitual.txt").strip() + "\n" + load_Q1("Stimuli/3/question.txt"))

    # for everything else load them normally
    else:
        few_shot_stim1 = ("C: " + load_text("Stimuli/1/ordinary.txt").strip() +" " + load_text("Stimuli/1/story.txt").strip() +" "
                          + load_text("Stimuli/1/intro.txt").strip() + " " + load_text("Stimuli/1/habitual.txt").strip() + "\n" + load_Q1("Stimuli/1/question.txt"))

        few_shot_stim3 = ("C: " + load_text("Stimuli/3/ordinary.txt").strip() +" " + load_text("Stimuli/3/story.txt").strip() +" "
                          + load_text("Stimuli/3/intro.txt").strip() + " " + load_text("Stimuli/3/habitual.txt").strip() + "\n" + load_Q1("Stimuli/3/question.txt"))

    # load responses for these first two
    # AND DON'T PANIC ABOUT THE NAME
    # it says WithIR but they are correctly adjusted in the respective directory, you just named them poorly
    few_shot_res1 = load_text(fs_prompt_directory + "/few_shot_stim1_WithIR_response.txt")
    few_shot_res3 = load_text(fs_prompt_directory + "/few_shot_stim3_WithIR_response.txt")

    #load others normally with the response
    few_shot_stim6 = ("C: " + load_text("Stimuli/6/ordinary.txt").strip() + " " + load_text(
        "Stimuli/6/story.txt").strip() + " " + load_text("Stimuli/6/intro.txt").strip() + " " + load_text(
                "Stimuli/6/habitual.txt").strip() + "\n" + load_Q1("Stimuli/6/question.txt"))
    few_shot_res6 = load_text(fs_prompt_directory + "/few_shot_stim6_WithIR_response.txt")

    few_shot_stim10 = ("C: " + load_text("Stimuli/10/ordinary.txt").strip() + " " + load_text(
        "Stimuli/10/story.txt").strip() + " " + load_text("Stimuli/10/intro.txt").strip() + " " + load_text(
                "Stimuli/10/habitual.txt").strip() + "\n" + load_Q1("Stimuli/10/question.txt"))
    few_shot_res10 = load_text(fs_prompt_directory + "/few_shot_stim10_WithIR_response.txt")

    # select according to the few shot version you want
    if few_shot_version == "Low":
        # Low
        user = "Ex1: " + few_shot_stim3 + few_shot_res3 + "\nEx2: " + few_shot_stim10 + few_shot_res10 + "\n"

    elif few_shot_version == "Mix":
        #Mix
        user = "Ex1: "+ few_shot_stim1 + few_shot_res1 + "\nEx2: " + few_shot_stim10 + few_shot_res10 + "\n"

    elif few_shot_version == "Opposite mix":
        # Opposite mix
        user = "Ex1: "+ few_shot_stim3 + few_shot_res3 + "\nEx2: " + few_shot_stim6 + few_shot_res6 + "\n"

    elif few_shot_version == "High":
        #High
        user = "Ex1: " + few_shot_stim1 + few_shot_res1 + "\nEx2: " + few_shot_stim6 + few_shot_res6 + "\n"

    else:
        raise Exception("Few shot version must be specified")

    prompts = [{"role": "system", "content": system}, {"role": "user", "content": user}]

    return prompts


def baseline_few_shot_prompt(few_shot_version: str, prompt: str, fs_prompt_directory: str):
    system = prompt

    few_shot_stim1 = ("C: " + load_text("Stimuli/1/ordinary.txt").strip() +" " + load_text("Stimuli/1/story.txt").strip() + "\n" + load_Q1("Stimuli/1/question.txt"))
    few_shot_res1 = load_text(fs_prompt_directory + "/few_shot_stim1_baseline_response.txt")

    few_shot_stim3 = ("C: " + load_text("Stimuli/3/ordinary.txt").strip() +" " + load_text("Stimuli/3/story.txt").strip() + "\n" + load_Q1("Stimuli/3/question.txt"))
    few_shot_res3 = load_text(fs_prompt_directory + "/few_shot_stim3_baseline_response.txt")

    few_shot_stim6 = ("C: " + load_text("Stimuli/6/ordinary.txt").strip() + " " + load_text(
        "Stimuli/6/story.txt").strip() + "\n" + load_Q1("Stimuli/6/question.txt"))
    few_shot_res6 = load_text(fs_prompt_directory + "/few_shot_stim6_baseline_response.txt")

    few_shot_stim10 = ("C: " + load_text("Stimuli/10/ordinary.txt").strip() + " " + load_text(
        "Stimuli/10/story.txt").strip() + "\n" + load_Q1("Stimuli/10/question.txt"))
    few_shot_res10 = load_text(fs_prompt_directory + "/few_shot_stim10_baseline_response.txt")


    if few_shot_version == "Low":
        # Low
        user = "Ex1: " + few_shot_stim3 + few_shot_res3 + "\nEx2: " + few_shot_stim10 + few_shot_res10 + "\n"

    elif few_shot_version == "Mix":
        # Mix
        user = "Ex1: " + few_shot_stim1 + few_shot_res1 + "\nEx2: " + few_shot_stim10 + few_shot_res10 + "\n"

    elif few_shot_version == "Opposite mix":
        # Opposite mix
        user = "Ex1: " + few_shot_stim3 + few_shot_res3 + "\nEx2: " + few_shot_stim6 + few_shot_res6 + "\n"

    elif few_shot_version == "High":
        # High
        user = "Ex1: " + few_shot_stim1 + few_shot_res1 + "\nEx2: " + few_shot_stim6 + few_shot_res6 + "\n"

    prompts = [{"role": "system", "content": system}, {"role": "user", "content": user}]

    return prompts


def cot_prompt(prompt):
    system = prompt
    few_shot_stim1 = ("C: " + load_text("Stimuli/1/ordinary.txt").strip() +" " + load_text("Stimuli/1/story.txt").strip() +" "
                      + load_text("Stimuli/1/intro.txt").strip() + " " + load_text("Stimuli/1/habitual.txt").strip() + "\n" + load_text("Stimuli/1/question.txt"))
    few_shot_res1 = load_text("Prompts/cot_stim1_WithIR_response.txt")

    few_shot_stim3 = ("C: " + load_text("Stimuli/10/ordinary.txt").strip() +" " + load_text("Stimuli/10/story.txt").strip() +" "
                      + load_text("Stimuli/10/intro.txt").strip() + " " + load_text("Stimuli/10/habitual.txt").strip() + "\n" + load_text("Stimuli/10/question.txt"))
    few_shot_res3 = load_text("Prompts/cot_stim10_WithIR_response.txt")

    user = "Ex1: "+ few_shot_stim1 + few_shot_res1 + "\nEx2: " + few_shot_stim3 + few_shot_res3
    prompts = [{"role": "system", "content": system}, {"role": "user", "content": user}]

    return prompts


def conversation_prompt_generic(
        prompt:str,
        fs_prompt_directory: str):

    prompts = [{"role": "system", "content": prompt}]

    # name files alphabetically
    # one must contain only STIMULUS if stimulus insertion is needed
    # QUESTION if the original question is wanted
    names = os.listdir(fs_prompt_directory)
    sorted_names = sorted(names)
    for filename in sorted_names:
        with open(os.path.join(fs_prompt_directory, filename)) as f:
            text = f.read()
            #prompts.append({"role": "user", "content": text})
            prompts.append(text)

    return prompts




