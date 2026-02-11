from builtins import len, print, range


def kmp_search(pattern, text):
    k,i,size_p, size_t=0,0,len(pattern),len(text)
    f = [-1]+[0]*size_p
    for i in range(1,size_p):
        while k>=0 and pattern[k]!=pattern[i]:
            k=f[k]
        k+=1
        f[i]=k
    k=0
    for i in range(size_t):
        while k>=0 and pattern[k]!=text[i]:
            k=f[k]
        k+=1
        if k==size_p:
            return i-size_p+1
    return -1


if __name__ == "__main__":
    pattern = "abc"
    text = "abxabc"
    index = kmp_search(pattern, text)
    if index != -1:
        print(f"Pattern found at index: {index}")
    else:
        print("Pattern not found in the text.")

    