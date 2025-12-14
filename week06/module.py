import week06
import plusNumber as pn
import platform

week06.greeting()

infoName = week06.personal["name"]
print(infoName)

plus = pn.plusNumber(10, 20)
print(plus)

os = platform.system()
print(os)