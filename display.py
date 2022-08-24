import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df= pd.read_excel('dday.xlsx',sheet_name='general')
total_valid =df['Valid'].sum()

st.set_page_config(page_title='Dadaab Consituency Election',page_icon='fm.png')
st.title("Dadaab MP Seat Race")
raiseheader = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Uchen&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,700;0,800;1,400;1,800&display=swap');
.css-10trblm{
	margin-top: -115px;
}
.css-znku1x{
	text-align:center;
}
.css-znku1x p{
	margin:-5px;
	padding-left:-15px;
	
	font-family: 'Open Sans', sans-serif;
}

</style>
"""
st.markdown(raiseheader,unsafe_allow_html=True)


votes4f=df['hon_Farah'].sum()
votes4k=df['kheyrow'].sum()
votes4i=df['a_Issack'].sum()



farah,kheyrow,issack = st.columns(3)
farah1,kheyrow1,issack1 = st.columns(3)

# farah, farah1, kheyrow, kheyrow1, issack, issack1 = st.columns(6)

def calculate(vote4each):
	percentage_f = (vote4each/total_valid) * 100
	return percentage_f

farah.image('fm.png')
farah1.write(f"Total Votes: {votes4f}")

farah1.write('Total Percentage: {:.2f}%'.format(calculate(votes4f)))


kheyrow.image('kherow.png')
kheyrow1.write(f"Total Votes: {votes4k}")

kheyrow1.write('Total Percentage: {:.2f}%'.format(calculate(votes4k)))


issack.image('issack1.png')
issack1.write(f"Total Votes: {votes4i}")
issack1.write('Total Percentage: {:.2f}%'.format(calculate(votes4i)))

# if votes4f > (total_valid/2):
# 	farah1.write(f'You leading with {votes4f-(votes4k+votes4i)} ')
# else:


checkvotes = [votes4i,votes4k,votes4f]

hv=np.max(checkvotes)
hv5=np.min(checkvotes)


if hv == votes4f:

	checkvote1 = [votes4i,votes4k]
	hv1=np.max(checkvote1)

	farah1.write(f"You are ahead by : {votes4f-hv1} votes")

elif hv == votes4k:
	checkvote1 = [votes4i,votes4f]
	hv1=np.max(checkvote1)
	kheyrow1.write(f"You are ahead by: {votes4k-hv1} votes")
else:
	checkvote1 = [votes4f,votes4k]
	hv1=np.max(checkvote1)
	issack1.write(f"You are ahead by: {votes4i-hv1} votes")
column9 =['ISSACK','KHEYROW','FARAH']
dfpi = pd.DataFrame([checkvotes],columns=column9)
yah1, yah2 = st.columns(2)
pie_chart = px.pie(dfpi, title = "Votes for Each Candidate", values=checkvotes,names=column9)
# yah1.plotly_chart(pie_chart)
data = [['FARAH',votes4f],['KHEYROW',votes4k],['ISSACK',votes4i]]
yahya = pd.DataFrame(data,columns=['Candidate','Votes'] )
yahya= yahya.sort_values(by='Votes', ascending=True)
bar_chart = px.bar(yahya,
                    x='Votes',
                    y='Candidate',
                    text='Votes',
                    orientation='h',
                    color_discrete_sequence = ['#F63366'],
                    template='plotly_white')
st.plotly_chart(bar_chart)
