import pandas as pd
import matplotlib.pyplot as plt

def robGraph():
        raw_data = {'maand': ['Jan', 'Feb', 'Mar', 'Apr', 'May', "Jun", 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                'cijfers_11': [10,1,0,16,36,21,20,17,21,32,23,37], #values van de maanden
                'cijfers_12': [43,58,43,32,28,33,32,32,24,28,13,21]} #values van de maanden
        df = pd.DataFrame(raw_data, columns = ['maand', 'cijfers_11', 'cijfers_12']) #dataframe

        position = list(range(len(df['cijfers_11']))) #position bars
        width = 0.25 #width bars

        fig, ax = plt.subplots(figsize=(10,5)) #plotting bars

        plt.bar(position, df['cijfers_11'], #eerste bar met cijfers_11 #dataframe van cijfers_11
                width, alpha=0.5, color='#EE3224', label=df['maand'][0]) #eerste value in maand

        plt.bar([p + width for p in position], #tweede bar met cijfers_12
                df['cijfers_12'],
                width, alpha=0.5, color='c', label=df['maand'][1]) #tweede value in 'maand'

        ax.set_ylabel('Aantal') #label voor y-as woord 'Aantal' genoemd
        ax.set_xlabel('Maanden') #label voor x-as
        ax.set_title('Straatroven per maand in 2011 en 2012 \n Leeftijdsgroep 18-24 jaar') #titel van diagram
        ax.set_xticks([p + 1.5 * width for p in position]) #positie van xticks
        ax.set_xticklabels(df['maand']) #label voor xticks

        plt.xlim(min(position)-width, max(position)+width*4) #min en max aangeven voor x- en y-as
        plt.ylim([0, max(df['cijfers_11'] + df['cijfers_12'])] )

        plt.legend(['2011', '2012'], loc='upper right') #legenda's met twee values
        plt.grid()
        plt.show()
robGraph()
