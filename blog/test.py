# 붕어빵을 만드는 기계
class Bung_O_Bbang_Machine(object):
    
    def __init__(self):
        self.flour = 'Bbang'
        self.fish = 'Bung_O_'

    def make_Bung_o_Bbang(self):
       Bung_O_Bbang = self.fish + self.flour

       return Bung_O_Bbang

if __name__ == '__main__':
    
    bm = Bung_O_Bbang_Machine() 

    print(bm.make_Bung_o_Bbang())
    
    #출력 결과물 : Bug_O_Bbang