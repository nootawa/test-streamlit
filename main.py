import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('Show Progress bar ')
'Start'
latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

#st.write('DataFrame')

#st.write('Display Image')

# st.write('Interactive Widgets')
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
#     )

# 'あなたの好きな数字は、',option, 'です。'


# st.write('Interactive Widgets')
# text = st.text_input('あなたの趣味を教えてください')
# 'わたしの趣味：',text,

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション',condition


# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'わたしの趣味：',text,
# 'コンディション',condition,

# st.write('Interactive Widgets')

# left_column, right_column = st.columns(2) #beta_columnだとエラーになるので、columsに変更 
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expender1 = st.expander('問い合わせ1') #beta_をつけるとエラーになるようなので、適宜修正が必要
# expender1.write('問い合わせ内容をここに書く')
# expender2 = st.expander('問い合わせ2') 
# expender2.write('問い合わせ内容をここに書く')
# expender3 = st.expander('問い合わせ3') 
# expender3.write('問い合わせ内容をここに書く')



# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'わたしの趣味：',text,
# 'コンディション',condition,

# if st.checkbox('Show Image'):
#     img = Image.open('def_0_6184.jpeg')
#     st.image(img, caption='画像', use_column_width=True)

# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

#st.write(df)
#st.dataframe(df, width=100, height=100)
#st.dataframe(df.style.highlight_max(axis=0))#, width=100, height=100)
#st.table(df.style.highlight_max(axis=0))


#"""
# 章
## 節
### 項
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

# df1 = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(df1)
# st.area_chart(df1)
# st.bar_chart(df1)

# df2 = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df2)