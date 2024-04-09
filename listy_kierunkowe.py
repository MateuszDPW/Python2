# # lista jednokierunkowa

# class Node:
#     def __init__(self, data):
#         self.data = data    # Przechowywanie danych elementu
#         self.next = None    # Wskaźnik na następny element, początkowo None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None    # Głowa listy, pocz. None

#     def append(self,data):
#         # dodawanie elementu na koniec listy
#         if not self.head:
#             self.head = Node(data)  # Jeśli lista jest pusta, nowy element staje się głową
#             return
#         last = self.head
#         while last.next:
#             last = last.next    # Przechodzenie do ostatniego elementu
#         last.next = Node(data)  # Tworzenie nowego elementu na końcu

#     def display_all(self):
#         # wyświetlenie wszystkich wartości wraz z następną wartością
#         tmp = self.head
#         while tmp:
#             next_value = tmp.next.data if tmp.next else "None"
#             print(f"Value: {tmp.data}, Next: {next_value}")
#             tmp = tmp.next
        
    
#     def display(self, data):
#         # wyświetlenie konkretnej wartości wraz z następną wartością
#         tmp = self.head
#         while tmp:
#             if  tmp.data == data:
#                 next_value = tmp.next.data if tmp.next else "None"
#                 print(f"Value: {tmp.data}, Next: {next_value}")
#                 return  
#             tmp = tmp.next
#         print(f"wartość nie istnieje")
            
# lista = SinglyLinkedList()
# lista.append(1)
# lista.append(2)
# lista.append(3)

# lista.display_all()

# lista.display(2)


# # Lista dwukierunkowa

class Node:
    def __init__(self, data):
        self.data = data    # Przechowywanie danych elementu
        self.next = None    # Wskaźnik na następny element, początkowo None
        self.prev = None  

class DoublyLinkedList:
    def __init__(self):
        self.head = None    # Głowa listy, pocz. None

    def append(self,data):
        # dodawanie elementu na koniec listy
        if not self.head:
            self.head = Node(data)  # Jeśli lista jest pusta, nowy element staje się głową
            return
        last = self.head

        while last.next:
            last = last.next    # Przechodzenie do ostatniego elementu
        
        new = Node(data)    
        last.next = new  # Tworzenie nowego elementu na końcu
        new.prev = last


    def display_all(self):
        # wyświetlenie wszystkich wartości wraz z następną wartością
        tmp = self.head
        while tmp:
            next_value = tmp.next.data if tmp.next else "None"
            prev_value = tmp.prev.data if tmp.prev else "None"
            print(f"Value: {tmp.data}, Next: {next_value}, Prev: {prev_value}")
            tmp = tmp.next
        
    
    def display(self, data):
        # wyświetlenie konkretnej wartości wraz z następną wartością
        tmp = self.head
        while tmp:
            if  tmp.data == data:
                next_value = tmp.next.data if tmp.next else "None"
                prev_value = tmp.prev.data if tmp.prev else "None"
                print(f"Value: {tmp.data}, Next: {next_value}, Prev: {prev_value}")
            tmp = tmp.next
        print(f"wartość nie istnieje")
            
lista = DoublyLinkedList()
lista.append(1)
lista.append(2)
lista.append(3)

lista.display_all()
