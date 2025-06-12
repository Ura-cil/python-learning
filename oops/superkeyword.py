class parentclass:
    def parent_method(self):
        print("this is the parent method")
class childclass(parentclass):
    def parent_method(self):
        print("uracil")
        super().parent_method()
    def child_method(self):
        print("this iis the child method. ")
        super().parent_method()
child_objects = childclass()
child_objects.child_method()
child_objects.parent_method()        
