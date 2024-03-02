# import: internal
from notion_automation import create_page
from notion_automation.vocab import WordLookup

# load some vocab.
file_path = "notion_automation/vocab/examples/word_examples.txt"
with open(file_path, "r") as file:
    vocabs = file.read()

# initialize the lookup engine.
word_finder = WordLookup()
vocabs = vocabs.split("\n")

# keep adding new vocab.
unknowns = []
for i, vocab in enumerate(vocabs):
    if i % 10 == 0:
        print(i)
    try:
        input_dict = word_finder.get_word_info(vocab)
        create_page(input_dict)
    except:
        unknowns.append(vocab)

# write the unknowns to add them manually.
file_path = "notion_automation/vocab/examples/unknowns.txt"
with open(file_path, "w") as file:
    file.write("{}".format("\n".join(unknowns)))
