b = int(input("Введіть число: "))
i = (b % 2)
print("число парне" if i == 0 else "число непарне")


#Завдання 6
day = input("Введіть день тижня:").lower()
match day:
    case "понеділок"| "вівторок" | "середа" | "четвер" | "п\'ятниця":
        print("Сьогодні на роботу")
    case "субота" | "неділя":
        print("Сьогодні вихідний")
    case _:
        print("Немає такого дня тижня")