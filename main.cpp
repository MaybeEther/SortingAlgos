#include <iostream>
#include <chrono>
#include <thread>
#include <vector>
#include <fstream>  // For file output

using namespace std;

// Function to log the time for each sort (only the raw time in seconds)
void logSortTime(chrono::duration<double> duration) {
    ofstream file("sort_times.txt", ios::app);  // Open the file in append mode
    if (file.is_open()) {
        file << duration.count() << endl;  // Write only the raw time
        file.close();
    } else {
        cout << "Unable to open file." << endl;
    }
}

// Function for Selection Sort
void selectionSort() {
    auto start = chrono::high_resolution_clock::now();  // Start timing

    // Simulate sorting process
    this_thread::sleep_for(chrono::seconds(1));  // Simulate a delay

    auto end = chrono::high_resolution_clock::now();  // End timing
    chrono::duration<double> duration = end - start;  // Calculate the duration

    cout << "selection !"<< duration.count() << endl;  // Console output
    logSortTime(duration);  // Log the time to file
}

// Function for Exchange Sort
void exchangeSort() {
    auto start = chrono::high_resolution_clock::now();  // Start timing

    // Simulate sorting process
    this_thread::sleep_for(chrono::seconds(1));  // Simulate a delay

    auto end = chrono::high_resolution_clock::now();  // End timing
    chrono::duration<double> duration = end - start;  // Calculate the duration

    cout << "exchange !" << duration.count() << endl;  // Console output
    logSortTime(duration);  // Log the time to file
}

// Function for Insertion Sort
void insertionSort() {
    auto start = chrono::high_resolution_clock::now();  // Start timing

    // Simulate sorting process
    this_thread::sleep_for(chrono::seconds(1));  // Simulate a delay

    auto end = chrono::high_resolution_clock::now();  // End timing
    chrono::duration<double> duration = end - start;  // Calculate the duration

    cout << "insertion !" << duration.count() << endl;  // Console output
    logSortTime(duration);  // Log the time to file
}

// Function for Merge Sort
void mergeSort() {
    auto start = chrono::high_resolution_clock::now();  // Start timing

    // Simulate sorting process
    this_thread::sleep_for(chrono::seconds(1));  // Simulate a delay

    auto end = chrono::high_resolution_clock::now();  // End timing
    chrono::duration<double> duration = end - start;  // Calculate the duration

    cout << "merge !" << duration.count() << endl;  // Console output
    logSortTime(duration);  // Log the time to file
}

// Function for Quick Sort
void quickSort() {
    auto start = chrono::high_resolution_clock::now();  // Start timing

    // Simulate sorting process
    this_thread::sleep_for(chrono::seconds(1));  // Simulate a delay

    auto end = chrono::high_resolution_clock::now();  // End timing
    chrono::duration<double> duration = end - start;  // Calculate the duration

    cout << "quick !" << duration.count() << endl;  // Console output
    logSortTime(duration);  // Log the time to file
}

//  Heap Sort function below!

void heapify(vector<int>& arr, int n, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest); // Recursively heapify the affected subtree
    }
}

void heapSort(string filename) {
    ifstream inputFile(filename);
    vector<int> arr;
    int num;
    while (inputFile >> num) {
        arr.push_back(num);}
    inputFile.close();
    auto start = chrono::high_resolution_clock::now();  // Start timer
    int n = arr.size();

    // Build heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extract elements from heap
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
    auto end = chrono::high_resolution_clock::now();  // End timer
    chrono::duration<double> duration = end - start;  // Calculate the duration

    cout << "heap !" << duration.count() << endl;  // Console output / trigger
    logSortTime(duration);  // Log the time to the timer for avgs
}


int main() {
    // Call the sorting functions one by one
    selectionSort();
    exchangeSort();
    insertionSort();
    mergeSort();
    quickSort();
    heapSort("numbersMain.txt");

    return 0;
}
