import pandas as pd
import streamlit as st
from database import disp_query

def query():
	query = st.text_input("Query:")
	if st.button("Run Query"):
		result=disp_query(query)
		st.success("Query run successfully")
		df = pd.DataFrame(result)
		with st.expander("Current data"):
			st.dataframe(df)
	