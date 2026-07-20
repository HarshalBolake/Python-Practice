class ParentClass:
    def feature_1(self):
        print("feature_1 from parent class is running")

    def feature_2(self):
        print("feature_2 from parent class is running")

class ChildClass(ParentClass):
    def feature_3(self):
        print("feature_3 from child class is running")

child1 = ChildClass()
child1.feature_1()
child1.feature_2()
child1.feature_3()