#include <iostream>
#include <cstdlib> 
#include <ctime>   

using namespace std;

int main() {

    srand(time(nullptr));

    int randomNumber = rand() % 100 + 1;

    int guess;
    bool guessedCorrectly = false;
    cout<<"WELCOME TO THE NUMBER GAME FROM CODSOFT"<<endl;
    cout<<endl;
    while (!guessedCorrectly) {

        cout << "Guess the number (between 1 and 100): ";
        cin >> guess;

        if (guess == randomNumber) {
            cout << "Congratulations! You guessed the correct number.\n";
            guessedCorrectly = true;
        } else if (guess < randomNumber) {
            cout << "Too low! Try again.\n";
        } else {
            cout << "Too high! Try again.\n";
        }
    }

    return 0;
}
