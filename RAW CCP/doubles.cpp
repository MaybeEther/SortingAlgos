#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <ctime>

int main() {
    std::ofstream outFile("numbersMain.txt");
    if (!outFile) {
        std::cerr << "Error opening file.\n";
        return 1;
    }

    std::srand(std::time(0));
    std::vector<int> numbers(100000);

    for (int i = 0; i < 200; i++) {
        if (std::rand() % 4 == 0) {  // 25% chance of generating a truly random number
            numbers[i] = std::rand() % 1000;
        } else {  // 75% chance of repeating a number from an earlier index
            numbers[i] = numbers[std::rand() % (i + 1)];
        }
    }

    for (int num : numbers) {
        outFile << num << "\n";
    }

    outFile.close();

    return 0;
}
