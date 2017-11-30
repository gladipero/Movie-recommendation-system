import pandas as pd
import graphlab


print "Welcome  to Movie recommendation system \n"
print "Made by : \n"
print "Amar shishodia  9915103078 \n"
print "Dhruv Sharma     9915103082 \n "
print "Omanshi Rastogi \n"
print "Alisha Chopra \n"
print "Press 1 to get the most popular recommendation on the basis of the training data set"
print "Press 2 to get the recommendations for Amar User profile created "
switch_var = input()
print "Training recommendation engine. Please wait"


# pass in column names for each CSV and read them using pandas. 
# Column names available in the readme file

#Reading users file:
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols,
 encoding='latin-1')

#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
 encoding='latin-1')

#Reading items file:
i_cols = ['movie_id', 'movie_title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,
 encoding='latin-1')

#Users


users.head()
items.head()
#print items.values[10][1]



r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp', 'movie_title']
ratings_base = pd.read_csv('ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')
#ratings_base.shape, ratings_test.shape

#print "rating_tes start"
#print ratings_test
#print 'ratings end'
train_data = graphlab.SFrame(ratings_base)
test_data = graphlab.SFrame(ratings_test)

#Train Model
item_sim_model = graphlab.item_similarity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating', similarity_type='pearson' )
#print "whaaaaaaaaaaat"


#Make Recommendations:

if switch_var == 1:
    #print "Yo"
    name = raw_input("\n Please enter your name: ")
    item_sim_recomm = item_sim_model.recommend()
    print "Name of the movie ",name," might like ",items.values[item_sim_recomm['movie_id'][0]][1],"Released on : ",items.values[item_sim_recomm['movie_id'][0]][2],"\n"
    print "IMDB link",items.values[item_sim_recomm['movie_id'][0]][4]
else:
    #print "wtf"
    item_sim_recomm = item_sim_model.recommend(users=['0'],k=1)
    print "Name of the movies Amar might like ",items.values[item_sim_recomm['movie_id'][0]][1],"Released on : ",items.values[item_sim_recomm['movie_id'][0]][2],"\n"
    print "IMDB link",items.values[item_sim_recomm['movie_id'][0]][4]
    
#item_sim_recomm.print_rows(num_rows=1)       


#print item_sim_recomm['movie_id'][0]

#print "Name of the movie user might like ",items.values[item_sim_recomm['movie_id'][0]][1]

