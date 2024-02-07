import streamlit as st
import pandas as pd

st.image("img/a2.jpeg")
st.header("การนำเสนอสถิติการเกิดอุบัติเหตุของประเทศไทย")

col1,col2=st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("25600")
with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("25600")

dt=pd.read_excel('data/DT01.xlsx')

st.write(dt.head(1))

NumM=dt[dt['Sex']=='หญิง'].count()
NumF=dt[dt['Sex']=='ชาย'].count()

dtSex=[NumM,NumF]
dtSexb=pd.DataFrame(dtSex)
st.bar_chart(dtSexb)