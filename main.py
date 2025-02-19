import tkinter as tk
from tkinter import Label, Button, Canvas, Text
import os
import time
import subprocess
import matplotlib.pyplot as plt
import numpy as np


def run_process(command, text_widget, filename):
    os.system(f"{command}")
    time.sleep(1)  # Wait a bit before reloading the file content
    load_file_content(text_widget, filename)


def run_rng():
    run_process("rng", text_display, "numbersMain.txt")


def run_ordered():
    run_process("ordered", text_display, "numbersMain.txt")


def run_reverced():
    run_process("reverced", text_display, "numbersMain.txt")


def run_doubles():
    run_process("doubles", text_display, "numbersMain.txt")

def averages():
    with open("sort_times.txt", "r") as file:
        content = file.readlines()

    numbers = [float(line.strip()) for line in content]  # Convert to float
    batch_size = 6
    num_batches = len(numbers) // batch_size

    averages = [sum(numbers[i::batch_size]) / num_batches for i in range(batch_size)]

    return averages
def averagesPNG(averages):
    labels = ['Selection', 'Exchange', 'Insertion', 'Merge', 'Quick', 'Heap']
    plt.bar(labels, averages)
    plt.title('Sort Averages')
    plt.xlabel('Sorts')
    plt.ylabel('time (seconds)')
    plt.savefig("averages.png")



def run_sort():
    # Reset all labels before starting the sort
    reset_sort_labels()

    # Run the process and listen for "finished" messages
    process = subprocess.Popen(["./SortMain.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def update_status(label, status_text, color):
        label.config(text=status_text, fg=color)


    while True:
        line = process.stdout.readline().strip()
        if line == '':  # End of output
            break

        # Split the line to get sort name and time
        parts = line.split("!")
        if len(parts) == 2:
            sort_name, sort_time = parts[0].strip(), parts[1].strip()

            # Update the corresponding label based on the sort name
            if sort_name == "selection":
                update_status(selection_sort_label, "Selection sort: FINISHED in s" + sort_time, "green")
            elif sort_name == "exchange":
                update_status(exchange_sort_label, "Exchange sort: FINISHED in s" + sort_time, "green")
            elif sort_name == "insertion":
                update_status(insertion_sort_label, "Insertion sort: FINISHED in s" + sort_time, "green")
            elif sort_name == "merge":
                update_status(merge_sort_label, "Merge sort: FINISHED in s" + sort_time, "green")
            elif sort_name == "quick":
                update_status(quick_sort_label, "Quick sort: FINISHED in s" + sort_time, "green")
            elif sort_name == "heap":
                update_status(heap_sort_label, "Heap sort: FINISHED in s" + sort_time, "green")

    process.stdout.close()
    process.wait()


def load_file_content(text_widget, filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            text_widget.config(state=tk.NORMAL)
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, content)
            text_widget.config(state=tk.DISABLED)
    except FileNotFoundError:
        text_widget.config(state=tk.NORMAL)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, "File not found.")
        text_widget.config(state=tk.DISABLED)


def reset_sort_labels():
    # Reset all sort labels to "NOT STARTED" (red color) before starting a new sort
    selection_sort_label.config(text="Selection sort: NOT STARTED", fg="red")
    exchange_sort_label.config(text="Exchange sort: NOT STARTED", fg="red")
    insertion_sort_label.config(text="Insertion sort: NOT STARTED", fg="red")
    merge_sort_label.config(text="Merge sort: NOT STARTED", fg="red")
    quick_sort_label.config(text="Quick sort: NOT STARTED", fg="red")
    heap_sort_label.config(text="Heap sort: NOT STARTED", fg="red")


def create_ui():
    global text_display, selection_sort_label, exchange_sort_label, insertion_sort_label
    global merge_sort_label, quick_sort_label, heap_sort_label, label_time

    root = tk.Tk()
    root.title("Sorting Visualization")
    root.geometry("900x500")

    # Status Labels
    selection_sort_label = Label(root, text="Selection sort: NOT STARTED", fg="red")
    selection_sort_label.place(x=20, y=20)

    exchange_sort_label = Label(root, text="Exchange sort: NOT STARTED", fg="red")
    exchange_sort_label.place(x=20, y=50)

    insertion_sort_label = Label(root, text="Insertion sort: NOT STARTED", fg="red")
    insertion_sort_label.place(x=20, y=80)

    merge_sort_label = Label(root, text="Merge sort: NOT STARTED", fg="red")
    merge_sort_label.place(x=20, y=110)

    quick_sort_label = Label(root, text="Quick sort: NOT STARTED", fg="red")
    quick_sort_label.place(x=20, y=140)

    heap_sort_label = Label(root, text="Heap sort: NOT STARTED", fg="red")
    heap_sort_label.place(x=20, y=170)

    # Sorting Buttons
    Button(root, text="RNG", bg="red", fg="white", command=run_rng).place(x=500, y=20)
    Button(root, text="ordered", bg="red", fg="white", command=run_ordered).place(x=580, y=20)
    Button(root, text="reverced", bg="red", fg="white", command=run_reverced).place(x=660, y=20)
    Button(root, text="doubles", bg="red", fg="white", command=run_doubles).place(x=740, y=20)
    Button(root, text="SORT", bg="green", fg="white", command=run_sort).place(x=600, y=60)

    # File Display
    Label(root, text="numbersMain.txt", bg="lightgray").place(x=500, y=100, width=380)
    text_display = Text(root, height=10, width=50)
    text_display.place(x=500, y=130)
    load_file_content(text_display, "numbersMain.txt")

    try:
        image = Image.open('times.png')
        display = ImageTk.PhotoImage(image)
        label = Label(root, image=display)
        label.image = display  # Keep reference
        label.place(x=20, y=280, width=400, height=200)  # Positioning
    except Exception as e:
        print(f"Error loading times.png: {e}")

        # Averages Graph Image
    try:
        image = Image.open('averages.png')
        display = ImageTk.PhotoImage(image)
        label = Label(root, image=display)
        label.image = display  # Keep reference
        label.place(x=460, y=280, width=400, height=200)  # Positioning
    except Exception as e:
        print(f"Error loading averages.png: {e}")

    root.mainloop()

    create_ui()


averagesPNG(averages())
create_ui()

