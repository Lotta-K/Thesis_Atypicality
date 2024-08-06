from datetime import datetime
from multiprocessing import Process
import time

import prompt_building
import prompting
import stimulus_reader
import all_prompts


def print_execution_statistic(_processes, stimuli_per_chunk, start_time):
    j = 0

    for _p in _processes:
        _p.join()
        print((j * stimuli_per_chunk), '/ 24')
        j += 1

    elapsed_time = time.time() - start_time
    print('Execution time:', elapsed_time / 60, 'mins')


def xstr(s):
    """

    :param s:
    :return:
    """
    if s is None:
        return ''
    else:
        return str(s) + "_"


default_prompts = {
    "zero_shot": all_prompts.zero_shot,
    "base_few_shot": all_prompts.few_shot,
    "few_shot": all_prompts.few_shot,
    "probing": all_prompts.probing,
    "probing2": all_prompts.probing_no_template,
    "individual_probing":all_prompts.probing,
    "calib_zero_shot": all_prompts.calibration,
    "calib_conv": all_prompts.calibration_conversational_a,
    "cot": all_prompts.cot,
    "conversation": all_prompts.conversation
}

additional_prompts = {
    "likert": all_prompts.likert,
    "fs_likert": all_prompts.fs_likert,
    "alternate": all_prompts.zero_shot_probing_intro,
    "know_gen": all_prompts.know_gen,
    "hop": all_prompts.know_gen
}

gpt_models = ("gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-2024-04-09")

ollama_models = ("llama3_instruct", "mixtral")


def determine_model_type(_model):
    if _model in gpt_models:
        return "gpt"
    elif _model in ollama_models:
        return "ollama"
    else:
        raise Exception("Unknown model type")


def determine_prompt(_prompt, _prompt_method):
    if _prompt is None:
        _prompt = default_prompts[_prompt_method]
        return _prompt
    elif _prompt in additional_prompts.keys():
        _prompt = additional_prompts[_prompt]
        return _prompt
    else:
        raise Exception(
            "You have specified an invalid prompt. Please specify a valid prompt or None to use the default prompt.")


def set_fs_directory(_fs_prompt_directory, _prompt_method):
    if _fs_prompt_directory is None and (_prompt_method == "few_shot" or _prompt_method == "base_few_shot"):
        fs_prompt_directory = "Few_Shot_Prompts_1303"
    elif _fs_prompt_directory is None and _prompt_method == "conversation":
        raise Exception("Conversation needs a directory specifying the prompts")
    elif _fs_prompt_directory is not None and _prompt_method != "few_shot" and _prompt_method != "base_few_shot" and _prompt_method != "conversation":
        fs_prompt_directory = None
    else:
        fs_prompt_directory = _fs_prompt_directory

    if fs_prompt_directory is not None:
        fs_prompt_directory = "prompt_directories/"+fs_prompt_directory

    return fs_prompt_directory


class ExperimentArguments:
    def __init__(
            self,
            _prompt_method: str,
            _model: str,
            _system=True,
            _prompt=None,
            _few_shot_version=None,
            _fs_prompt_directory=None,
            _temperature: float = 1,
            _notes="",
            _settings=[1, 2, 3, 4, 5, 6]
    ):
        self.prompt_method = _prompt_method
        self.prompt = determine_prompt(_prompt, _prompt_method)
        self.prompt_type = _prompt
        self.model = _model
        self.system = _system
        self.folder = f"{datetime.now().strftime('%Y-%m-%d_%H-%M')}_{_model}_t-{_temperature}_{_prompt_method}_{xstr(_few_shot_version)}{xstr(_fs_prompt_directory)}{xstr(_prompt)}{_notes}"
        self.temperature = _temperature
        self.few_shot_version = _few_shot_version
        self.settings = _settings
        self.fs_prompt_directory = set_fs_directory(_fs_prompt_directory, _prompt_method)
        self.model_type = determine_model_type(_model)


def main():
    start_time = time.time()
    experiment_arguments = ExperimentArguments(
        _prompt_method="conversation",
        _model="gpt-4",  #"gpt-3.5-turbo" #"gpt-4-1106-preview #gpt-4 #gpt-4-turbo-2024-04-09 #llama3_instruct #mixtral
        _system=True,
        _prompt="hop",
        _temperature=1,
        _notes="fr",  #fr or partial or test: default empty
        _fs_prompt_directory="conv_3_hop_c",
        #_few_shot_version="High"
        #_settings = [1,3,5] #default [1,2,3,4,5,6] not relevant if prompt method defines needed settings
    )

    stimuli_per_chunk = 3 # 3 for gpt-4 with 24 stimuli or it will collapse

    # MAKE SURE IN FEW_SHOT THIS MATCHES WHAT STIMULI ARE USED AS EXEMPLARS: High -> 1,6 mixed->1,10 low-> 3,10
    stimuli_to_be_excluded = []
    if experiment_arguments.few_shot_version == "Low":
        stimuli_to_be_excluded = ["10", "3"]
    elif experiment_arguments.few_shot_version == "Mix":
        stimuli_to_be_excluded = ["1", "10"]
    elif experiment_arguments.few_shot_version == "Opposite mix":
        stimuli_to_be_excluded = ["6", "3"]
    elif experiment_arguments.few_shot_version == "High":
        stimuli_to_be_excluded = ["1", "6"]

    # manually exclude stimuli
    #stimuli_to_be_excluded = ["2", "3", "4", "5", "6",  "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]

    stimuli = stimulus_reader.read_stimuli(stimuli_to_be_excluded, experiment_arguments.settings,
                                           experiment_arguments.prompt_method, experiment_arguments.prompt_type)

    chunks = [stimuli[i:i + stimuli_per_chunk] for i in range(0, len(stimuli), stimuli_per_chunk)]
    processes = []
    i = 0

    for chunk in chunks:
        #chunk_off_set = (i * stimuli_per_chunk) + global_offset

        p = Process(target=prompting.run_experiment, args=(
            chunk,
            experiment_arguments.prompt,
            experiment_arguments.prompt_method,
            experiment_arguments.few_shot_version,
            experiment_arguments.fs_prompt_directory,
            experiment_arguments.model,
            experiment_arguments.system,
            experiment_arguments.folder,
            experiment_arguments.temperature,
            experiment_arguments.model_type
        ))

        processes.append(p)
        p.start()

        i += 1

    print_execution_statistic(processes, stimuli_per_chunk, start_time)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
