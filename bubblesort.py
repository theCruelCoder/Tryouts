# 冒泡法

# 属于交换顺序
# 两两比较大小，交换位置。如同水泡咕嘟咕嘟往上冒
# 结果分为升序和降序排列

# 升序
# n个数从左至右，编号从0开始到n-1，索引0和1的值比较，如果索引0大，则交换位置，如果索引1大，则不交换。继续比较索引1和2的值，将大值放在右侧。知道n-2和n-1比较完，第一轮比较完成。第二轮从索引0比较到n-2，因为最右侧n-1位置上已经是最大值了。依此类推，每一轮都会减少最右侧不参与比较，直至剩下最后两个数比较。
# 降序
# 和升序相反

lst = [1,3,2,0]
length = len(lst)

for i in range(length):
    for j in range(length - 1 - i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)

# 优化实现
nums = [1,2,3,4,5,6,7,9,8]
length = len(nums)
for i in range(length):
    flag = False
    for j in range(length - 1 - i):
        count += 1
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            flag = True
            count_swap += 1
    if not flag:
        break
print(nums, count_swap, count)

# 冒泡法需要数据一轮轮比较
# 可以设定一个标记判断此轮是否有数据交换发生，如果没有发生交换，可以结束排序，如果发生交换，继续下一轮排序
# 最差的情况：初始顺序与目标顺序完全相反，遍历次数=n(n-1)/2
# 最好的情况：初始顺序与目标顺序完全相同，遍历次数n-1
# 时间复杂度O(n^2)

