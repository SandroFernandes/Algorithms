# generate all permutations of a string using recursion

def permute_string(string):
    if len(string) == 1:
        return [string]
    else:
        perms = []
        for i in range(len(string)):
            for perm in permute_string(string[:i] + string[i+1:]):
                perms.append(string[i] + perm)
        return perms

print(permute_string('abc'))