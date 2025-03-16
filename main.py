import sys
from product import Product
from customer import Customer
from cart import Cart
from order import Order

def main():
    products = [
        Product("Laptop", 15000, 5),
        Product("Telefon", 10000, 10),
        Product("Kulaklık", 500, 20)
    ]

    name = input("Müşteri Adınızı Girin: ")
    email = input("E-posta adresinizi girin: ")
    customer = Customer(name, email)

    cart = Cart()

    while True:
        print("\nÜrünler:")
        for i, product in enumerate(products):
            print(f"{i+1}. {product}")

        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("1. Ürün ekle")
        print("2. Ürün çıkar")
        print("3. Sepeti görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        choice = input("Seçiminizi Yapın: ")

        if choice == "1":
            try:
                product_index = int(input("Hangi ürünü eklemek istiyorsunuz? (Numara): ")) - 1
                if 0 <= product_index < len(products):
                    quantity = int(input("Kaç adet eklemek istiyorsunuz?: "))
                    cart.add_product(products[product_index], quantity)
                else:
                    print("Geçersiz ürün numarası!")
            except ValueError:
                print("Geçersiz giriş, tekrar deneyin!")
        
        elif choice == "2":
            product_name = input("Hangi ürünü çıkarmak istiyorsunuz? (İsim): ")
            found = False
            for item in cart.items.values():
                if item['product'].name.lower() == product_name.lower():
                    cart.remove_product(item['product'].name)
                    print(f"{product_name} sepetten çıkarıldı.")
                    found = True
                    break
            if not found:
                print("Ürün sepetinizde bulunamadı!")
        
        elif choice == "3":
            print("\nSepetiniz:")
            cart.display_cart()
            print(f"Toplam Tutar: {cart.get_total()} TL")
        
        elif choice == "4":
            order = Order(customer, cart)
            order.place_order()
            break
        
        elif choice == "5":
            print("Çıkış yapılıyor...")
            sys.exit()
        
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin!")

if __name__ == "__main__":
    main()