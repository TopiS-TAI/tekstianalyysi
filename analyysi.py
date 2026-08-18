from collections import Counter
contents = None
words = None

def check_words(words, search):
    lower_words = [word.lower() for word in words]
    score = 0
    for word in search:
        score += lower_words.count(word.lower())
    return score

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
print('5. Arvioi, onko tekstin kieli suomea, ruotsia vai englantia')
option = input('Valitse toiminto (1-5): ')
print()
match option:
    case '1':
        chars = len(contents)
        print(f'Tekstissä on yhteensä {chars} merkkiä.')
    case '2':
        words_count = len(words)
        print(f'Tekstissä on yhteensä {words_count} sanaa.')
    case '3':
        words_counter = Counter(words)
        commonest = words_counter.most_common(50)
        print(f'Yleisimmät sanat tekstissä ovat: ')
        for word in commonest:
            print(f'{word[0]}: {word[1]} kappaletta.')
    case '4':
        stripped = contents.replace(' ', '')
        chars_counter = Counter(stripped)
        commonest = chars_counter.most_common(5)
        print(f'Yleisimmät merkit tekstissä ovat: ')
        for char in commonest:
            print(f'"{char[0]}": {char[1]} kappaletta.')
    case '5':
        finwords = ['että', 'ei', 'mutta', 'kun', 'ovat', 'joka', 'jos', 'vaikka', 'olla', 'tämä', 'voida', 'saada']
        swewords = ['jag', 'du', 'han', 'det', 'vi', 'ni', 'en', 'ett']
        engwords = ['the', 'be', 'to', 'and', 'a', 'an', 'that', 'have']
        fin = eng = swe = 0
        fin += check_words(words, finwords)
        swe += check_words(words, swewords)
        eng += check_words(words, engwords)
        if fin + swe + eng < len(words) / 50:
            print('En tunnista kieltä.')
        elif fin > swe and fin > eng:
            print('Luulen, että kieli on suomea.')
        elif swe > fin and swe > eng:
            print('Luulen, että kieli on ruotsia.')
        elif eng > swe and eng > fin:
            print('Luulen, että kieli on englantia.')
print()