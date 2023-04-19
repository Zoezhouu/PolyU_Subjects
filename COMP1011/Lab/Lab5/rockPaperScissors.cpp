#include <iostream>
#include <time.h>

using namespace std;

char decideWhoWins(int comp, int human) {
	if (comp == human) {
		return 'd';
	}
	else if ((comp == 2 && human == 1) || (comp == 3 && human == 2) || (comp == 1 && human == 3)) {
		return 'c';
	}
	return 'h';
}

int main() {

	srand(time(0));
	int compChoice = rand() % 3 + 1;
	int humanChoice;
	char yesNo;

	do {
		do {
			cout << "Please choose Rock (1), Paper (2) or Scissors (3): ";
			cin >> humanChoice;
		} while (!(humanChoice == 1 || humanChoice == 2 || humanChoice == 3));

		cout << "Computer throws " << ((compChoice == 1) ? "Rock" : (compChoice == 2) ? "Paper" : "Scissors") << "." << endl;
		char decision = decideWhoWins(compChoice, humanChoice);
		if (decision == 'c') {
			cout << "Computer Wins." << endl;
		}
		else if (decision == 'h') {
			cout << "You Win." << endl;
		}
		else {
			cout << "Draw." << endl;
		}

		do {
			cout << "Play again? (Y/N): ";
			cin >> yesNo;
		} while (!(yesNo == 'y' || yesNo == 'Y' || yesNo == 'n' || yesNo == 'N'));

	} while (yesNo == 'Y' || yesNo == 'y');

	cout << "Thanks for playing!" << endl;

	return 0;
}
