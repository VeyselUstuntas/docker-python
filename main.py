class Account():
    def __init__(self, sahip, bakiye, paraBirimi):
        self.sahip=sahip
        self.bakiye=bakiye
        self.paraBirimi=paraBirimi
        
    def ParaYatır(self,yatiralacakTutar):
        self.bakiye+=yatiralacakTutar
        print(f"Hesabınıza '{yatiralacakTutar}' tutarında para yatırıldı. Güncel Bakiye: {self.bakiye}\n")
    
    def ParaÇekme(self,cekilecekTutar):
        if cekilecekTutar>self.bakiye:
            print("Bakiyeniz Yetersiz...\n")
        else:
            self.bakiye-=cekilecekTutar
            print(f"Hesabınızdan '{cekilecekTutar}' tutarında para çekildi. Güncel Bakiye: {self.bakiye}\n")
    def BakiyeGöster(self):
        print(f"Hesabınızda Bulunan Para miktarı: {self.bakiye}\n")
        
    def HesapBilgisi(self):
        print(f"""
                Hesap Sahibi Adı :{self.sahip}
                Hesap Bakiyesi   :{self.bakiye}
                Hesap Para Birimi:{self.paraBirimi}
        \n""")

hesap1=Account("Veysel",400000,"Dolar")
hesap1.BakiyeGöster()
hesap1.HesapBilgisi()