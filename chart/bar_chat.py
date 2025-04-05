import matplotlib.pyplot as plt

categories = ['Router','Firewall','L2Switch','L3 Switch','Proxy']
values = [50,60,30,40,25]
plt.bar(categories,values)
plt.title("Produt Stauts")
plt.xlabel("Categories")
plt.ylabel("Amount")
plt.show()