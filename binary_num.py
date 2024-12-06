# دالة لتحويل النص من صيغة بايناري إلى حروف
def binary_to_text(binary_str):
    # تقسيم النص البايناري إلى مجموعات من 8 بتات
    binary_values = [binary_str[i : i + 8] for i in range(0, len(binary_str), 8)]

    # تحويل كل مجموعة إلى عدد عشري ثم تحويلها إلى حرف
    text = "".join([chr(int(b, 2)) for b in binary_values])

    return text


# اختبار الدالة باستخدام نص بايناري
binary_str =input("Enter your Binary code\n")  # يمثل "Hello" 0100100001100101011011000110110001101111
text = binary_to_text(binary_str)
print(text)  # يجب أن يطبع "Hello"