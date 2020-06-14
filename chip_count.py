import pandas as pd
import matplotlib.pyplot as plt

text = open('my_name_is_masha_rus.txt', encoding = 'utf-8', mode = 'r').read()



def repeated_chip_places(lang, chip_size):
    chip_places = {}
    for i in range(len(lang)):
        if lang[i:i+chip_size] in chip_places.keys():
            chip_places[lang[i:i+chip_size]].append(i)
        else:
            chip_places[lang[i:i+chip_size]] = [i]
    return chip_places


rep_pos = repeated_chip_places(text,3)

chip_repetitions = []
for chip in rep_pos.items():
    chip_repetitions.append((len(chip[1]), chip[0]))
chip_repetitions.sort()


df = pd.DataFrame(chip_repetitions)
df.columns = ['frequency', 'sequence']
print(df.tail(25))
x_labels = df["sequence"].tail(25).values.tolist()
print(x_labels)
df.tail(25).plot(kind='bar', use_index=False)
plt.xticks(ticks=df.head(25).index, labels = x_labels)
plt.show()
