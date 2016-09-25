import panda as pd

d = {'one' : [1., 2., 3., 4.],
     'two' : [4., 3., 2., 1.]}

df = pd.DataFrame(d, index=['a', 'b', 'c', 'd'])

print(df)
