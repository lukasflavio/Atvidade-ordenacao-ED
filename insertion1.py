import time  # Importa o módulo para medir o tempo

def insertion_sort(array):
    # Inicia a contagem de tempo
    start_time = time.time()

    # Algoritmo de Insertion Sort
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    # Finaliza a contagem de tempo
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo de execução do Insertion Sort: {elapsed_time:.6f} segundos")
    return array

# Lê os números do arquivo de entrada
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        # Lê os números e os converte para uma lista de inteiros
        return list(map(int, file.readlines()))

# Escreve os números ordenados em um arquivo de saída
def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        # Escreve cada número em uma nova linha
        file.write('\n'.join(map(str, numbers)))

# Programa principal
def main():
    
    input_file = "num.100000.4.in"
    output_file = "num.100000.4.out"
    
    # Lê os números do arquivo de entrada
    numbers = read_numbers_from_file(input_file)
    
    # Ordena os números usando Insertion Sort
    sorted_numbers = insertion_sort(numbers)
    
    # Escreve os números ordenados no arquivo de saída
    write_numbers_to_file(output_file, sorted_numbers)
    print(f"Números ordenados salvos em '{output_file}'.")

if __name__ == "__main__":
    main()
