#include <iostream>
#include <cstring>

using namespace std;

struct MovieType
{
    char Movie_Name[20];
    char Movie_Director[20];
    char producer[20];
    int released_year;
    int num_copies;
};

void user_input_call_by_reference(MovieType &);
void print_info(MovieType &);

int main()
{

    MovieType this_movie;

    user_input_call_by_reference(this_movie);
    print_info(this_movie);

    return 0;
}

void user_input_call_by_reference(MovieType &movie)
{
    char Movie_Name[20];
    char Movie_Director[20];
    char producer[20];

    cout << "Please enter the Movie_Name: ";
    cin >> Movie_Name;
    strcpy(movie.Movie_Name, Movie_Name);

    cout << "Please enter the Movie_Director: ";
    cin >> Movie_Director;
    strcpy(movie.Movie_Director, Movie_Director);

    cout << "Please enter the producer: ";
    cin >> producer;
    strcpy(movie.producer, producer);

    cout << "Please enter the released_year: ";
    cin >> movie.released_year;

    cout << "Please enter the num_copies in stocks: ";
    cin >> movie.num_copies;
}

void print_info(MovieType &movie)
{
    cout << "Movie_Name:" << movie.Movie_Name << endl;
    cout << "Movie_Director:" << movie.Movie_Director << endl;
    cout << "Movie_Producer:" << movie.producer << endl;
    cout << "released_year:" << movie.released_year << endl;
    cout << "num_copies:" << movie.num_copies << endl;
}