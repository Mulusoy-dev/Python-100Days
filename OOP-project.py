# class User:                                                       # Boş bir Sınıf (Class) oluşumu
#     def __init__(self, user_id, user_name):                       # attributes başlatmak için kullanılır
#         self.id = user_id
#         self.name = user_name
#         self.followers = 0
#         self.following = 0

# user_1 = User("001", "melih")                                     # 'User' sınıfından 'user_1' adında bir obje oluşturulması
# user_2 = User("007", "james")                                     # 'User' sınıfından 'user_2' adında bir obje oluşturulması


class Question:
    def __init__(self, text, answer):
        self.uText = text
        self.uAnswer = answer


new_q = Question("2+3=5", "True")

print(new_q.uText)
print(new_q.uAnswer)










