import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_detail = pd.DataFrame({
    'student' : ['usman', 'ali', 'ahmad', 'jawad',  'khan'],
    'marks' : [89, 56, 76, 92, 67]
})

sns.lineplot(x = 'student', y = 'marks', data = student_detail, marker = 'o')
plt.show()



