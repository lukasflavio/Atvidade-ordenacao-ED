import time

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return list(map(int, file.readlines()))

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        file.write('\n'.join(map(str, numbers)))

def main():
    input_file = "num.100000.4.in"
    output_file = "num.100000.4.out"
    
    numbers = read_numbers_from_file(input_file)
    
    start_time = time.time()
    

    sorted_numbers = selection_sort(numbers)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    write_numbers_to_file(output_file, sorted_numbers)
    print(f"Números ordenados salvos em '{output_file}'.")
    print(f"Tempo de execução: {elapsed_time:.6f} segundos")

if __name__ == "__main__":
    main()
