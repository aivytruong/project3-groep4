import pandas as pd
import matplotlib.pyplot as plt

def robGraph():
        raw_data = {'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', "Jun", 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                'numbers_11': [10,1,0,16,36,21,20,17,21,32,23,37], #values of the months
                'numbers_12': [43,58,43,32,28,33,32,32,24,28,13,21]} #values of the months
        df = pd.DataFrame(raw_data, columns = ['months', 'numbers_11', 'numbers_12']) #dataframe

        position = list(range(len(df['numbers_11']))) #position bars
        width = 0.25 #width bars

        fig, ax = plt.subplots(figsize=(10,5)) #plotting bars

        plt.bar(position, df['numbers_11'], #first bar of numbers_11 #dataframe of numbers_11
                width, alpha=0.5, color='#EE3224', label=df['months'][0]) #first value of month

        plt.bar([p + width for p in position], #second bar with number 12
                df['numbers_12'],
                width, alpha=0.5, color='c', label=df['months'][1]) #second value in 'month'

        ax.set_ylabel('Amount') #label for  y-axis is called 'Amount'
        ax.set_xlabel('Months') #label voor x-axis is called 'Months'
        ax.set_title('Robberies each month in 2011 and 2012 \n Age group 18-24 years') #title of diagram
        ax.set_xticks([p + 1.5 * width for p in position]) #position van xticks
        ax.set_xticklabels(df['months']) #label for xticks

        plt.xlim(min(position)-width, max(position)+width*4) #show min and max for x-axis and y-axis
        plt.ylim([0, max(df['numbers_11'] + df['numbers_12'])] )

        plt.legend(['2011', '2012'], loc='upper right') #legends with two values
        plt.grid()
        plt.show()

#robGraph()
