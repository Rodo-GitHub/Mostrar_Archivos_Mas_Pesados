# Este código utiliza la función os.walk() para recorrer todos los archivos en el directorio especificado y la función os.path.getsize() para obtener el tamaño de cada archivo.

#Luego, los archivos se almacenan en una lista junto con su tamaño y se ordenan de forma descendente según su tamaño.

#Finalmente, se muestran los primeros 10 archivos de la lista junto con su tamaño en megabytes.

import os

def get_files_sorted_by_size(directory):
    """Función para obtener los archivos ordenados por tamaño en un directorio."""
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            size = os.path.getsize(file_path)
            files.append((file_path, size))
    return sorted(files, key=lambda x: x[1], reverse=True)

def main():
    """Función principal para mostrar los archivos más pesados en un directorio."""
    directory = input("Ingrese la ruta del directorio a revisar: ")
    file_list = get_files_sorted_by_size(directory)
    print("Los archivos más pesados en el directorio son:")
    for file, size in file_list[:10]:
        print(f"{file} - {size / 1024 / 1024:.2f} MB")

if __name__ == '__main__':
    main()
