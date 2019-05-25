class MutLoop(object):

    def simpleFor(self, x):
        input_list = range(0,x)
        output_list = []
        for i in input_list: 
            output_list.append(i)
        return output_list

    def inlineFor(self, x):
        input_list = range(0,x)
        output_list = [y+1 for y in input_list]
        """
        atom: [y for y in input_list]
        testlist_comp: y for y in input_list
        name: y
        comp_for: for y in input_list
        keyword: for
        name: y
        keyword: in
        name: input_list
        """
        return output_list

    def simpleWhile(self, x):
        i = 0
        output_list = []
        while i < x:
            output_list.append(i)
            i += 1
        return output_list

