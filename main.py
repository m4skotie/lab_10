def z1():
    import json
    with open('products.json',encoding='utf=8' ) as f:
        data = json.load(f)
    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
def z2():
    import json
    with open('products.json', encoding='utf=8') as f:
        data = json.load(f)
    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
    new_product = {}
    new_product['name'] = input("Введите название нового продукта: ")
    new_product['price'] = float(input("Введите цену нового продукта: "))
    new_product['weight'] = float(input("Введите вес нового продукта: "))
    new_product['available'] = bool(input("Есть ли новый продукт в наличии? (True/False): "))
    data['products'].append(new_product)
    with open('products.json', 'w') as f:
        json.dump(data, f)
    print("\nОбновленное содержимое файла products.json:")
    with open('products.json', 'r') as f:
        print(f.read())


def z3():
    enru = open('en-ru.txt', 'r', encoding='utf-8').readlines()
    ruen = open("ru-en.txt", "w")
    for i in enru:
        a = i.split(' - ')
        n = len(a[1])
        n = n - 1
        ruen.write(a[1][:n] + ' - ' + a[0] + '\n')
    ruen.close()
    text = open('ru-en.txt', 'r')
    lines = text.readlines()
    lines.sort()
    text.close()
    text2 = open('ru-en.txt', 'w')
    for line in lines:
        text2.write(line)
z3()








