from collections import Counter
contents = None
words = None

while True:
    filename = input('Anna avattavan tiedoston nimi: ')
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            words = contents.split(' ')
            break
    except FileNotFoundError as e:
        print(f'Tiedostoa {filename} ei löydy!')
    except Exception as e:
        print('Muu virhe: ' + e.strerror)

print(f'Tiedosto {filename} avattu.')
print('1. Laske merkkien määrä')
print('2. Laske sanojen määrä')
print('3. Listaa 5 yleisintä sanaa')
print('4. Listaa 5 yleisintä merkkiä')
option = input('Valitse toiminto (1-4): ')
match option:
    case '1':
        chars = len(contents)
        print(f'Tekstissä on yhteensä {chars} merkkiä.')
    case '2':
        words_count = len(words)
        print(f'Tekstissä on yhteensä {words_count} sanaa.')
    case '3':
        words_counter = Counter(words)
        commonest = words_counter.most_common(5)
        print(commonest)