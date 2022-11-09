// Initial imports
// to use printf
#include <stdio.h>
// to use new `array` instead of old ones 
#include <array>
// to use stack data structure
#include <stack>
// to precisely measure time spent on computation
#include <chrono>

// Predefined values
#define SIZE 9
#define BLANK 0

void printBoard(std::array<std::array<int, SIZE>, SIZE> board) {
    /**
     * Print out the board
     *
     * @param board two-dimensional array representing the board
     * @return none
     */

    printf("======================\n");
    for (int i = 0;  i < SIZE; i++) {
        printf("= ");
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] != BLANK) {
                printf("%d ", board[i][j]);
            } else {
                printf(". ");
            }
        }
        printf(" =\n");
    }
    printf("======================\n\n");
}

bool checkGuess(int y, int x, std::array<std::array<int, SIZE>, SIZE> board) {
    /**
     * Check if the value on the provided coordinate is correct
     *
     * As rules of Sudoku define that horizontal, vertiacal lines
     * and the inner 3x3 squere cannot contain two exact digits
     *
     * @param y coordinate
     * @param x coordinate
     * @param board two-dimensional array representing the board
     * @return whether the board is correct
     */

    // We use 3x10 array to use as a memory of the previously encountered values
    // it is faster to define one big array once than define 3 times small ones

    // Each array is 10 digits long to accomodate a blank value
    // pool of possible values from 1 to 9 and blank being 0
    // allows us to access array by the value
    // even though we don't care about 0s, it is cheaper to addres 
    // 10s element with a value of '9', than to trim it.

    // Initially all of the values are 0,
    // we add '1' to the value we access,
    // if it is more that '1', the board is not correct.
    std::array<std::array<int, SIZE + 1>, 3> values = {{
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    }};

    // Horizontal line is checked by iterating all of the xs in the provided y coordinate
    for (int i = 0; i < SIZE; i++) {
        if (board[y][i] != 0) {
            values[0][board[y][i]] += 1;
            if (values[0][board[y][i]] > 1) {
                return false;
            }
        }
    }
    // Vertical line is checked by iterating all of the ys in the provided x coordinate
    for (int i = 0; i < SIZE; i++) {
        if (board[i][x] != 0) {
            values[1][board[i][x]] += 1;
            if (values[1][board[i][x]] > 1) {
                return false;
            }
        }
    }
    // We find the boarders of the inner square and do the previously defined operations
    for (int i = y / 3 * 3; i < y / 3 * 3 + 3; i++) {
        for (int j = x / 3 * 3; j < x / 3 * 3 + 3; j++) {
            if (board[i][j] != 0) {
                values[2][board[i][j]] += 1;
                if (values[2][board[i][j]] > 1) {
                    return false;
                }
            }
        }
    }
    return true;
}


int findFirstBlank(std::array<std::array<int, SIZE>, SIZE> board) {
    /**
     * Get the first blank in the board
     * 
     * Iterates over the board returns y and x or -1 if no avaliable.
     * Returns in a specific format as it is way faster to do a couple of 
     * integer operation instead of using Tuples or Arrays.
     *
     * @param board two-dimensional array representing the board
     * @return integer that contains y (first digit in decimal representation) 
     * and x (second digit in decimal representation). If no blaks available, -1 is supplied
     */
    for (int y = 0; y < SIZE; y++) {
        for (int x = 0; x < SIZE; x++) {
            if (board[y][x] == BLANK) {
                return y * 10 + x;
            }
        }
    }
    return -1;
}

void solve(std::array<std::array<int, SIZE>, SIZE> board) {
    /**
     * Solves the Sudoku puzzle
     * 
     * Uses backtracking and utilizes stack data struckture
     * @param board two-dimensional array representing the board
     * @return none
     */

    // We print out the inintial board
    printBoard(board);

    // We declare utilized varibales
    int blank, blankX, blankY, iterations;
    std::stack<std::array<std::array<int, SIZE>, SIZE>> boardStack;
    std::array<std::array<int, SIZE>, SIZE> boardCandidate = board;
    std::array<std::array<int, SIZE>, SIZE> newBoardCandidate = board;

    // We push the provided board to the stack.
    boardStack.push(board);

    // We iterate over the stuck until it is empty
    // Or we find the solution
    while (!boardStack.empty()) {
        // We take the top element of the stack
        boardCandidate = boardStack.top();
        boardStack.pop();

        // We get the first element of the board we took
        blank = findFirstBlank(boardCandidate);

        // if it has a blank
        if (blank >= 0) {
            // We get y and x out of it
            blankY = blank / 10;
            blankX = blank % 10;

            // We iterate over the possible values (from 9 to 1)
            for (int possibleValue = SIZE; possibleValue >= 1; possibleValue--) {
                // We set the coordinates with the value
                boardCandidate[blankY][blankX] = possibleValue;
                
                // If the board is possible
                if (checkGuess(blankY, blankX, boardCandidate)) {
                    // We copy the board and push it to the stack
                    // There is the example of the advantage of using Array from STL
                    // As the assigment operator COPIES the assignee array
                    newBoardCandidate = boardCandidate;
                    boardStack.push(newBoardCandidate);
                    iterations++;
                }
            }
        // If no blanks
        // The board is solved
        } else {
            printBoard(newBoardCandidate);
            printf("Iterations: %d\n", iterations);
            return;
        }
    }
    printf("No solution\n");
}


