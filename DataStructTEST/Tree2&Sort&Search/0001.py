# x คือตัวที่เราจะเช็คว่าอยู่ใน list มั้ย
# arr จาก input ต้อง sort ก่อน
# l = 0, r = len(arr)-1
def bi_search(arr, left, right, x): 
    if right >= left:
        
        mid = left + (right-left) // 2

        if arr[mid] == x:
            return "Found"
        elif arr[mid] > x:
            return bi_search(arr, left, mid-1, x)
        else:
            return bi_search(arr, mid+1, right, x)
    else:
        return "Not found"


inp = input("Enter Input : ").split("/")
arr, k = list(map(int, inp[0].split())), int(inp[1])
arr.sort()
print(bi_search(arr, 0, len(arr)-1, k))

# arr = [33, 2, 11, 82, 77, 28, 15, 76, 9, 64]
# k = 28