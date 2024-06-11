class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

def create_account():
    account_number = input("Masukkan nomor akun: ")
    account_holder = input("Masukkan nama pemegang akun: ")
    return BankAccount(account_number, account_holder)

def menu():
    print("\n=== Menu Bank ===")
    print("1. Buat Akun")
    print("2. Cek Saldo")
    print("3. Setor Tunai")
    print("4. Tarik Tunai")
    print("5. Keluar")

def main():
    accounts = {}
    while True:
        menu()
        choice = input("Pilih menu (1-5): ")

        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Akun untuk {account.account_holder} berhasil dibuat.")

        elif choice == '2':
            account_number = input("Masukkan nomor akun: ")
            if account_number in accounts:
                print(f"Saldo: {accounts[account_number].check_balance()}")
            else:
                print("Akun tidak ditemukan.")

        elif choice == '3':
            account_number = input("Masukkan nomor akun: ")
            if account_number in accounts:
                amount = float(input("Masukkan jumlah setoran: "))
                if accounts[account_number].deposit(amount):
                    print("Setoran berhasil.")
                else:
                    print("Setoran gagal. Jumlah tidak valid.")
            else:
                print("Akun tidak ditemukan.")

        elif choice == '4':
            account_number = input("Masukkan nomor akun: ")
            if account_number in accounts:
                amount = float(input("Masukkan jumlah penarikan: "))
                if accounts[account_number].withdraw(amount):
                    print("Penarikan berhasil.")
                else:
                    print("Penarikan gagal. Jumlah tidak valid atau saldo tidak mencukupi.")
            else:
                print("Akun tidak ditemukan.")

        elif choice == '5':
            print("Terima kasih telah menggunakan layanan kami.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
