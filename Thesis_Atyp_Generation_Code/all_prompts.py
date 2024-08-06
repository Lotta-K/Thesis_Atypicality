
few_shot_full = """You will receive a context (C) and two questions (Q1, Q2).  
Answer the questions by rating the frequency on a scale from 0% of the time to 100% of the time. Explain your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
Additionally, tell me how a person that knows the people mentioned in the context would answer the below questions, using the same scale and explaining their answer in no more than two sentences.
You will be provided with 2 examples (Ex1, Ex2).
Use the following template for your output, where '<>' is a placeholder for content:
X: <AI or Person>
Q: <Q1 or Q2>
A: <Answer (0-100%)>
R: <Reasoning>"""

few_shot = """You will receive a context (C) and one question (Q1).  
Answer the questions by rating the frequency on a scale from 0% of the time to 100% of the time. Explain your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
You will be provided with 2 examples (Ex1, Ex2).
Use the following template for your output, where '<>' is a placeholder for content:
X: <AI>
Q: <Q1>
A: <Answer (0-100%)>
R: <Reasoning>"""

zero_shot = """You will receive a context (C) and two questions (Q1, Q2).  
Answer the questions by rating the frequency on a scale from 0% of the time to 100% of the time. Explain your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
Use the following template for your output, where '<>' is a placeholder for content:
X: <AI>
Q: <Q1 or Q2>
A: <Answer (0-100%)>
R: <Reasoning>"""


cot = """You will receive a context (C) and two questions (Q1, Q2).  
Answer the questions by rating the frequency on a scale from 0% of the time to 100% of the time. Show all the reasoning steps you took to reach your answer. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
You will be provided with 2 examples (Ex1, Ex2).
Use the following template for your output, where '<>' is a placeholder for content:
X: <AI>
Q: <Q1 or Q2>
R: <Reasoning>
A: <Answer>"""

zero_shot_old = """You will receive a context (C) and two questions (Q1, Q2).  
    Answer the questions by rating the frequency on a scale from 0% of the time to 100% of the time. Explain your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
    Additionally, tell me how a person that knows the people mentioned in the context would answer the below questions, using the same scale and explaining their answer in no more than two sentences.
    Use the following template for your output, where '<>' is a placeholder for content:
    X: <Responder: AI or Person>
    Q: <Question>
    A: <Answer>
    R: <Reasoning> 
    """


zero_shot_probing_intro = """You are an expert on human behavior and communication who will be answering questions (Q1, Q2) based on short contexts (C). There is no right or wrong answer to the questions you'll see, and you are willing to use your best judgement and commit to a concrete, specific response, even in cases where you can't be sure that you are correct. 
Answer the questions by rating the frequency on a scale from 0% of the time to 100% of the time. Give a short and concise reasoning to explain your answer.
Use the following template for your output, where '<>' is a placeholder for content:
X: <Responder: AI>
Q: <Q1 or Q2>
A: <Answer>
R: <Reasoning>"""

probing = """You are an expert on human behavior and communication who will be answering a question based on short contexts (C). There is no right or wrong answer to the questions you'll see, and you are willing to use your best judgement and commit to a concrete, specific response, even in cases where you can't be sure that you are correct. 
Please keep your answer as short and concise as possible.
Use the following template for your output, where '<>' is a placeholder for content:
X: <Responder: AI>
Q: <Q1-Q6>
A: <Answer>"""

probing_no_template = """You are an expert on human behavior and communication who will be answering questions based on short contexts (C). There is no right or wrong answer to the questions you'll see, and you are willing to use your best judgement and commit to a concrete, specific response, even in cases where you can't be sure that you are correct. 
Please keep your answer as short and concise as possible.
"""

conversation = """You are an expert on human behavior and communication who will be answering questions based on short contexts (C). There is no right or wrong answer to the questions you'll see, and you are willing to use your best judgement and commit to a concrete, specific response, even in cases where you can't be sure that you are correct. 
Please keep your answer as short and concise as possible. The fisrt question is: Can you identify a redundant information in the context C?
"""



#### What did I use this one for???
just_qs_intro = """Answer the following questions by rating the frequency on a scale from 0% of the time to 100% of the time. Give a short and concise reasoning to explain your answer.
Use the following template for your output, where '<>' is a placeholder for content:
X: <Responder: AI>
Q: <Q1 or Q2>
A: <Answer (0-100%)>
R: <Reasoning>"""

likert = """You will receive a context (C) and two questions (Q1, Q2). 
Answer the questions by rating the frequency on a scale from 1 to 7 (1 - Never; 2 - Rarely, less than 10% of the time; 3 - Occasionally, 30% of the time; 4 - Sometimes, about 50% of the time; 5 - Frequently, about 70% of the time; 6 - Usually, about 90% of the time; 7 - Every time).
Give a reasoning for your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
Use the following template for your output, where '<>' is a placeholder for content:
X: <AI>
Q: <Q1 or Q2>
A: <Answer>
R: <Reasoning>
"""

fs_likert = """You will receive a context (C) and one question (Q1).
Answer the questions by rating the frequency on a scale from 1 to 7 (1 - Never; 2 - Rarely, less than 10% of the time; 3 - Occasionally, 30% of the time; 4 - Sometimes, about 50% of the time; 5 - Frequently, about 70% of the time; 6 - Usually, about 90% of the time; 7 - Every time).
Give a reasoning for your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
You will be provided with 2 examples (Ex1, Ex2).
Use the following template for your output, where '<>' is a placeholder for content:
X: <AI>
Q: <Q1 or Q2>
A: <Answer>
R: <Reasoning>
"""

know_gen = """
You are an expert on human behavior and communication. In this conversation you will receive tasks and questions that you will answers as briefly and accurately as possible. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
"""

calibration = """
You will receive a context (C) and a question (Q1).
Answer the questions by rating the frequency from 0% of the time to 100% of the time. Give a reasoning for your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
Provide your 4 best guesses and the probability that each guess is correct (0.0 to 1.0).
Use the following template for your output, where '<>' is a placeholder for content:
X: <Guess (1-4)>
Q: <Q1>
A: <Answer (0%-100%)>
P: <Probability (0.0 to 1.0)>
R: <Reasoning>
"""


calibration_conversational_a = """
You will receive a context (C) and a question (Q1).
Answer the questions by rating the frequency from 0% of the time to 100% of the time. Give a reasoning for your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
Provide your 4 best guesses.
Use the following template for your output, where '<>' is a placeholder for content:
X: <Guess (1-4)>
A: <Answer (0%-100%)>
R: <Reasoning>
"""

calibration_conversational_b = """
Given the 4 guesses you provided, assign each a probability that it is the correct guess (0.0 to 1.0).
Use the following template for your output, where '<>' is a placeholder for content:
X: <Guess (1-4)>
A: <Answer (0%-100%)>
R: <Reasoning>
P: <Probability (0.0 to 1.0)>

"""

calibration_orig = """
You will receive a context (C) and a question (Q1). Provide your 4 best guesses and the probability that the guess is correct (0.0 to 1.0).
Answer the questions by rating the frequency from 0% of the time to 100% of the time. Give a reasoning for your answer in no more than two sentences. Always give a definitive answer, even if that means making assumptions and speculating based on common knowledge of human behavior.
Provide your 4 best guesses and the probability that the guess is correct (0.0 to 1.0).
Use the following template for your output, where '<>' is a placeholder for content:
X: <Guess (1-4)>
Q: <Q1>
A: <Answer (0%-100%)>
P: <Probability (0.0 to 1.0)>
R: <Reasoning>
"""