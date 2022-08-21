class User:                                                       # Boş bir Sınıf (Class) oluşumu
    def __init__(self, user_id, user_name):                       # attributes başlatmak için kullanılır
        self.id = user_id
        self.name = user_name




user_1 = User("001", "melih")                                     # 'User' sınıfından 'user_1' adında bir obje oluşturulması
user_2 = User("007", "james")                                     # 'User' sınıfından 'user_2' adında bir obje oluşturulması



print(user_1.id)
print(user_2.id)


