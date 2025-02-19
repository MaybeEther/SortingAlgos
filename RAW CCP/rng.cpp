#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

int main() {
    std::ofstream outFile("numbersMain.txt");
    if (!outFile) {
        std::cerr << "Error opening file.\n";
        return 1;
    }

    std::srand(std::time(0));
    for (int i = 0; i < 100000; i++) {
        outFile << (std::rand() % 1000) << "\n";  // Random number between 0 and 999
    }

    outFile.close();
    return 0;
}
