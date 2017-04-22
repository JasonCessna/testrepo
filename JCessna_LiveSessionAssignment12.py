
# coding: utf-8

# In[18]:

my_list = [45.4,44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
print my_list[4]
my_list.append(55.2)
del my_list[5]
for i in range(len(my_list)):
   if my_list[i] > 45:
    print my_list[i]


# In[54]:

import numpy
numpArray = numpy.array(my_list)
print 'numpy mean of numpArray: ',numpy.mean(numpArray), '\nnumpy standard deviation of numpArray: ',numpy.std(numpArray)
for i in range(len(numpArray)):
    if numpArray[i] < 45:
        print numpArray[i]
print 'numpy min of numpArray: ', numpy.min(numpArray), 'numpy max of numpArray: ', numpy.max(numpArray)


# In[78]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import pandas

iris = pandas.read_csv("IRIS.csv")
print iris.head()

iris.drop('Id', axis=1)
iris_setosa = iris[iris.Species == 'Iris-setosa']
print iris_setosa.describe()

print iris.groupby('Species').describe()
iris.boxplot(by='Species')

import seaborn as sns
sns.pairplot(iris,hue='Species')



# In[ ]:




# In[ ]:



