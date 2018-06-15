from name_function import get_formatted_name

print("Pressione 'q' para sair.")
while True:
    first = input('Digite o primeiro nome: ')
    if first == 'q':
        break
    last = input('Digite o sobrenome: ')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print('Nome formatado: ' + formatted_name)
