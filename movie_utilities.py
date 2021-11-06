"""
-------------------------------------------------------
movie_utilities.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-09-13"
-------------------------------------------------------

"""

from movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Postconditions:
        returns
        movie - a completed movie object (Movie).
    -------------------------------------------------------
    """
    
    title = input("Title: ")
    year = int(input("Year: "))
    director = input("Director: ")
    rating = float(input("Raing: "))
    menu()
    genres = read_genres()
    movie = Movie(title, year, director, rating, genres)
    
           
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Preconditions:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Postconditions:
        returns
        movie - contains the data from line (Movie)
    -------------------------------------------------------
    """

    component = line.split("|")
    
    temp = component[4].split(",")
    
    i=0
    
    while i < len(temp):
        temp[i] = int(temp[i])
        i = i +1
        
    
    genres = []
    
    for i in temp:
        
        genres.append(i)
        
    movie=Movie(str(component[0]),int(component[1]),str(component[2]),float(component[3]),genres)
        
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of movie objects into a list.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Preconditions:
        fv - a already open file of movie data (file)
    Postconditions:
        returns
        movies - a list of movie objects (list of Movie)
    -------------------------------------------------------
    """
    movies=[]
    for line in fv:
        #line=file_variable.readline()
        movie=read_movie(line)
        movies.append(movie)
        
    return movies


def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Postconditions:
        Menu of genres is printed.
    -------------------------------------------------------
    """
    print("Genres")
    for i in range(len(Movie.GENRES)):
        print(" {} {}".format(i,Movie.GENRES[i]))
        
    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Postconditions:
        returns
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    genres = []
    x = input("Enter a genre number (ENTER to quit):")
    
    while x != "" or genres == []:
                
        if not x.isdigit():
            print("Error: not a positive number.")
        else:
            y = int(x)
            
            if y in genres:
                print("Error: genre already chosen")
                
            elif y not in Movie.GENRE_CODES:
                print("Error: input must be < 10")
        
            else:
                genres.append(y)
            
        x = input("Enter a genre number (ENTER to quit):")
        
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Preconditions:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Postconditions:
        fv contains the contents of movies
    -------------------------------------------------------
    """

# Your code here        
        
    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Postconditions:
        returns
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    for i in range(len(movies)):
        if movies[i].year == year:
            ymovies.append(movies[i])
        
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Postconditions:
        returns
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    rmovies = []
    for i in range(len(movies)):
        if movies[i].rating == rating:
            rmovies.append(movies[i])    
        
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Postconditions:
        returns
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    for i in range(len(movies)):
        if genre in movies[i].genres:
            gmovies.append(movies[i])    
        
    return gmovies      
        

def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Postconditions:
        returns
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    length = len(genres)
    n=0
    for i in range(len(movies)):
        for x in genres:
            if x in movies[i].genres:
                n = n + 1
        if n == length and len(movies[i].genres) == length:
            gmovies.append(movies[i])  
        
        n=0
    return gmovies

def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
    Postconditions:
        returns
        counts - the number of movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = []
    counter=0
    
    for i in range(len(Movie.GENRES)):
        for movie in movies:
            if i in movie.genres:
                counter = counter + 1
        
        counts.append(counter)
        counter = 0        
    
    return counts