import matplotlib.pyplot as plt
a= ["A", "B", "C", "D"]
b = [1, 2, 3, 4]
plt.barh(a,b)
for index, value in enumerate(b):
    plt.text(value,index,str(value))
plt.show()
 