class ParentClass:
    def feature_1(self):
        print("feature_1 is running from ParentClass")

class ChildClass_1(ParentClass):
    def feature_2(self):
        print("feature_2 is running from ChildClass_1")

class ChildClass_2(ParentClass):
    def feature_3(self):
        print("feature_3 is runing from ChildClass_2")

child1 = ChildClass_1()
child1.feature_1()
child1.feature_2()


