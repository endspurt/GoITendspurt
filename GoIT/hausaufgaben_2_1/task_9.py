


#Aufgaben:

#1. Erstellen Sie eine Funktion namens `discount_price`, die zwei Argumente annimmt: `price` - der ursprüngliche Preis eines Produkts und `discount` - ein Rabatt als reelle Zahl von 0 bis 1.
#2. Innerhalb der Funktion `discount_price` erstellen Sie eine verschachtelte Funktion namens `apply_discount`, die `nonlocal` verwendet, um auf die Variable `price` zuzugreifen und sie zu modifizieren.
#3. Die Funktion `apply_discount` soll den reduzierten Preis berechnen, indem sie `price` mit (1 - `discount`) multipliziert.
#4. Rufen Sie `apply_discount` innerhalb von `discount_price` auf und geben Sie dann den aktualisierten Preis zurück.

#Erwartetes Ergebnis:

#Die Funktion sollte den Preis des Produkts nach Anwendung des Rabatts zurückgeben.

#Tipps:

#- Die Verwendung von `nonlocal` ermöglicht es der Funktion `apply_discount`, die in der äußeren Funktion `discount_price` deklarierte Variable `price` zu modifizieren.
#- Verwenden Sie die Formel `price * (1 - discount)` zur Berechnung des reduzierten Preises.



def discount_price(price, discount):
    # Перевірка, щоб знижка була в допустимому діапазоні
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")
    
    # Вкладена функція для застосування знижки
    def apply_discount():
        nonlocal price  # Вказує, що змінна price є з зовнішньої функції
        price *= (1 - discount)  # Розрахунок нової ціни з урахуванням знижки

    apply_discount()  # Виклик вкладеної функції для модифікації ціни
    return price      # Повернення оновленої ціни

# Приклад використання функції
original_price = 100.0
discount_value = 0.2
final_price = discount_price(original_price, discount_value)
print(f"The final price after discount is: ${final_price:.2f}")