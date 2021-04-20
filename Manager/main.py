from employee import Employee
from manager import Manager
from developer import Developer



dev_ken = Developer("Ken", 22200, "Java")
dev_eliza = Developer("Eliza", 25000, "Python" )
dev_ren = Developer("Ren", 23000, "Java")
dev_freddy = Developer("Freddy", 23500, "Python")
dev_amber = Developer("Amber", 23550, "C++")

devs = [dev_ken, dev_eliza, dev_ren, dev_freddy]

mgr = Manager ("Megan", 20000, devs)

print("Java developers:")
java_devs = mgr.all_java_devs()
for dev in java_devs:
    print(f"{dev.name}")

print("Python developers:")
python_devs = mgr.all_python_devs()
for dev in python_devs:
    print(f"{dev.name}")