#include <iostream>
#ifdef _WIN32
  #include<windows.h>
#endif  

void clear()
{
  #ifdef _WIN32
    system("cls");
  #else
    system("clear");
  #endif
}

using namespace std;

/**
 * A structure called PC is defined, which
 * will be performing 'analysis' to play.
 */
struct pc {
    int rock = 0, paper = 0, scissors = 0;
};

int main() {

    char ans;

    int pcOption    = 0,
        userOption  = 0,
        playerScore = 0,
        pcScore     = 0,
        playedGames = 0,
        tiedGames   = 0;

    pc computer;

    /**
     * Iterator cycle that will be running as many
     * times as you want to play against the PC.
     */
    do {

        cout << "\nLet's play 'ROCK, PAPER or SCISSORS'" << endl;

        /**
         * Iterator cycle that verifies the player's response.
         */
        do {

            cout << "\nWhat is your choice?\n(1) ROCK\n(2) PAPER\n(3) SCISSORS\nEnter your choice: ";
            cin >> userOption;

            /**
             * If the player's answer is incorrect,
             * a message is displayed and the cycle is repeated.
             */
            if (userOption != 1 && userOption != 2 && userOption != 3) {
                clear();
                cout << "\nYou have entered an invalid option. Please re-enter your choice." << endl;
            }

        } while (userOption != 1 && userOption != 2 && userOption != 3);

        /**
         * If not previously played, the PC makes a random choice.
         */
        if (computer.rock == 0 && computer.paper == 0 && computer.scissors == 0)
            pcOption = rand() % 3;

            /**
             * If previously played, the PC will make a choice
             * based on an analysis of previous games.
             */
        else {

            int size = computer.rock + computer.paper + computer.scissors;
            int pcChoices[size];
            int index = 0;

            while (index < size) {

                for (int i = 0; i < computer.rock; i++) {
                    pcChoices[index] = 1;
                    index++;
                }
                for (int i = 0; i < computer.paper; i++) {
                    pcChoices[index] = 2;
                    index++;
                }
                for (int i = 0; i < computer.scissors; i++) {
                    pcChoices[index] = 3;
                    index++;
                }

            }

            pcOption = pcChoices[rand() % size];

        }

        /**
         * Comparisons are made to define the winner and loser.
         * In addition, the PC learns from the game and
         * the choices made by both the player and the PC.
         */
        if (pcOption == 1 && userOption == 1) {
            cout << "\nTie! You and the PC have chosen Rock." << endl;
            computer.paper++;
            tiedGames++;
        }
        if (pcOption == 2 && userOption == 2) {
            cout << "\nTie! You and the PC have chosen Paper." << endl;
            computer.scissors++;
            tiedGames++;
        }
        if (pcOption == 3 && userOption == 3) {
            cout << "\nTie! You and the PC have chosen Scissors." << endl;
            computer.rock++;
            tiedGames++;
        }
        if (pcOption == 1 && userOption == 2) {
            cout << "\nYou won! The PC has chosen Rock and you chose Paper." << endl;
            computer.scissors += 3;
            computer.paper++;
            computer.rock -= 3;
            playerScore++;
        }
        if (pcOption == 1 && userOption == 3) {
            cout << "\nYou lose! The PC has chosen Rock and you have chosen Scissors." << endl;
            computer.rock += 3;
            computer.scissors++;
            computer.paper -= 3;
            pcScore++;
        }
        if (pcOption == 2 && userOption == 3) {
            cout << "\nYou won! The PC has chosen Paper and you have chosen Scissors." << endl;
            computer.rock += 3;
            computer.scissors++;
            computer.paper -= 3;
            playerScore++;
        }
        if (pcOption == 3 && userOption == 2) {
            cout << "\nYou lose! The PC has chosen Scissors and you have chosen Paper." << endl;
            computer.scissors += 3;
            computer.paper++;
            computer.rock -= 3;
            pcScore++;
        }
        if (pcOption == 2 && userOption == 1) {
            cout << "\nYou lose! The PC has chosen Paper and you have chosen Rock." << endl;
            computer.paper += 3;
            computer.scissors++;
            computer.rock -= 3;
            pcScore++;
        }
        if (pcOption == 3 && userOption == 1) {
            cout << "\nYou won! The PC has chosen Scissors and you have chosen Rock." << endl;
            computer.paper += 3;
            computer.rock++;
            computer.scissors -= 3;
            playerScore++;
        }

        playedGames++;

        /**
         * Results are displayed.
         */
        cout<< "\n - PC Score = "   << pcScore 
            << " - Your Score = "   << playerScore 
            << " - Played games: "  << playedGames 
            << " - Tied games: "    << tiedGames
            <<endl;

        /**
         * Cycle iterator to know if the player wants to play again.
         */
        do {

            cout << "\nDo you want to continue playing? \n(0) Yes\n(1) No\nEnter your choice: ";
            cin >> ans;
            /**
             * If the player's answer is incorrect,
             * a message is displayed and the cycle is repeated.
             */
            if (ans != '0' && ans != '1') {
                clear();
                cout << "\nYou have entered an invalid option. Please re-enter your choice." << endl;
            } else
                clear();

        } while (ans != '0' && ans != '1'); 

    } while (ans == '0');

    return 0;

}
