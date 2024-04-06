import math


class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.pages = []
        i = 0
        while i < self.page_count:
            self.pages.append(data[i * items_on_page:(i + 1) * items_on_page])
            i += 1
        print(self.pages)


    @property
    def page_count(self) -> int:
        return math.ceil(self.item_count / self.items_on_page)

    @property
    def item_count(self):
        return len(self.data)

    def count_items_on_page(self, page_number):
        try:
            return len(self.pages[page_number])
        except:
            raise Exception("Invalid index. Page is missing.")


    def find_page(self, data):
        result = []
        if data in self.data:
            i = 0
            while True:
                idx = self.data.find(data, i)
                if idx == -1: break
                len_data = len(data)
                while len_data > 0:
                    result.append(idx // self.items_on_page)
                    idx += self.items_on_page
                    len_data = 0 if (len_data - self.items_on_page < 0) else len_data - self.items_on_page
                i = idx

        else:
            raise Exception(f'\'{data}\' is missing on the pages')
        return result

    def display_page(self, page_number):
        return self.pages[page_number]


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    # Your |beaut|iful |text
    print(pages.page_count)
    # 4
    print(pages.item_count)
    # 19

    print(pages.count_items_on_page(0))
    # 5
    print(pages.count_items_on_page(3))
    # 4
    print(pages.count_items_on_page(4))
    # Exception: Invalid index. Page is missing.
    print(pages.find_page('Your'))
    # [0]
    print(pages.find_page('e'))
    # [1, 3]
    print(pages.find_page('beautiful'))
    # [1, 2]
    print(pages.find_page('great'))
    # Exception: 'great' is missing on the pages
    print(pages.display_page(0))
    # 'Your '
