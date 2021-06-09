movie_available = True
have_money = False

get_excited = movie_available | have_money
print(get_excited)


buy = movie_available & have_money
print(buy)
