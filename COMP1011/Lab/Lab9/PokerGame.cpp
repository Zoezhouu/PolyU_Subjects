#include <time.h>
#include <iostream>

using namespace std;

struct Card
{
    int rank; // 1~13, A->2~10->J->Q->K
    int face; // 0~3, D->C->H->S
};

// Function Prototypes
void genGards(Card *);
bool isStraightHand(Card *);
void printCardShort(Card);
void sortCards(Card[], int);

int main(void)
{
    Card cards[5];

    // Prepare random seed
    srand(time(NULL));

    // Generate cards
    genGards(cards);

    /*
    For testing the special case
    cards[0].rank = 1;
    cards[1].rank = 10;
    cards[2].rank = 11;
    cards[3].rank = 13;
    cards[4].rank = 12;
    */

    // Sort the cards based on rank
    sortCards(cards, 5);

    // Print the cards
    for (int i = 0; i < 5; i++)
    {
        printCardShort(cards[i]);
        cout << " ";
    }

    // Print the status
    if (isStraightHand(cards))
    {
        cout << "forms a straight hand.";
    }
    else
    {
        cout << "does not form a straight hand.";
    }

    return 0;
}

void genGards(Card *cards)
{
    Card tempcard;
    int DrawnCards = 0;
    bool Duplicate = false;

    while (DrawnCards < 5)
    {
        tempcard.rank = rand() % 13 + 1;
        tempcard.face = rand() % 4;

        // Check if Duplicate
        Duplicate = false;
        for (int i = 0; i < DrawnCards; i++)
        {
            if (cards[i].rank == tempcard.rank)
            {
                if (cards[i].face == tempcard.face)
                {
                    Duplicate = true;
                }
            }
        }

        // Add the card into the array if not duplicate
        if (!Duplicate)
        {
            cards[DrawnCards].rank = tempcard.rank;
            cards[DrawnCards].face = tempcard.face;
            DrawnCards++;
        }
    }
    // Note: Another approach is to eliminate the drawn card(s) to make sure
    // no duplicate is found in the subsequence draws. It leaves another exercise for you.
}

bool isStraightHand(Card *cards)
{
    int SpecialStraight[5] = {1, 10, 11, 12, 13};
    bool SimpleConsecutive = true;  // Direct Straight
    bool SpecialConsecutive = true; // A 10 J Q K

    // Check if simple consecutive
    // NOTE: face is ignored in a straight, so not checked
    for (int i = 0; i < 4; i++)
    {
        // Check if simple consecutive
        if (cards[i].rank + 1 != cards[i + 1].rank)
        {
            SimpleConsecutive = false;
        }
    }

    // Check if special consecutive
    // NOTE: face is ignored in a straight, so not checked
    for (int i = 0; i < 5; i++)
    {
        if (cards[i].rank != SpecialStraight[i])
        {
            SpecialConsecutive = false;
        }
    }

    return SimpleConsecutive || SpecialConsecutive;
}

void printCardShort(Card card)
{
    // Rank
    switch (card.rank)
    {
    case 1:
        cout << "A";
        break;
    case 11:
        cout << "J";
        break;
    case 12:
        cout << "Q";
        break;
    case 13:
        cout << "K";
        break;

    default:
        cout << card.rank;
        break;
    }

    // Face
    switch (card.face)
    {
    case 0:
        cout << "D";
        break;
    case 1:
        cout << "C";
        break;
    case 2:
        cout << "H";
        break;
    case 3:
        cout << "S";
        break;
    }

    return;
}

void sortCards(Card cards[], int size)
{
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - 1; j++)
        {
            if (cards[j].rank > cards[j + 1].rank)
            {
                Card temp = cards[j];
                cards[j] = cards[j + 1];
                cards[j + 1] = temp;
            }
        }
    }
}