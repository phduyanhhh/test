menu = {
    'Thịt bò': 100,
    'Thịt gà': 80,
    'Bia': 20,
    'Rượu': 45,
    'Cơm rang': 40,
    'Nem': 35
}
class MENU():
    def print_menu(self):
        print("----- MENU -----")
        for Menu in menu:
            print(f"{Menu} --- {menu[Menu]}k")
    def oder(self):
        self.so_mon = int(input("Số món bạn muốn oder là: "))
        self.gio_do = {}
        for i in range(1, self.so_mon + 1):
            mon = input(f"Món {i}: ")
            so_luong = int(input(f"Số {mon} cần dùng: "))
            self.gio_do[mon] = so_luong  

        print("----- ODER -----")
        for do in self.gio_do:
            print(f"{do} số lượng {self.gio_do[do]}")
        return self.gio_do
    def thanh_toan(self):
        total = 0
        for Menu in menu:
            for oder in self.gio_do:
                if Menu == oder:
                    total = total + self.gio_do[oder] * menu[Menu]
        print("----- HÓA ĐƠN THANH TOÁN -----")
        print(f"Thành Tiền: {total}k")
do = MENU()
do.print_menu()
do.oder()
do.thanh_toan()