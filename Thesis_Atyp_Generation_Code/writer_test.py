import result_writer


results = [ ["1,",""""
    Begin setting: 2 
X: AI
Q: How often do you think John usually pays the cashier when going shopping?
A: 100%
R: John always pays the cashier when going shopping because it is a common practice to pay for groceries at the store.

Q: How often do you think John usually gets apples when going shopping?
A: 50%
R: John may or may not get apples when going shopping, as it depends on his preference and shopping list. It is a common item to buy at the grocery store, but not everyone buys apples every time they shop.

X: Person
Q: How often do you think John usually pays the cashier when going shopping?
A: 90%
R: John always pays the cashier when shopping, as it is the standard procedure at stores.

Q: How often do you think John usually gets apples when going shopping?
A: 70%
R: John often buys apples when shopping, as he enjoys having them as a snack or for cooking.
End setting: 2 """],["11ww",
            """
                Begin setting: 3 
            X: XXAI
            Q: XXHow often do you think John usually pays the cashier when going shopping?
            A: 10%
            R: XXJohn always pays the cashier when going shopping because it is a common practice to pay for groceries at the store.

            Q: XXHow often do you think John usually gets apples when going shopping?
            A: 5%
            R: John may or may not get apples when going shopping, as it depends on his preference and shopping list. It is a common item to buy at the grocery store, but not everyone buys apples every time they shop.

            X: XXPerson
            Q: XXHow often do you think John usually pays the cashier when going shopping?
            A: 9%
            R: XXJohn always pays the cashier when shopping, as it is the standard procedure at stores.

        """
            ], ["22ww",
            """
                Begin setting: 3 
            X: XXAI
            Q: XXHow often do you think John usually pays the cashier when going shopping?
            A: 10%
            R: XXJohn always pays the cashier when going shopping because it is a common practice to pay for groceries at the store.

            
            X: XXPerson
            Q: XXHow often do you think John usually pays the cashier when going shopping?
            A: 9%
            R: XXJohn always pays the cashier when shopping, as it is the standard procedure at stores.

        """
            ], ["zzzzz",
            """
                Begin setting: 3 
            X: YYAI
            Q: YYHow often do you think John usually pays the cashier when going shopping?
            A: 10%
            R: YYJohn always pays the cashier when going shopping because it is a common practice to pay for groceries at the store.

            Q: YYHow often do you think John usually gets apples when going shopping?
            A: 5%
            R: John may or may not get apples when going shopping, as it depends on his preference and shopping list. It is a common item to buy at the grocery store, but not everyone buys apples every time they shop.

            X: YYPerson
            Q: XXHow often do you think John usually pays the cashier when going shopping?
            A: 9%
            R: YYJohn always pays the cashier when shopping, as it is the standard procedure at stores.

            Q: YYHow often do you think John usually gets apples when going shopping?
            A: 7%
            R: YYJohn often buys apples when shopping, as he enjoys having them as a snack or for cooking.
            End setting: 3 """
            ]]
