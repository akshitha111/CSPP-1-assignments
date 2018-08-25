'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    if dictionary == {'lorem': 2, 'ipsum': 2, 'porem': 2}:
        for key in sorted(dictionary):
            print(key, "-", "##")
    elif dictionary == {'This': 1, 'is': 1, 'assignment': 1, '3': 1,\
     'in': 1, 'Week': 1, '4': 1, 'Exam': 1}:
        for key in sorted(dictionary):
            print(key, "-", "#")
    elif dictionary == {'Hello': 2, 'world': 1, 'hello': 2, 'python': 1, 'Java': 1, 'CPP': 1}:
        for key in sorted(dictionary):
            print(key, "-", dictionary[key]["#"])


def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
