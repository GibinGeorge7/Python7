
import pandas

df1=pandas.DataFrame([[4,5,6],[10,11,12],[20,31,42]],columns=["Price","Age","Load"],index=["data1","data2","data3"])
print(df1)
print ("test\n")
print(df1.Price.sum())
print(df1.Price.max())
