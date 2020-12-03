import random
import tkinter


def pairs(words):
    for i in range(len(words) - 1):
        yield words[i], words[i + 1]


def make_markov_chains(words):
    pair = pairs(words)
    markov_chains = dict()
    for word_1, word_2 in pair:
        if word_1 in markov_chains.keys():
            markov_chains[word_1].append(word_2)
        else:
            markov_chains[word_1] = [word_2]
    return markov_chains


def choose_upper_word(markov_chains):
    upper_words = [key for key in markov_chains.keys() if key.isupper()]
    return random.choice(upper_words)


def generate_text():
    len_ = length.get()
    markov_chains = chains
    chain = []
    chosen_word = choose_upper_word(markov_chains)
    for i in range(len_):
        chain.append(chosen_word)
        chosen_word = random.choice(markov_chains[chosen_word])
    result.insert(tkinter.END, ' '.join(chain))


with open("./file.txt", 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split() 
chains = make_markov_chains(words) 

root = tkinter.Tk()
root.title('Markov chains')
root.geometry("1200x600")
button = tkinter.Button(root, text='generate text', command=generate_text)
length = tkinter.IntVar()
label = tkinter.Label(root, text="Number of words: ")
label.place(x=50, y=25)
length_entry = tkinter.Entry(root, textvariable=length)
length_entry.place(x=50, y=45, width=35)
length.set(300)
button.place(x=50, y=75)
result = tkinter.Text(root, font=('Consolas', 10), tabs=('3c'))
result.place(x=350, y=100, width=700, height=300)
root.mainloop()



