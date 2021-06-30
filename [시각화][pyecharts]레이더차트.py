!pip install pyecharts
!pip install wheel
!pip install pyecharts==0.1.9.4

# 코렙 한글폰트 적용
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

!apt -qq -y install fonts-nanum > /dev/null
 
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
 
fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=10)
fm._rebuild()
 
# 그래프에 retina display 적용
%config InlineBackend.figure_format = 'retina'
 
# Colab 의 한글 폰트 설정
plt.rc('font', family='NanumBarunGothic')

from pyecharts import Radar
 
schema = [ 
    ("접근성", 6500), ("유동인구", 16000), ("매출지수", 30000), ("점포지수", 38000), ("소비인구", 52000), ("기상정보", 25000)]
CU = [[4300, 10000, 28000, 35000, 50000, 19000]]
K7 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar()
radar.config(schema)
radar.add("CU", CU, is_splitline=True, is_axisline_show=True)
radar.add("세븐일레븐", K7, label_color=["#4e79a7"], is_area_show=False)
#radar.show_config()
radar.render()
