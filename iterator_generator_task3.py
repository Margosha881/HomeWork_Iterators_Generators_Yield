class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_iter = iter(self.list_of_list)
        self.list_nested = []
        return self

    def __next__(self):
        while True:
            try:
                self.cur_elem = next(self.list_iter)
            except StopIteration:
                if not self.list_nested:
                    raise StopIteration
                else:
                    self.list_iter = self.list_nested.pop()
                    continue

            if isinstance(self.cur_elem,list):
                self.list_nested.append(self.list_iter)
                self.list_iter = iter(self.cur_elem)
            else:
                return self.cur_elem


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()