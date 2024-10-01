import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('ml-1m/users.dat',sep = '::',header=None,engine = 'python',names=unames)
rnames =['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('ml-1m/ratings.dat',sep = '::',header=None,engine = 'python',names=rnames)
mnames = ['movie_id','title','genres']
movies = pd.read_table('ml-1m/movies.dat',sep = '::',header = None, engine = 'python',names = mnames,encoding='latin-1')

data = pd.merge(pd.merge(ratings,users),movies)

mean_ratings = data.pivot_table('rating','title','gender',aggfunc='mean')
ratings_by_title = data.groupby('title').size()
#print(ratings_by_title[:10])
active_titles = ratings_by_title.index[ratings_by_title>=250]

top_female_ratings = mean_ratings.sort_values(by=['F'],ascending=False)
#print(top_female_ratings[:45])
mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by=['diff'])
#print(sorted_by_diff[:15])

rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.loc[active_titles]
#print(rating_std_by_title[:10])
rating_sort = rating_std_by_title.sort_values(ascending=False)[:10]
print(rating_sort)
