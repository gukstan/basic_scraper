import pandas as pd

premier_2022 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')


premier_2022.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'}, inplace=True)

premier_2022