results2 = [
    """
X: AI
Q: How often do you think John usually pays the cashier when going shopping?
A: 100%
R: John usually pays the cashier every time he goes shopping because that is the normal expectation when purchasing items from a grocery store.

X: AI
Q: How often do you think John usually gets apples when going shopping?
A: 50%
R: Since the context does not provide any specific information about John's preference for apples, it is reasonable to assume that he might buy apples half of the time and not buy them the other half.

X: Human
Q: How often do you think John usually pays the cashier when going shopping?
A: 100%
R: John always pays the cashier when going shopping as that is the normal expectation for any purchase made at a store.

X: Human
Q: How often do you think John usually gets apples when going shopping?
A: It depends on John's personal preference and whether he likes apples or not. If he likes apples, he might get them around 75% of the time. If he doesn't like apples or prefers other fruits, he might only get them around 25% of the time.

    """,
    """
X: I'm an AI language model and I don't have access to personal information about individuals. Therefore, I cannot provide an accurate answer based on specific knowledge of John or the people mentioned in the context.

Q1: How often do you think John usually pays the cashier when going shopping?
A: John seems to be typically broke and doesn't usually pay when he goes to the grocery store, so I would estimate that he pays the cashier 0% of the time.

R: Based on the information given that John is typically broke and doesn't usually pay when going shopping, it suggests that he might not pay the cashier at all. However, this is a speculative assumption based on the limited information provided.

A (person that knows John): John usually doesn't pay the cashier when going shopping.
R: The answer assumes that the person has observed John's behavior over time and is aware of his financial situation and habits.

Q2: How often do you think John usually gets apples when going shopping?
A: Based on the context provided, there is no specific mention of John getting apples during his shopping trips, so it's difficult to determine how often he usually gets them. Therefore, I cannot provide a definitive answer.

R: The context does not provide any information about John's preference for apples or frequency of getting them during shopping trips. Without this information, it is not possible to estimate the frequency with any certainty.

A (person that knows John): It's uncertain how often John usually gets apples when going shopping.
R
    """,
    """
X: AI
Q: How often do you think John usually pays the cashier when going shopping?
A: 100%
R: Based on the context, it is stated that John paid the cashier when he came back from the grocery store. It can be assumed that John usually pays the cashier when going shopping.

Q: How often do you think John usually gets apples when going shopping?
A: 50%
R: There is no explicit mention of John getting apples in the context. It is unclear how often John gets apples when going shopping. A person familiar with John's shopping habits may be able to give a more accurate answer.

    """,
    """
X: AI
Q1: How often do you think John usually pays the cashier when going shopping?
A: 0% of the time.
R: John is typically broke and doesn't usually pay when he goes to the grocery store, as mentioned in the context. Additionally, Susan specifically mentioned that John paid the cashier on this occasion, implying that it is not the usual scenario.

Q2: How often do you think John usually gets apples when going shopping?
A: N/A.
R: The context does not provide any information about John's usual grocery shopping habits regarding apples.

    """,
    """
X: I am sorry, but I don't have enough information to provide a definitive answer. 
Q: How often do you think John usually pays the cashier when going shopping?
A: It is likely that John usually pays the cashier every time he goes shopping.
R: Since John is depicted as a regular grocery shopper, it is common practice to pay at the cashier when making a purchase. 

Q: How often do you think John usually gets apples when going shopping?
A: It is possible that John usually gets apples sometimes when going shopping.
R: In this specific instance, Susan mentioned that John got apples. Therefore, it can be inferred that he occasionally purchases apples, but not necessarily every time. 

A person that knows the people mentioned in the context might answer the questions as follows:

Q: How often do you think John usually pays the cashier when going shopping?
A: 100%
R: Since the person knows John personally, they have direct knowledge of his shopping habits and can provide a definitive answer based on that knowledge.

Q: How often do you think John usually gets apples when going shopping?
A: 50%
R: The person might assume that John sometimes buys apples based on the information provided by Susan, but they cannot be certain about the frequency unless they have more specific knowledge about John's grocery shopping habits.

    """,
    """
    Begin setting: 3 
X: AI
Q: How often do you think John usually pays the cashier when going shopping?
A: 100%
R: John always pays the cashier when going shopping because it is a common practice to pay for groceries at the store.

Q: How often do you think John usually gets apples when going shopping?
A: 50%
R: John may or may not get apples when going shopping, as it depends on his preference and shopping list. It is a common item to buy at the grocery store, but not everyone buys apples every time they shop.

X: Person
Q: How often do you think John usually pays the cashier when going shopping?
A: 100%
R: John always pays the cashier when shopping, as it is the standard procedure at stores.

Q: How often do you think John usually gets apples when going shopping?
A: 70%
R: John often buys apples when shopping, as he enjoys having them as a snack or for cooking.
End setting: 3 """,
    """
X: AI
Q1: How often do you think John usually pays the cashier when going shopping?
A1: 0% of the time.
R1: John is typically broke and doesn't usually pay when he goes to the grocery store, implying that he frequently doesn't pay the cashier.

Q2: How often do you think John usually gets apples when going shopping?
A2: 100% of the time.
R2: Since Susan specifically mentioned that John got some apples from the grocery store, it can be inferred that John always gets apples when he goes shopping. 

A person who knows the people mentioned in the context
Q1: How often do you think John usually pays the cashier when going shopping?
A1: 0% of the time.
R1: Based on the information given that John is typically broke and doesn't usually pay at the grocery store, someone who knows him would primarily answer that he rarely or never pays the cashier.

Q2: How often do you think John usually gets apples when going shopping?
A2: 100% of the time.
R2: Since Susan specifically mentioned that John got apples from the grocery store, someone who knows John would assume that he always gets apples when he goes shopping.

           """]
result_writer.write_result_csv(results, "writer_test_temp", "none", "test_writer", "few_shot", 0.98)

