import whatsapp,telegram,instagram,tiktok

def Whatsapp(x):
    whatsapp.main(x)
    whatsapp.app.run(port=5000, debug=False)
def Telegram():
    telegram.Telegram()
def TikTok():
    tiktok.Tiktok()
def Instagram():
    instagram.Instagram()