class ParentClass_1:
    def feature_1(self):
        print("feature_1 is running from ParentClass_1")
    
class ParentClass_2:
    def feature_2(self):
        print("feature_2 is running from ParentClass_2")
    
class ChildClass(ParentClass_1,ParentClass_2):
    def feature_3(self):
        print("feature_3 is running from ChildClass")

Child1 = ChildClass()
Child1.feature_1()
Child1.feature_2()
Child1.feature_3()