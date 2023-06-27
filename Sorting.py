import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time

def print_iterations(arr, sort_type):
    print(f"\n{sort_type} Sort Iterations:")
    print("First 5 iterations: ", arr[:5])
    print("Last 5 iterations: ", arr[-5:])

def print_execution_time(time_taken):
    print("Execution Time: ", time_taken, "seconds")

def print_before_after(arr, sort_type):
    print(f"\nBefore {sort_type} Sort: ", arr)
    sorted_arr, _ = bubble_sort(arr.copy()) if sort_type == "Bubble" else insertion_sort(arr.copy())
    print(f"After {sort_type} Sort: ", sorted_arr)

def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    while True:
        print("\nMenu:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            sorted_arr, execution_time = bubble_sort(arr)
            print_iterations(sorted_arr, "Bubble")
            print_execution_time(execution_time)
            print_before_after(arr, "Bubble")
        elif choice == 2:
            sorted_arr, execution_time = insertion_sort(arr)
            print_iterations(sorted_arr, "Insertion")
            print_execution_time(execution_time)
            print_before_after(arr, "Insertion")
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
