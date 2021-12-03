import collections
class Str():
    def repeat(self, string_value):
        dictionary ={}
        splitted = collections.Counter(string_value)
        for key, st in splitted.items():
            dictionary[key] = st
            if st >=3: 
                print("False")
                return False
            else:    
                print("True")
                return True
    def pal(self, string_value):
        reverse_string = string_value[::-1]
        if string_value == reverse_string:
            print("True")
            return True
        else:
            print("False")
            return False
print("Введіть слова на перевірку:")
s=Str()
s.repeat(input("Чи містить рядок повтори послідовностей символів довжиною від 3 символів? (напр. ссттнн).\n"))
s.pal(input("Чи є рядок паліндромом? (напр. зараз).\n"))