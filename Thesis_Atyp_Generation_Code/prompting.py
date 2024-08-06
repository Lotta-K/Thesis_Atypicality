import copy
import os
import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

import ollama_test
import prompt_building, result_writer
import all_prompts


# Load your API key from an environment variable or secret management service
def set_api_key():
    """ get and set API key"""
    openai.api_key = os.getenv("OPENAI_API_KEY")

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def run_chat_completion(prompts: list, stimulus: str, assistant: bool, temperature:int, prompt_method: str ="zero_shot", model="gpt-3.5-turbo"):
    """

    :param temperature:
    :param prompts:
    :param stimulus:
    :param assistant:
    :param prompt_method:
    :param model:
    :return:
    """

    if prompt_method == "few_shot" and assistant:
        messages = prompts.append({"role": "user", "content": stimulus[1]})
    elif prompt_method == "few_shot":
        users = prompts.pop()
        temp = users["content"]
        new = temp + "\n" + stimulus[1]
        users["content"] = new
        messages = prompts.append(users)

    chat_completion = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature)
    return chat_completion.choices[0].message.content, messages

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def run_chat_completion_w_backoff(prompts: list, stimulus: str, temperature:int, model="gpt-3.5-turbo"):
    """
    send a request for chat completion to the openAI  server with only a user message
    :param temperature:
    :param stimulus:
    :param prompts:
    :param model: specify model to be used
    :return: result
    @retry: retry sending request if servers return an error
    """
    messages = copy.deepcopy(prompts)
    users = messages.pop()
    temp = users["content"]
    new = temp + "\n" + stimulus[1]
    users["content"] = new
    messages.append(users)

    chat_completion = openai.ChatCompletion.create(model=model, messages=messages, temperature = temperature )
    return chat_completion.choices[0].message.content, messages

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def run_chat_completion_w_backoff_and_system(prompts: list, stimulus: str, temperature:int, model="gpt-3.5-turbo"):
    """
    send a request for chat completion to the openAI  server with a system/assistant message and a user prompt
    :param temperature:
    :param prompts:
    :param prompt: system/assistant prompt
    :param stimulus: user message
    :param model: specify model to be used
    :return: result
    @retry: retry sending request if servers return an error
    """
    messages = copy.deepcopy(prompts)
    messages.append({"role": "user", "content": stimulus[1]})

    chat_completion = openai.ChatCompletion.create(model=model, messages=messages, temperature = temperature)
    return chat_completion.choices[0].message.content.encode("utf-8").decode(), messages

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def run_chat_completion_w_backoff_and_system_and_few_shot(prompts: list, stimulus: str, temperature:int, model: str):
    """
    send a request for chat completion to the openAI  server with a system/assistant message and a user prompt
    :param temperature:
    :param assistant:
    :param prompts:
    :param stimulus: user message
    :param model: specify model to be used
    :return: result
    @retry: retry sending request if servers return an error
    """

    messages = copy.deepcopy(prompts)


    users = messages.pop()
    temp = users["content"]
    new = temp + "\n" + stimulus[1]
    users["content"] = new
    messages.append(users)


    chat_completion = openai.ChatCompletion.create(model=model, messages=messages, temperature = temperature)
    return chat_completion.choices[0].message.content, messages
#response.choices[0].message.content.encode("utf-8").decode()



