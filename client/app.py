import streamlit as st
import requests as r

st.title('hello world!')

with st.form(key='login_form'):
    username = st.text_input('ユーザー名')
    password = st.text_input('パスワード', type='password')
    submit_button = st.form_submit_button(label='ログイン')

if submit_button:
    response = r.get(f'https://api.launchpencil.f5.si/zikanwari/?user={username}&pass={password}')
    if response.status_code == 200:
        
        a = response.text.split(',')

        if a[0] == 'エラー':
            if str(a[1]).startswith("Access denied for user"):
                st.error('認証に失敗しました。ユーザー名またはパスワードが間違っているか設定されていません。')
            else:
                st.error(a[1])
            st.stop()

        table_data = [[0 for j in range(5)] for i in range(7)]
        table_data[1][2] = 5

        for i in range(0, 35):
            table_data[i//5][i%5] = a[i]

        st.table(table_data)
    else:
        # エラーが発生した場合はエラーメッセージを表示する
        st.error(response.status_code)