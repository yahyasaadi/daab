import streamlit as st
import pandas as pd
# import openpyxl
import numpy as np
from streamlit.components.v1 import html




st.set_page_config(page_title='Election Analysis',page_icon="chart_with_upwards_trend",)

st.title("2022 Election Data Analysis.")

col1, col2 = st.columns(2)

dfward = pd.read_excel("Book1.xlsx",sheet_name='Sheet2')

dfpoling=pd.read_excel("Book1.xlsx",sheet_name='df')

with st.form("my_form"):


	ward_select = col1.selectbox('Choose your ward',dfward)

	dfpolingFl = dfpoling[dfpoling['WARDS'].str.match(ward_select)]

	poling_select = col2.selectbox('Choose your poling station',dfpolingFl['POLING_STATION'])

	col3, col4,col5,col6,col7 = st.columns(5)

	regNo = col3.number_input("Registered Voters",min_value=0)
	rejVotes = col4.number_input("Rejected Voters",min_value=0)
	desValues = col5.number_input("Desputed Votes",min_value=0)
	valid = col6.number_input("Valid Votes Casted",min_value=0)
	###waiting for confirmation
	rejOb = col7.number_input("Rejection Objected",min_value=0)
	st.markdown(" ")
	st.markdown(" ")



	st.subheader("Data for Candidates.")
	col8, col9, col10 = st.columns(3)

	hon_Farah = col8.number_input("Hon Farah Maalim", min_value=0)
	kheyrow = col9.number_input("Kheyrow", min_value=0)
	a_Issack = col10.number_input("Ahmed Issack", min_value=0)
	st.markdown('')
	st.markdown('')

	submitted = st.form_submit_button("Submit")
	if submitted:
		dfup = pd.read_excel("Book3.xlsx",sheet_name='general')
		regNo >= (rejVotes + desValues+ valid +rejOb )
		valid == (hon_Farah+kheyrow+a_Issack)
		infoo = [ward_select,poling_select, regNo, rejVotes, desValues, valid , rejOb, hon_Farah, kheyrow, a_Issack]

		# path = 'Book3.xlsx'
		columns = ['ward','poling','Registered','Rejected','Desputed','Valid','Rejection', 'hon_Farah', 'kheyrow', 'a_Issack']
		df = pd.DataFrame([infoo],columns=columns)
		df2 = pd.read_excel("dday.xlsx",sheet_name='general')



		# dfcad = pd.read_excel("dday.xlsx",sheet_name='Sheet1')
		# column2 = ['CANDIDATES','VOTES']
		# dfyahya = pd.DataFrame(,columns=columns2)



		
		frames = [df, df2]
		result = pd.concat(frames)
		# result = str(result)
		# result = result.reset_index()
		# st.write(result)

		
		myerror ="""
		
			alert('Error Occured!');
		
		"""
		my_html = f"<script>{myerror}</script>"
		##saving logics
		if (regNo >= (rejVotes + desValues+ valid +rejOb )) & (valid == (hon_Farah+kheyrow+a_Issack)):
			writer = pd.ExcelWriter("dday.xlsx", engine='xlsxwriter')
			result.to_excel(writer,sheet_name = 'general', index=False)
			writer.save()
			writer.close()
		else:
			html(my_html) 

			refresh = """
				if ( window.history.replaceState ) {
	        		window.history.replaceState( null, null, window.location.href );
	    		}
			"""
			my_html1 = f"<script>{refresh}</script>"
			html(my_html1)

footer="""
 <style>
 @import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@700&display=swap');
 .css-12ttj6m{
 border:none;
 }
 .css-1cpxqw2{
 background-color:#17A2B8;
 color:#fff;
 }
 .css-1cpxqw2:hover{
 background-color:#fff;
 color:skyblue;
 border:1px solid #17A2B8;
 }
 .css-10trblm{
 text-align:center;
 font-family: 'Cormorant SC', serif;
 margin-bottom:34px;
 margin-top:-35px;
 background-color:#000;
 color:#fff;
 }
 </style>
 """
st.markdown(footer,unsafe_allow_html=True) 