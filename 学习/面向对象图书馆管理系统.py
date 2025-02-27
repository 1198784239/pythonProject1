# 设计一个图书馆管理系统，包含以下功能：
# 1.图书馆（Library）有一个图书列表（books）和一个读者列表（readers）。
# 2.图书（Book）有书名（title）、作者（author）、ISBN 编号（isbn）和借阅状态（is_borrowed）。
# 3.读者（Reader）有读者姓名（name）、读者编号（reader_id）和已借阅图书列表（borrowed_books）。
# 4.图书馆支持添加图书（add_book）、添加读者（add_reader）、借阅图书（borrow_book）和归还图书（return_book）的操作。
# 5.在借阅图书时，需要检查图书是否可借以及读者是否已达到借阅上限（假设每位读者最多可借阅 3 本图书）。
# 3.在归还图书时，需要更新图书的借阅状态和读者的已借阅图书列表。

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < 3

    def borrow_book(self, book):
        if self.can_borrow() and book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)
        print(f"已添加图书: {book.title}")

    def add_reader(self, reader):
        self.readers.append(reader)
        print(f"已添加读者: {reader.name}")

    def borrow_book(self, reader_id, isbn):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if reader and book:
            if reader.borrow_book(book):
                print(f"读者 {reader.name} 成功借阅图书: {book.title}")
            else:
                print("借阅失败，图书已借出或读者已达到借阅上限。")
        else:
            print("未找到对应的读者或图书。")

    def return_book(self, reader_id, isbn):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if reader and book:
            if reader.return_book(book):
                print(f"读者 {reader.name} 成功归还图书: {book.title}")
            else:
                print("归还失败，图书未被该读者借阅。")
        else:
            print("未找到对应的读者或图书。")


# 测试代码
library = Library()
book1 = Book("Python 编程入门", "张三", "123456789")
book2 = Book("数据结构与算法", "李四", "987654321")
book3 = Book("数据结构与算法2", "李四", "987654323")
book4 = Book("数据结构与算法3", "李四", "987654324")
reader1 = Reader("王五", "001")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_reader(reader1)

library.borrow_book("001", "123456789")
library.borrow_book("001", "987654321")
library.borrow_book("001", "987654323")
library.borrow_book("001", "987654324")
# library.return_book("001", "123456789")