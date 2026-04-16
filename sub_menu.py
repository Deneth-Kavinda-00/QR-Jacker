import color
import payload


def sub_menu():
    print(color.blue()+"[01]Join and Gift Win")
    print(color.blue()+"[02]Join and Free Data")
    print(color.blue()+"[03]Exit"+color.clear())
    choice = int(input("Select an option: "))
    if choice == 1:
        payload.Whatsapp(1)
    elif choice == 2:
        payload.Whatsapp(2)
    elif choice == 3:
        exit(0)
    else:
        print(color.red()+"Invalid Input")
        sub_menu()