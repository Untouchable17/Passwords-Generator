import random
import time

__author__ = 'SecDet Samurai'


class Generate:

    def __init__(self, count=0, length=0):
        self.count = count
        self.length = length

    def password_generator(self):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

        try:
            for c_script in range(self.count):
                generator = ' '
                for subscript in range(self.length):
                    generator += random.choice(chars)

                self.save_passwords(generator)
                print(generator)

        except ValueError:
            print("Unknown error. Try again")
            return self.password_generator()

    def get_data(self):

        try:
            count = int(input("Введите кол-во паролей: "))
            length = int(input("Введите длину пароля: "))
            self.count, self.length = count, length

        except ValueError: exit(-1)

        self.password_generator()
        choose = input("\nСгенерировать новые пароли? \n>> \"+\" или \"-\": ").lower()
        return self.generate_passwd() if choose == "+" else exit()

    @staticmethod
    def save_passwords(data):

        with open('passwords.txt', 'a') as file:
            file.write(f"{data}\n")


def main():
    generator = Generate()
    generator.get_data()


if __name__ == "__main__":
    main()