@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def run_conversational_chat_completion_generic(prompts: list, stimulus: str, temperature: int, model="gpt-3.5-turbo"):

    cur_prompts = copy.deepcopy(prompts)
    messages = [cur_prompts[0]]

    for i in range(1,len(prompts)-1):
        cur_prompt = cur_prompts[i]

        cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[1]))
        cur_prompt = cur_prompt.replace("QUESTION", str(stimulus[2]))
        if len(stimulus)>3:
            cur_prompt = cur_prompt.replace("GENERATION", str(stimulus[3]))
        messages.append({"role": "user", "content": cur_prompt})


        completion = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature)
        completion_message = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": completion_message})
        i+=1

    cur_prompt = cur_prompts[-1]
    cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[1]))
    cur_prompt = cur_prompt.replace("QUESTION", str(stimulus[2]))
    if len(stimulus) > 3:
        cur_prompt = cur_prompt.replace("GENERATION", str(stimulus[3]))
    messages.append({"role": "user", "content": cur_prompt})

    #if "STIMULUS" in cur_prompt:
     #   cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[1]))
      #  messages.append({"role": "user", "content": cur_prompt})
    #if "QUESTION" in cur_prompt:
    #    cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[2]))
       # messages.append({"role": "user", "content": cur_prompt})
    #if "GENERATION" in cur_prompt:
      #  cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[3]))
     #   messages.append({"role": "user", "content": cur_prompt})
    #else:
    #    messages.append({"role": "user", "content": cur_prompt})

    completion = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature)
    #return completion.choices[0].message.content + "\n" + "<SPLIT>" + "\n" + str(messages)
    return completion.choices[0].message.content, messages



@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def run_conversational_chat_completion_calib(prompts: list, stimulus: str, temperature: int, model: str):

    messages = copy.deepcopy(prompts)
    messages.append({"role": "user", "content": stimulus[1]})

    first_completion = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature)

    first_completion_message = first_completion.choices[0].message.content

    messages.append({"role": "assistant", "content": first_completion_message})
    messages.append({"role": "user", "content": all_prompts.calibration_conversational_b})

    chat_completion = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature)
    #return first_completion.choices[0].message.content + "\n\n" + chat_completion.choices[0].message.content
    return chat_completion.choices[0].message.content, messages


#thats the old version needed for conversational probing
#keeping it around until I properly refactor that if ever
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def run_conversational_chat_completion_probe(prompts: list, stimulus: str, temperature: int, model: str):

    messages = copy.deepcopy(prompts)
    probe_stimulus = stimulus[1][0]
    question_stimulus = all_prompts.probing_no_template + "\n" + stimulus[1][1]

    messages.append({"role": "user", "content": probe_stimulus})

    probe_completion = openai.ChatCompletion.create(model=model, messages=messages, temperature = temperature)
    probe_message = probe_completion.choices[0].message.content

    messages.append({"role": "assistant", "content": probe_message})
    messages.append({"role": "user", "content": question_stimulus})

    chat_completion = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature)
    return probe_completion.choices[0].message.content + "\n\n" + chat_completion.choices[0].message.content, messages
    #return chat_completion.choices[0].message.content


def run_experiment(
        stimuli: list,
        prompt: str,
        prompt_method: str,
        few_shot_version: str,
        fs_prompt_directory: str,
        model: str,
        system: bool,
        folder: str,
        temperature: int,
        model_type: str

):
    if not os.path.exists(folder):
        os.mkdir(folder)

    set_api_key()

    if prompt_method == "few_shot":
        prompts = prompt_building.few_shot_prompt(few_shot_version=few_shot_version, prompt=prompt, fs_prompt_directory=fs_prompt_directory)
    elif prompt_method == "base_few_shot":
        prompts = prompt_building.baseline_few_shot_prompt(few_shot_version=few_shot_version, prompt=prompt, fs_prompt_directory=fs_prompt_directory)
    elif prompt_method == "cot":
        prompts = prompt_building.cot_prompt(prompt=prompt)
    elif prompt_method == "probing":
        prompts = prompt_building.zero_shot_prompt(prompt=prompt, system=system)
    elif prompt_method == "probing2":
        prompts = prompt_building.zero_shot_prompt(prompt=prompt, system=system)
    elif prompt_method == "individual_probing":
        prompts = prompt_building.zero_shot_prompt(prompt=prompt, system=system)
    elif prompt_method == "calib_zero_shot":
        prompts = prompt_building.zero_shot_prompt(prompt=prompt, system=system)
    elif prompt_method == "calib_conv":
        prompts = prompt_building.zero_shot_prompt(prompt=prompt, system=system)
    elif prompt_method == "zero_shot":
        prompts = prompt_building.zero_shot_prompt(prompt=prompt, system=system)
    elif prompt_method == "conversation":
        prompts = prompt_building.conversation_prompt_generic(prompt=prompt, fs_prompt_directory=fs_prompt_directory)
    # currently defaults to zero shot prompting but could also throw an error or something I guess
    else:
        prompts = prompt_building.zero_shot_prompt(prompt=prompt, system=system)

    run_stimuli_set(prompt_method, folder, model, prompts, stimuli, system, temperature, model_type)


