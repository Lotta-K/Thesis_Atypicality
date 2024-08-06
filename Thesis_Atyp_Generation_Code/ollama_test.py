import copy

from ollama import Client

model_types = {"llama3_instruct": "llama3:instruct" , "mixtral": "mixtral:8x7b"}


def ollama_chat_call(model, prompt, ip='127.0.0.1', port=11434):

    client = Client(host=f'http://{ip}:{port}')
    response = client.chat(model=model,
                           messages=[{'role': 'user', 'content': prompt},],
                           options={"seed": 5, "temperature": 0.8, "num_predict": 1000,
                                    "repeat_penalty": 1.2, "top_p": 0.9, "top_k": 40},
                           stream=False)
    return response

def ollama_chat_call_test(prompts, stimulus, t, model, ip='127.0.0.1', port=11434):

    model = model_types[model]
    print(model)
    messages = copy.deepcopy(prompts)
    messages.append({"role": "user", "content": stimulus[1]})

    #print(messages)

    client = Client(host=f'http://{ip}:{port}')
    response = client.chat(model=model,
                           messages= messages,
                           options={"seed": 5, "temperature": t, "num_predict": 1000,
                                    "repeat_penalty": 1.2, "top_p": 0.9, "top_k": 40},
                           stream=False)
    return response, messages

def ollama_chat_call_generic_conv(prompts, stimulus, t, model, ip='127.0.0.1', port=11434):

    model = model_types[model]
    cur_prompts = copy.deepcopy(prompts)
    messages = [cur_prompts[0]]

    client = Client(host=f'http://{ip}:{port}')

    for i in range(1, len(prompts) - 1):
        cur_prompt = cur_prompts[i]

        cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[1]))
        cur_prompt = cur_prompt.replace("QUESTION", str(stimulus[2]))
        if len(stimulus) > 3:
            cur_prompt = cur_prompt.replace("GENERATION", str(stimulus[3]))
        messages.append({"role": "user", "content": cur_prompt})

        completion = client.chat(model=model,
                           messages= messages,
                           options={"seed": 5, "temperature": t, "num_predict": 1000,
                                    "repeat_penalty": 1.2, "top_p": 0.9, "top_k": 40},
                           stream=False)
        #completion_message = completion.choices[0].message.content
        completion_message = completion['message']['content']
        messages.append({"role": "assistant", "content": completion_message})
        print("I have hopped")
        i += 1

    cur_prompt = cur_prompts[-1]
    cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[1]))
    cur_prompt = cur_prompt.replace("QUESTION", str(stimulus[2]))
    if len(stimulus) > 3:
        cur_prompt = cur_prompt.replace("GENERATION", str(stimulus[3]))
    messages.append({"role": "user", "content": cur_prompt})

    # if "STIMULUS" in cur_prompt:
    #   cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[1]))
    #  messages.append({"role": "user", "content": cur_prompt})
    # if "QUESTION" in cur_prompt:
    #    cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[2]))
    # messages.append({"role": "user", "content": cur_prompt})
    # if "GENERATION" in cur_prompt:
    #  cur_prompt = cur_prompt.replace("STIMULUS", str(stimulus[3]))
    #   messages.append({"role": "user", "content": cur_prompt})
    # else:
    #    messages.append({"role": "user", "content": cur_prompt})

    completion = client.chat(model=model,
                             messages=messages,
                             options={"seed": 5, "temperature": t, "num_predict": 1000,
                                      "repeat_penalty": 1.2, "top_p": 0.9, "top_k": 40},
                             stream=False)
    # return completion.choices[0].message.content + "\n" + "<SPLIT>" + "\n" + str(messages)
    #return completion.choices[0].message.content, messages
    return completion['message']['content'], messages

def ollama_generate_call(model, prompt, ip='127.0.0.1', port=11434):

    client = Client(host=f'http://{ip}:{port}')
    response = client.generate(model=model,
                               prompt=prompt,
                               options={"seed": 5, "temperature": 0.8, "num_predict": 1000,
                                    "repeat_penalty": 1.2, "top_p": 0.9, "top_k": 40},
                               stream=False)
    return response

if __name__ == '__main__':
    model = "llama3:instruct"
    prompt = "What is Llama-3? Can you make a joke about it?"
    response = ollama_chat_call(model, prompt)
    print(response)
    response = ollama_generate_call(model, prompt)
    print(response)

