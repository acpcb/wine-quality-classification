import pandas as pd

def create_target(df):
    df=df.copy(); df['high_quality']=(df['quality']>=7).astype(int); return df

def add_features(df):
    df=df.copy(); df['bound_sulfur_dioxide']=df['total sulfur dioxide']-df['free sulfur dioxide']; df['free_sulfur_ratio']=df['free sulfur dioxide']/(df['total sulfur dioxide']+1e-6); df['acidity_ratio']=df['fixed acidity']/(df['volatile acidity']+1e-6); df['alcohol_density_ratio']=df['alcohol']/(df['density']+1e-6); return df
