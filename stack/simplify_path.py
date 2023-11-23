import re


def simplifyPath(path: str) -> str:
    folder_stack = list()
    split_path = path.split('/')
    print(split_path)
    for element in split_path:
        if element == '..':
            if folder_stack:
                folder_stack.pop()
        elif element == '.':
            continue
        elif element != '':
            folder_stack.append(element)
    return '/' + '/'.join(folder_stack)


print(simplifyPath('/.../'))
