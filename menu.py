import payload,color
import sub_menu


def main_menu():
    print(color.blue()+'''[01]WhatsApp                    [02]Telegram''')
    print('''[03]TikTok                      [04]Instagram'''+color.clear())
    choice = int(input("Select an option: "))
    if choice == 1:
        sub_menu.sub_menu()
    elif choice == 2:
        payload.Telegram()
    elif choice == 3:
        payload.Tiktok()
    elif choice == 4:
        payload.Instagram()
    elif choice == 5:
        exit(0)
    else:
        print(color.red()+"Invalid option")
        main_menu()

