if __name__ == "__main__":

    def faktorial(n):
        

        if n == 0 or n == 1:
            return 1    
        return n * faktorial(n - 1)

print (faktorial(0))
print (faktorial(1))
print (faktorial(5))
print (faktorial(100))





# def while_enumerate(iterable, start=0):
#     result = []
#     index = 0
#     while index < len(iterable):
#         result.append((start + index, iterable[index]))
#         index += 1
#     return result


# def for_enumerate(iterable, start=0):
#     result = []
#     index = start
#     for el in iterable:
#         result.append((index, el))
#         index += 1
#     return result









    # text = "abcdef"
    # print(for_enumerate(text, 10))
    # print(while_enumerate(text, 10))
