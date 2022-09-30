import subprocess
import platform
import locale
import chardet
        
class pinging():
    def __init__(self, counter):
        self.counter = counter
        self.coding = locale.getpreferredencoding()
        self.param = "-n" if platform.system().lower() == "windows" else "-c"
        
    def test(self, web):
        self.args = ["ping", self.param, f"{self.counter}", web]
        self.process = subprocess.Popen(self.args, stdout=subprocess.PIPE )
        for line in self.process.stdout:
        # coding = chardet.detect(line)
            line = line.decode(self.coding, errors="replace")
            print(line)
            
ping = pinging(2)
ping.test("google.com")
ping.test("youtube.com")
ping.test("yandex.ru")
        
        
    
    
    
    
# Не понимаю почему, но при использование. Может быть отличие работы PyCharm от VS Code?
# coding = locale.getpreferredencoding() // cp1251

# ЏаЁЎ«Ё§ЁвҐ«м­®Ґ ўаҐ¬п ЇаЁҐ¬ -ЇҐаҐ¤ зЁ ў ¬б:  
#     ЊЁ­Ё¬ «м­®Ґ = 35¬бҐЄ, Њ ЄбЁ¬ «м­®Ґ = 46 ¬бҐЄ, ‘аҐ¤­ҐҐ = 40 ¬бҐЄ
    