def run_stimuli_set(prompt_method, folder, model, prompts, stimuli, system, temperature, model_type):
    for i in range(0, len(stimuli), 1):
        stimulus_entry = stimuli[i]
        stimuli_set = stimulus_entry[1]
        name = stimulus_entry[0]
        results: list[list[str]] = []
        messages_list = []

        print(" Looking at Stimulus Set #" + name)

        for stimulus in stimuli_set:
            result, messages = run_stimulus(prompt_method, model, prompts, stimulus, system, temperature, model_type)
            results.append([stimulus[0], result])
            messages_list.append([stimulus[0],messages])
            print(f"Stimulus {stimuli_set.index(stimulus) + 1} of {len(stimuli_set)} in set #{name} has been processed")

        print(f"The results of {name} are about to be noted.")
        result_writer.write_result(results, name, folder)
        result_writer.save_messages_csv(messages_list, name, model, folder, folder)
        # run id is always folder (folder, folder..)
        result_writer.write_result_csv(results, name, model, folder, prompt_method, temperature, folder)


def run_stimulus(prompt_method, model, prompts, stimulus, system, temperature, model_type):

    if model_type == "gpt":

        if system and prompt_method == "few_shot":
            print("...contacting server")
            return run_chat_completion_w_backoff_and_system_and_few_shot(
                prompts=prompts,
                stimulus=stimulus,
                model=model,
                temperature=temperature
            )
        elif system and prompt_method == "base_few_shot":
            print("...contacting server")
            return run_chat_completion_w_backoff_and_system_and_few_shot(
                prompts=prompts,
                stimulus=stimulus,
                model=model,
                temperature=temperature
            )
        elif system and prompt_method == "cot":
            print("...contacting server")
            return run_chat_completion_w_backoff_and_system_and_few_shot(
                prompts=prompts,
                stimulus=stimulus,
                model=model,
                temperature=temperature
            )
        elif system and prompt_method == "probing":
            print("...contacting server for zero shot")
            return run_chat_completion_w_backoff_and_system(
                prompts=prompts,
                stimulus=stimulus,
                model=model,
                temperature=temperature
            )
        elif system and prompt_method == "probing2":
            print("...contacting server for probing2")
            return run_conversational_chat_completion_probe(
                prompts=prompts,
                stimulus=stimulus,
                model=model,
                temperature=temperature
            )
        elif system and prompt_method == "calib_conv":
            print("...contacting server for conversational calibration")
            return run_conversational_chat_completion_calib(
                prompts=prompts,
                stimulus=stimulus,
                model=model,
                temperature=temperature
            )

        elif system and prompt_method == "conversation":
            print("...contacting server for conversational chat completion")
            return run_conversational_chat_completion_generic(
                prompts=prompts,
                stimulus=stimulus,
                model=model,
                temperature=temperature
            )

        elif system:
            print("...contacting server for zero shot")
            return run_chat_completion_w_backoff_and_system(
                prompts=prompts,
                stimulus=stimulus,
                model=model,
                temperature=temperature
            )

    elif model_type == "ollama":
        if prompt_method == "conversation":
            print("ollama doing conversational chat completion")
            result, messages = ollama_test.ollama_chat_call_generic_conv(prompts, stimulus, t=temperature, model = model)
            return result, messages
        else:

            #TODO implement other analogous prompting method? Not sure if a differentaiation is needed at this point actually?
            print("doing ollama shit")
            result, placeholder = ollama_test.ollama_chat_call_test(prompts, stimulus, t=temperature, model = model)
            #print(result)
            return result['message']['content'], placeholder
    #run completion doesn't work anyways so maybe throw error instead
    #return run_completion(prompt=prompt + stimulus, model=model)

