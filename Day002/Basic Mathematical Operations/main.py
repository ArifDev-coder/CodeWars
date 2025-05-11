"""
Betul, penggunaan eval() tidak disarankan dalam banyak kasus, terutama jika kamu mengerjakan proyek yang melibatkan input dari pengguna atau data yang tidak sepenuhnya terkendali. Meski eval() sangat kuat dan fleksibel, ia membawa risiko keamanan yang besar.

Kenapa eval() Berisiko?
eval() akan mengeksekusi string yang kamu berikan seolah-olah itu adalah kode Python yang sah. Jika input tersebut berisi kode berbahaya, seperti perintah untuk menghapus file atau akses ke sistem file (misalnya os.remove()), itu bisa dieksekusi tanpa kamu sadari.

Misalnya, jika kamu menggunakan eval() dengan input dari pengguna:

python

user_input = "__import__('os').system('rm -rf /')"  # Ini bisa menghancurkan sistem
eval(user_input)

Ini bisa sangat berbahaya karena pengguna bisa memanfaatkan input tersebut untuk mengeksekusi perintah-perintah berbahaya.
"""



"""
I am still thinking how eval() can be potentially unsafe.

Looking for it in the internet I had found some examples.

Code Injection:
user_input = input("Enter an expression: ")
result = eval(user_input)
print(result)
The user input:

__import__('os').system('rm -rf /')  # Dangerous!
DDoS
eval("while True: pass")
I will try to improve my lambda functions, to use it instead of using eval next time.

"""


"""
3 reasons why I think this approach should not be encouraged and should have 0 on Best Practices:

1. Security risk: Using eval() can be dagerous, especially if the input comes from an untrusted source. It can execute arbitrary code, leading to potential security vulnerabilities.
2. Hard to Debug: Errors in dynamically evaluated expressions can be harder to trace compared to explicit conditional branches.
3. Performance: eval() can be slower than direct operations due to the overhead of parsing and interpreting the string.
"""

operator = input("ENTER OPERATION: ")
value1 = float(input("ENTER FIST NUMBER: "))
value2 = float(input("ENTER SECOND NUMBER: "))

def basic_op(operator, value1, value2):
    try:
        return eval(f"{value1} {operator} {value2}")
    except SyntaxError:
        return "Invalid Operator"
    except NameError:
        return "Invalid Value"
    except ValueError:
        return "Invalid Value"

print(basic_op(operator, value1, value2))

def safe_calculate(operation, a, b):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    return operations.get(operation, lambda x, y: "Operasi tidak dikenali!")(a, b)


print(safe_calculate('+', 10, 5))  # Output: 15