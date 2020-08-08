import pandas as pd

import plotly.express as px

cd = pd.read_csv("data - data.csv")

fig  =   px.line(cd, x="Date" ,  y="Cases"  ,color="Country" ,  title="No. of cases")

fig.show()