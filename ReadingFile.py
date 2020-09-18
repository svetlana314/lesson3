def main():
    with open('referat.txt', 'r', encoding = 'utf-8') as doc:content = doc.read()
    file_length = len(content)
    print(file_length)

    words = len(content.split())
    print(words)

    with open('referat2.txt', 'w', encoding = 'utf-8') as doc2:
        for line in content:
            line = line.replace('.', '!')
            doc2.write(line)

if __name__ == "__main__":
    main()