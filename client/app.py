import streamlit as st
import requests as r
import influxdb_client, os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("token")
org = "lp-cloud"
url = "http://10.0.0.2:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="zikanwari"

write_api = write_client.write_api(write_options=SYNCHRONOUS)


st.title('manage page')

with st.form(key='form'):
    message_text = st.text_input('表示させる文章')
    submit_button = st.form_submit_button(label='送信')

if submit_button:
    point = (
    Point("congestion")
    .field("message", message_text + ",")
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)

if st.button('とても混んでいる(100%)'):
    point = (
    Point("congestion")
    .field("percentage", 100)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)

if st.button('混んでいる(75%)'):
    point = (
    Point("congestion")
    .field("percentage", 75)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)

if st.button('普通(50%)'):
    point = (
    Point("congestion")
    .field("percentage", 50)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)

if st.button('空いている(25%)'):
    point = (
    Point("congestion")
    .field("percentage", 25)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)

if st.button('整備中(0%)'):
    point = (
    Point("congestion")
    .field("percentage", 0)
    )
    write_api.write(bucket=bucket, org="lp-cloud", record=point)