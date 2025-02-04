from transliterate import translit
from num2words import num2words

def main():
    numbers=('78','15','3','40','8')
    
    text = ("""Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.
More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...
            """)

    print(translit(text, 'ru'))

    for number in numbers:
        print(f'{number} -', translit(num2words(number),'ru'))

if __name__ == '__main__':
    main()