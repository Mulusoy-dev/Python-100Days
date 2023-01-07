# Multi-threading (Çoklu işlem parçacığı) -> Tek bir işlemde aynı anda birden çok iş parçaçığı yürütme işlemidir.

# Python iş parçacığı oluşturma, programınızın farklı bölümlerinin aynı anda çalışmasını sağlar ve tasarımı hızlandırır.
# Dezavantaj: Python Versiyon 3.6 ile kullanılıyor.
#
# Programınızda çalışan ve her biri aynı anda bağımsız bir görev yapan iki (veya daha fazla) farklı işlemciye sahip olmak gibi düşünmek cazip gelebilir.
# İş parçacıkları farklı işlemcilerde çalışıyor olabilir, ancak her seferinde yalnızca bir tane çalışıyor olacaklar.
#
#


# _thread ve threading modülleri Multi-thread işlemleri için kullanılır.
# Bu modüller senkronizasyona yardımcı olur ve kullanımda olan bir iş parçaçığına kilit sağlar.

# Bir kilit objesi Lock() ile oluşturulur.
# Lock iki duruma sahip: "locked" ve "unlocked".
# İki basit metoda sahip: "acquire()" ve "release()".

# Durum "unlocked" -> "locked" çevirmek için print_lock.acquire()
# Durum "locked" -> "unlocked" çevirmek için print_lock.release()

# thread.start_new_thread() görevi, yeni bir iş parçacığı başlatmak ve tanımlayıcısını döndürmek için kullanılır.
# Ilk argüman çağrılacak olan fonksiyondur ve ikinci argüman, argümanların konum listesini döndüren bir tuple nesnesidir.


from _thread import *
import threading

print_lock = threading.local()                            # Bir kilit nesnesi oluşturuldu.




