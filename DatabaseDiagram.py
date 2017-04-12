import pandas as pd
import matplotlib.pyplot as plt

raw_data = {'maand': ['Jan', 'Feb', 'Mar', 'Apr', 'May', "Jun", 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'cijfers_11': [10,1,0,16,36,21,20,17,21,32,23,37],
        'cijfers_12': [43,58,43,32,28,33,32,32,24,28,13,21]}
df = pd.DataFrame(raw_data, columns = ['maand', 'cijfers_11', 'cijfers_12'])

pos = list(range(len(df['cijfers_11'])))
width = 0.25

fig, ax = plt.subplots(figsize=(10,5))

plt.bar(pos,
        df['cijfers_11'],
        width,
        alpha=0.5,
        color='#EE3224',
        label=df['maand'][0])

plt.bar([p + width for p in pos],
        df['cijfers_12'],
        width,
        alpha=0.5,
        color='c',
        label=df['maand'][1])

ax.set_ylabel('Aantal')
ax.set_title('Straatroven per maand in 2011 en 2012 \n Leeftijdsgroep 18-24 jaar')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(df['maand'])

plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['cijfers_11'] + df['cijfers_12'])] )

plt.legend(['2011', '2012'], loc='upper right')
plt.grid()
plt.show()
