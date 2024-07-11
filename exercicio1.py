import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pingouin as pg
import plotly.express as px 
import plotly.io as pio
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from scipy.stats import chi2_contingency
import statsmodels.api as sm
import plotly.graph_objects as go
pio.renderers.default='browser'

# importação de banco de dados
dados_pisa = pd.read_csv('./bancos_dados/notas_pisa.csv', delimiter=';')

