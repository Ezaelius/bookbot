def main():
    path_to_file = "./books/frankenstein.txt"
    name_of_book = path_to_file.strip("./books/ .txt")
    book = text_getter(path_to_file)
    num_words = wordcount(book)
    num_chars , total_char = character_count(book)
    num_chars_s = Sorting(num_chars)

    
    print(f"~-~ Reporting on {name_of_book} ~-~ \n---------")
    print(f"{num_words} words were found in the book\n---------")
    
    for item in num_chars_s:
        print(f"the letter '{item['char']} was found {item['num']}times")
    print(f"The total number of characters was {total_char} \n---------")
    print("-~- End of the report -~-")

def text_getter(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
    return file_contents

def wordcount(book):
    words = book.split()
    return len(words)

def character_count(book):
    final_count = {}
    total = 0
    for char in book.lower() :
        if char not in final_count and char.isalpha():
            final_count[char] = 1
            total += 1
        elif char.isalpha():
            final_count[char] += 1
            total += 1
    return final_count, total

def sort_on(dict):
    return dict["num"]

def Sorting(num_char):
    Sorted_list = []
    for ch in num_char:
        Sorted_list.append({"char": ch,"num": num_char[ch]})
    Sorted_list.sort(reverse=True, key=sort_on)
    return Sorted_list

main()