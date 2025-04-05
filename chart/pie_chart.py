import matplotlib.pyplot as plt

categories = ['Router','Firewall','L2Switch','L3 Switch','Proxy']
values = [50,60,30,40,25]
plt.pie(values,labels=categories,autopct='%1.1f%%')
plt.title("Produt Stauts Pi Chart")
plt.show()
