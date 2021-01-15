modules = {
	"module1" : ["math", "english", "design"],
	"module2" : ["algo", "html", "networks"],
	"module3" : ["js", "java"]
}
newArray=[]
for key in modules:
    for index in(modules[key]):
        newArray.append(index)
print(newArray)