"""Plot long format table of point charges.
Copyright 2019 Simulation Lab
University of Freiburg
Author: Lukas Elflein <elfleinl@cs.uni-freiburg.de>
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def default_style(func):
	"""A decorator for setting global plotting styling options."""
	def wrapper(*args, **kwargs):
		fig = plt.figure(figsize=(16,10))
		sns.set_context("talk", font_scale=0.9)
		plt.xlim(-2, 2)
		plt.tick_params(grid_alpha=0.2)
		func(*args, **kwargs)
		plt.clf()
	return wrapper


@default_style
def boxplot(df):
   bp = sns.boxplot(x='value', y='atom', data=df, whis=100)#, hue='variable')
   bp.figure.savefig('box.png')


def swarmplot(df):   
   bp = sns.swarmplot(x='value', y='atom', data=df, hue='variable')#, hue='variable')
   bp.figure.savefig('swarm.png')

def main():
   print('Reading ...')
   #df = pd.read_csv('sarah_plot.csv')
   df = pd.read_csv('baderua_with_avarege.csv')

   print('Melting ...')
   df = pd.melt(df, id_vars=['atom', 'resid'])
   #df['value'] = df['value'].str.replace(',', '.').astype(float)

   print('Plotting ...')
   boxplot(df)
   swarmplot(df)
   print('Done.')

if __name__ == '__main__':
	main()
