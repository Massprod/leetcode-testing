# Given a string path, which is an absolute path (starting with a slash '/')
#  to a file or directory in a Unix-style file system,
#  convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory,
#  a double period '..' refers to the directory up a level,
#  and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
# For this problem, any other format of periods such as '...' are treated as file/directory names.
# The canonical path should have the following format:
#   1) The path starts with a single slash '/'.
#   2) Any two directories are separated by a single slash '/'.
#   3) The path does not end with a trailing '/'.
#   4) The path only contains the directories on the path from the root directory
#      to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.
# ------------------
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.


def simplify_path(path: str) -> str:
    # working_sol (19.47%, 99.94%) -> (49ms, 16.1mb)  time: O(n) | space: O(n)
    list_stack: list[str] = []
    cur_dir: str = ''
    for sym in path:
        if sym == '/':
            # Stay in current == do nothing.
            if cur_dir == '.':
                pass
            # Go to parent dir == delete current.
            elif cur_dir == '..':
                if list_stack:
                    list_stack.pop()
            # Add current directory.
            elif cur_dir:
                list_stack.append(cur_dir)
            cur_dir = ''
        else:
            cur_dir += sym
    # Extra check for last directory.
    if cur_dir:
        if cur_dir == '.':
            pass
        elif cur_dir == '..':
            if list_stack:
                list_stack.pop()
        elif cur_dir:
            list_stack.append(cur_dir)
    path: str = ''
    if list_stack:
        for direct in list_stack:
            path += '/' + direct
        return path
    # Only root.
    else:
        return '/'


# Time complexity: O(n) -> traversing input_string to get all directories => O(n) -> extra traverse of these
# n - len of input_string^^| directories to create simplified path => O(log n).
#                            Even if all directories will stay present in stack, we're still deleting '/' ->
#                            -> so it's only a part of original string.
# Auxiliary space: O(n) -> worst case, no '.' or '..' present, we will recreate original string => O(n).
# ------------------
# Should be doable with simple stack and deleting [-1] when '..' to get parent directory.
# '.' == do nothing, and everything else is just names of directories to add.
# Extra, can use split() to delete all '/'. But assume we're not allowed to use it.
# Better to leave simple loop, even if it's uglier. Especially with last index directory.


test: str = "/home/"
test_out: str = "/home"
assert test_out == simplify_path(test)

test = "/../"
test_out = "/"
assert test_out == simplify_path(test)

test = "/home//foo/"
test_out = "/home/foo"
assert test_out == simplify_path(test)

test = "/../test////////test2//tsdt...wer234/./werwerw/./werwerwerwe/..//../"
test_out = "/test/test2/tsdt...wer234"
assert test_out == simplify_path(test)
