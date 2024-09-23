import gensim.downloader as api
import inflection

"""
models

word2vec-google-news-300
glove-wiki-gigaword-100

"""
print("loading, please wait")
model = api.load("word2vec-google-news-300")
choice = None



while True:
    add_words = []
    sub_words = []
    inputs = []
    choice = None

    while choice not in ["+", "-", "*"]:
        choice = input("\n\n+: addition mode\n-: subtraction mode\n*: compound mode\n")
        pass
    
    print()
    if choice == "+":
        add_words = [input("add a word "), input("add another word to that ")]
        inputs = add_words
    elif choice == "-":
        add_words = [input("add a word ")]
        sub_words = [input("subtract the word with ")]
        inputs = [add_words[0], sub_words[0]]
    elif choice == "*":
        continue

    result = model.most_similar(positive=add_words, negative=sub_words)
    most_similar_key, similarity = result[0]

    for inputted in inputs:
        results_list = [key_result[0] for key_result in result]
        pluralized_input = inflection.pluralize(inputted)
        if pluralized_input in results_list:
            print("removed", result[results_list.index(pluralized_input)])
            result.pop(results_list.index(pluralized_input))

    if choice in ["+", "-"]:
        print(add_words[0], choice, add_words[1] if choice == "+" else sub_words[0], "=", result[0][0])
        print(similarity, "\n\ntop 5 runner ups:")

    for i in range(1, 6):
        most_similar_key, similarity = result[i]
        print(inflection.ordinalize(i+1)+":", add_words[0], choice, add_words[1] if choice == "+" else sub_words[0], "=", most_similar_key)
    input("enter to use again")



