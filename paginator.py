class Paginator():
    def __init__(self, data, page_size):
        self.data = data 
        self.page_size = page_size
        
    def get_page(self, page_number):
        print(self.data[self.page_size*page_number-self.page_size:self.page_size*page_number])
        
data_list = ['obj1', 'obj2', 'obj3', 'obj4', 'obj5', 'obj6', 'obj7', 'obj8', 'obj9', 'obj10', 'obj11',]

paginator = Paginator(data=data_list, page_size=3)
paginator.get_page(4)