int main() {
    // easy
    // std::array<std::array<int, SIZE>, SIZE> board = {{
    //     {5, 3, 0, 0, 7, 0, 0, 0, 0},
    //     {6, 0, 0, 1, 9, 5, 0, 0, 0},
    //     {0, 9, 8, 0, 0, 0, 0, 6, 0},
    //     {8, 0, 0, 0, 6, 0, 0, 0, 3},
    //     {4, 0, 0, 8, 0, 3, 0, 0, 1},
    //     {7, 0, 0, 0, 2, 0, 0, 0, 6},
    //     {0, 6, 0, 0, 0, 0, 2, 8, 0},
    //     {0, 0, 0, 4, 1, 9, 0, 0, 5},
    //     {0, 0, 0, 0, 8, 0, 0, 7, 9}
    // }};

    // medium
    // std::array<std::array<int, SIZE>, SIZE> board = {{
    //     {1, 0, 0, 0, 0, 7, 0, 9, 0},
    //     {0, 3, 0, 0, 2, 0, 0, 0, 8},
    //     {0, 0, 9, 6, 0, 0, 5, 0, 0},
    //     {0, 0, 5, 3, 0, 0, 9, 0, 0},
    //     {0, 1, 0, 0, 8, 0, 0, 0, 2},
    //     {6, 0, 0, 0, 0, 4, 0, 0, 0},
    //     {3, 0, 0, 0, 0, 0, 0, 1, 0},
    //     {0, 4, 0, 0, 0, 0, 0, 0, 7},
    //     {0, 0, 7, 0, 0, 0, 3, 0, 0},
    // }};

    // medium
    // std::array<std::array<int, SIZE>, SIZE> board = {{
    //     {0, 0, 0, 0, 0, 7, 0, 0, 9},
    //     {0, 4, 0, 0, 8, 1, 2, 0, 0},
    //     {0, 0, 0, 9, 0, 0, 0, 1, 0},
    //     {0, 0, 5, 3, 0, 0, 0, 7, 2},
    //     {2, 9, 3, 0, 0, 0, 0, 5, 0},
    //     {0, 0, 0, 0, 0, 5, 3, 0, 0},
    //     {8, 0, 0, 0, 2, 3, 0, 0, 0},
    //     {7, 0, 0, 0, 5, 0, 0, 4, 0},
    //     {5, 3, 1, 0, 7, 0, 0, 0, 0}
    // }};

    // hard
    // https://mumbaimirror.indiatimes.com/mumbai/other/worlds-toughest-sudoku-is-here-can-you-crack-it/articleshow/16045183.cms
    // std::array<std::array<int, SIZE>, SIZE> board = {{
    //     {0, 0, 5, 3, 0, 0, 0, 0, 0},
    //     {8, 0, 0, 0, 0, 0, 0, 2, 0},
    //     {0, 7, 0, 0, 1, 0, 5, 0, 0},
    //     {4, 0, 0, 0, 0, 5, 3, 0, 0},
    //     {0, 1, 0, 0, 7, 0, 0, 0, 6},
    //     {0, 0, 3, 2, 0, 0, 0, 8, 0},
    //     {0, 6, 0, 5, 0, 0, 0, 0, 9},
    //     {0, 0, 4, 0, 0, 0, 0, 3, 0},
    //     {0, 0, 0, 0, 0, 9, 7, 0, 0},
    // }};

    // hard
    // std::array<std::array<int, SIZE>, SIZE> board = {{
    //     {7, 0, 0, 0, 1, 0, 0, 0, 9},
    //     {0, 9, 2, 0, 0, 8, 0, 5, 0},
    //     {3, 0, 0, 2, 0, 0, 0, 0, 0},
    //     {9, 0, 0, 0, 0, 0, 0, 0, 0},
    //     {0, 0, 0, 0, 6, 0, 0, 0, 0},
    //     {0, 1, 4, 7, 0, 0, 0, 0, 0},
    //     {0, 0, 0, 0, 0, 7, 4, 0, 0},
    //     {0, 0, 3, 0, 0, 0, 0, 0, 0},
    //     {0, 2, 5, 4, 0, 0, 0, 0, 1},
    // }};


    // the hardest ever???
    // https://abcnews.go.com/blogs/headlines/2012/06/can-you-solve-the-hardest-ever-sudoku
    std::array<std::array<int, SIZE>, SIZE> board = {{
        {8, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 3, 6, 0, 0, 0, 0, 0},
        {0, 7, 0, 0, 9, 0, 2, 0, 0},
        {0, 5, 0, 0, 0, 7, 0, 0, 0},
        {0, 0, 0, 0, 4, 5, 7, 0, 0},
        {0, 0, 0, 1, 0, 0, 0, 3, 0},
        {0, 0, 1, 0, 0, 0, 0, 6, 8},
        {0, 0, 8, 5, 0, 0, 0, 1, 0},
        {0, 9, 0, 0, 0, 0, 4, 0, 0},
    }};


    auto begin = std::chrono::high_resolution_clock::now();
    solve(board);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %.6f seconds.\n", elapsed.count() * 1e-9);
}