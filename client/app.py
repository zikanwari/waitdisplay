import streamlit as st
import requests as r
import influxdb_client, os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "lp-cloud"
url = "http://10.0.0.2:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="congestion"

write_api = write_client.write_api(write_options=SYNCHRONOUS)


st.title('manage page')

with st.form(key='form'):
    username = st.text_input('表示させる文章')
    submit_button = st.form_submit_button(label='送信')

if submit_button:
    response = r.get(f'https://api.launchpencil.f5.si/zikanwari/?user={username}')
    if response.status_code == 200:

        st.info(response.text)
        
    else:
        # エラーが発生した場合はエラーメッセージを表示する
        st.error(response.status_code)

if st.button('とても混んでいる(100%)'):
    point = (
    Point("congestion")
    .tag("tagname1", "tagvalue1")
    .field("field1", 100)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)

if st.button('混んでいる(75%)'):
    point = (
    Point("congestion")
    .tag("tagname1", "tagvalue1")
    .field("field1", 75)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)

if st.button('普通(50%)'):
    point = (
    Point("congestion")
    .tag("tagname1", "tagvalue1")
    .field("field1", 50)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)

if st.button('空いている(0%)'):
    point = (
    Point("congestion")
    .tag("tagname1", "tagvalue1")
    .field("field1", 0)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)