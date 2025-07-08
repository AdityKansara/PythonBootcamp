import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums = ['1','2','3','4','5','6','7','8','9','0']
special=['!','$','#','%','&','*','+','(',')']

print("Welcome to Password Generator\n")
total_letters = int(input("How many letters do you like in your password?\n"))
total_num = int(input("How many numbers do you like?\n"))
total_sym = int(input("How many symbols do you like?\n"))

# generated_password = ""
# for i in range(total_letters):
#     generated_password += random.choice(letters)
# for i in range(total_num):
#     generated_password += random.choice(nums)
# for i in range(total_sym):
#     generated_password += random.choice(special)

generated_password = []
for i in range(total_letters):
    generated_password.append(random.choice(letters))
for i in range(total_num):
    generated_password.append(random.choice(nums))
for i in range(total_sym):
    generated_password.append(random.choice(special))

random.shuffle(generated_password)
final_pwd = ""
for char in generated_password:
    final_pwd += char

print("Your generated Password is " + final_pwd)