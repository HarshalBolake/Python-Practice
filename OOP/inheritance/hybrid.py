class ParentClass:
    def feature_1(self):
        print("feature_1 is running from parentClass")

class ChildClass_1(ParentClass):
    def feature_2(self):
        print("feature_2 is runing from ChildClass_1")
    
class ChildClass_2(ParentClass):
    def feature_3(self):
        print("feature_3 is running from ChildClass_2")

class ChildClass_3(ChildClass_1,ChildClass_2):
    def feature_4(self):
        print("feature_4 is running from ChildCLass_3")

Child = ChildClass_3()
Child.feature_1()
Child.feature_2()
Child.feature_3()
Child.feature_4()
