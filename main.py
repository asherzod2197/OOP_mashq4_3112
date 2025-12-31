class Kino:
    def __init__(self, joylar):
        self.joylar = joylar

    def chipta_ol(self):
        if self.joylar > 0:
            self.joylar -= 1
            print("🎟 Chipta olindi")
        else:
            print("❌ Joylar qolmadi")

    def qolgan(self):
        print(f"🎬 Qolgan joylar: {self.joylar}")



kino1 = Kino(3)

kino1.qolgan()
kino1.chipta_ol()
kino1.chipta_ol()
kino1.chipta_ol()
kino1.chipta_ol()
kino1.qolgan()
