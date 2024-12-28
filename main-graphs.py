import matplotlib.pyplot as plt
import pandas as pd
import os

# Number of tables to extract
number_tables = 24

# list of key-words to analyze
formatted_key_words = ['Model-Agency', 'Model-Agency-London', 'London-Model-Agencies', 'London-Model-Agency',
                       'Male-Models-London', 'Curvy-Model-Agency', 'Big-and-Tall-Model-Agency',
                       'Plus-Size-Model-Agency', 'Plus-Size-Model-Agency-UK', 'Curve-Models-London',
                       'Plus-Size-Models-London', 'London-Influencer-Agency', 'Influencers', 'Models',
                       'Male-Models-New-York', 'Models-New-York', 'New-York-Models', 'New-York-Model-Agency',
                       'Big-and-Tall-Models-New-York', 'New-York-Influencer-Agency', 'Plus-Size-Models',
                       'Curve-Models', 'Big-and-Tall-Models', 'Plus-Size-Influencers']

key_words = ['Model Agency', 'Model Agency London', 'London Model Agencies', 'London Model Agency',
             'Male Models London', 'Curvy Model Agency', 'Big and Tall Model Agency', 'Plus Size Model Agency',
             'Plus Size Model Agency UK', 'Curve Models London', 'Plus Size Models London', 'London Influencer Agency',
             'Influencers', 'Models', 'Male Models New York', 'Models New York', 'New York Models',
             'New York Model Agency', 'Big and Tall Models New York', 'New York Influencer Agency', 'Plus Size Models',
             'Curve Models', 'Big and Tall Models', 'Plus Size Influencers']


def mk_graph_clicks(fkws, kws):
    i = 0
    for index in range(number_tables):
        # Read csv file
        file_path = f'/Users/stefanobeni/Code_Projects/Misc_Projects/modelling-seo-kwt/{fkws[i]}-table.csv'
        df = pd.read_csv(file_path)

        dates = df.iloc[1:5, 1]
        clicks = df.iloc[1:5, 3].astype(float)
        impressions = df.iloc[1:5, 4].astype(float)
        ctr = df.iloc[1:5, 5].astype(float)
        # position = df.iloc[1:5, 6].astype(float)

        fig, ax1 = plt.subplots()

        # Plot clicks and impressions on the primary y-axis
        ax1.plot(dates, clicks, label="Clicks", color='blue')
        ax1.plot(dates, ctr, label="CTR", color='green')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Clicks / CTR')

        # Create a secondary y-axis for ctr
        ax2 = ax1.twinx()
        ax2.plot(dates, impressions, label="Impressions", color='red')
        # ax2.plot(dates, position, label="Position", color='orange')
        ax2.set_ylabel('Impressions')

        # Show legend for both y-axes
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

        fig.tight_layout()  # Adjust layout to prevent overlap

        plt.title(kws[i])

        # Create a new directory to save figures if it doesn't exist
        save_dir = '/Users/stefanobeni/Code_Projects/Misc_Projects/modelling-seo-kwt/graphs1'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Save the figure
        save_path = os.path.join(save_dir, f'{fkws[i]}-graph1.png')
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

        plt.close()
        # plt.show()

        i += 1


def mk_graph_position(fkws, kws):
    i = 0
    for index in range(number_tables):
        # Read csv file
        file_path = f'/Users/stefanobeni/Code_Projects/Misc_Projects/modelling-seo-kwt/{fkws[i]}-table.csv'
        df = pd.read_csv(file_path)

        dates = df.iloc[1:5, 1]
        position = df.iloc[1:5, 6].astype(float)

        plt.plot(dates, position, label="Position", color='orange')
        plt.xlabel('Date')
        plt.ylabel('Position')

        '''
        fig, ax1 = plt.subplots()

        # Plot clicks and impressions on the primary y-axis
        ax1.plot(dates, clicks, label="Clicks", color='blue')
        ax1.plot(dates, ctr, label="CTR", color='green')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Clicks / CTR')

        # Create a secondary y-axis for ctr
        ax2 = ax1.twinx()
        ax2.plot(dates, impressions, label="Impressions", color='red')
        # ax2.plot(dates, position, label="Position", color='orange')
        ax2.set_ylabel('Impressions')

        # Show legend for both y-axes
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
        '''

        plt.tight_layout()  # Adjust layout to prevent overlap

        plt.title(kws[i])

        # Create a new directory to save figures if it doesn't exist
        save_dir = '/Users/stefanobeni/Code_Projects/Misc_Projects/modelling-seo-kwt/graphs2'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Save the figure
        save_path = os.path.join(save_dir, f'{fkws[i]}-graph2.png')
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

        plt.close()
        # plt.show()

        i += 1


# mk_graph_clicks(formatted_key_words, key_words)
# mk_graph_position(formatted_key_words, key_words)
