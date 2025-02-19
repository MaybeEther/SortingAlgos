#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
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

    for (int &num : numbers) {
        num = std::rand() % 1000;
    }

    std::sort(numbers.begin(), numbers.end());

    for (int num : numbers) {
        outFile << num << "\n";
    }

    outFile.close();
    return 0;
}
