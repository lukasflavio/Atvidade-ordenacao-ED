import time  

def insertion_sort(array):
   
    start_time = time.time()
    
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo de execução do Insertion Sort: {elapsed_time:.6f} segundos")
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
    
    sorted_numbers = insertion_sort(numbers)
    
    write_numbers_to_file(output_file, sorted_numbers)
    print(f"Números ordenados salvos em '{output_file}'.")

if __name__ == "__main__":
    main()
