l = [1, 2, 3, 4, 5]
['yes'
 if v == 1
 else 'no' if v == 2
 else print("NO")
 for v in l]

nb['cells'] = [ md_cell(read_file(name))
                if name.endswith('.md')
                else code_cell(read_file(name))
                if name.endswith('.py')
                else None
                for name in filenames ]

[0, None, 2] if not None
