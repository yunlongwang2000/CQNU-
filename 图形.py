import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

data = pd.read_excel('data.xlsx')
print(data)


# 绘制折线图
def huazhexiantu(x, y, z):
    plt.figure()
    plt.plot(data[x], data[y])
    plt.title(z)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.savefig(z)

def hua_sandian(x, y, z):
    plt.figure()
    plt.scatter(data[x], data[y])
    plt.title(z)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.savefig(z)

def hua_3Dsabdian(x,y,z,name):
    fig=plt.figure()
    ax = Axes3D(fig)
    ax.scatter(data[x], data[y], data[z], c='r')
    plt.xlabel(x)
    plt.ylabel(y, rotation=38)  # y 轴名称旋转 38 度
    ax.set_zlabel(z)  # 因为 plt 不能设置 z 轴坐标轴名称，所以这里只能用 ax 轴来设置（当然，x 轴和 y 轴的坐标轴名称也可以用 ax 设置）
    plt.savefig(name, bbox_inches='tight', dpi=2400)  # 保存图片，如果不设置 bbox_inches='tight'，保存的图片有可能显示不全

huazhexiantu('日期', '平均气温（°C）', '2013年12月至2021年6月日平均气温')
plt.show()

huazhexiantu('日期', '累计降水量(mm)', '2013年12月至2021年6月日累计降水量')
plt.show()

huazhexiantu('日期', 'AQI', '2013年12月至2021年6月AQI')
plt.show()

hua_sandian('平均气温（°C）','AQI','平均气温与AQI')
plt.show()

hua_sandian('累计降水量(mm)','AQI','降水量与AQI')
plt.show()

hua_sandian('平均气温（°C）','质量等级','平均气温与空气质量')
plt.show()

hua_sandian('累计降水量(mm)','质量等级','降水量与空气质量')
plt.show()

hua_sandian('平均风速（m/s）','质量等级','风速与空气质量')
plt.show()

hua_sandian('平均气压(hPa)','质量等级','气压与空气质量')
plt.show()

hua_sandian('平均相对湿度(1%)','质量等级','相对湿度与空气质量')
plt.show()

hua_3Dsabdian('平均气温（°C）','累计降水量(mm)','AQI','气温、降水量与AQI的关系')
plt.show()

hua_3Dsabdian('平均气温（°C）','累计降水量(mm)','质量等级','气温、降水量与空气质量的关系')
plt.show()