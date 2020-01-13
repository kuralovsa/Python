class Printer:
    def log(self,*values):
        print(values)
class FormatPrinter(Printer):
    def log (self,*values):
        l=str(values)
        m=len(l)
        print(f'*'*(m+2))
        print("*"+l+'*')
        print(f'*'*(m+2))
a=FormatPrinter()
a.log(555,'hello',888)
