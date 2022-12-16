<p align="center">
<a href="https://programmercarl.com/other/xunlianying.html" target="_blank">
  <img src="../pics/训练营.png" width="1000"/>
</a>
<p align="center"><strong><a href="https://mp.weixin.qq.com/s/tqCxrMEU-ajQumL1i8im9A">参与本项目</a>，贡献其他语言版本的代码，拥抱开源，让更多学习算法的小伙伴们收益！</strong></p>


## 27. 移除元素

[力扣题目链接](https://leetcode.cn/problems/remove-element/)

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并**原地**修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

**你不需要考虑数组中超出新长度后面的元素。**

## 思路

针对本题，我录制了视频讲解：[数组中移除元素并不容易！LeetCode：27. 移除元素](https://www.bilibili.com/video/BV12A4y1Z7LP)，结合本题解一起看，事半功倍！

有的同学可能说了，多余的元素，删掉不就得了。

**要知道数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖。**

数组的基础知识可以看这里[程序员算法面试中，必须掌握的数组理论知识](https://programmercarl.com/数组理论基础.html)。

### 暴力解法

这个题目暴力的解法就是两层for循环，一个for循环遍历数组元素 ，第二个for循环更新数组。

删除过程如下：

![27.移除元素-暴力解法](https://tva1.sinaimg.cn/large/008eGmZEly1gntrc7x9tjg30du09m1ky.gif)

很明显暴力解法的时间复杂度是O(n^2)，这道题目暴力解法在leetcode上是可以过的。

代码如下：

```CPP
// 时间复杂度：O(n^2)
// 空间复杂度：O(1)
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            if (nums[i] == val) { // 发现需要移除的元素，就将数组集体向前移动一位
                for (int j = i + 1; j < size; j++) {
                    nums[j - 1] = nums[j];
                }
                i--; // 因为下标i以后的数值都向前移动了一位，所以i也向前移动一位
                size--; // 此时数组的大小-1
            }
        }
        return size;

    }
};
```

* 时间复杂度：O(n^2)
* 空间复杂度：O(1)

### 双指针法

双指针法（快慢指针法）： **通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。**

定义快慢指针

* 快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
* 慢指针：指向更新 新数组下标的位置

很多同学这道题目做的很懵，就是不理解 快慢指针究竟都是什么含义，所以一定要明确含义，后面的思路就更容易理解了。

删除过程如下：

![27.移除元素-双指针法](https://tva1.sinaimg.cn/large/008eGmZEly1gntrds6r59g30du09mnpd.gif)

很多同学不了解


**双指针法（快慢指针法）在数组和链表的操作中是非常常见的，很多考察数组、链表、字符串等操作的面试题，都使用双指针法。**

后续都会一一介绍到，本题代码如下：

```CPP
// 时间复杂度：O(n)
// 空间复杂度：O(1)
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slowIndex = 0;
        for (int fastIndex = 0; fastIndex < nums.size(); fastIndex++) {
            if (val != nums[fastIndex]) {
                nums[slowIndex++] = nums[fastIndex];
            }
        }
        return slowIndex;
    }
};
```
注意这些实现方法并没有改变元素的相对位置！

* 时间复杂度：O(n)
* 空间复杂度：O(1)

```CPP
/**
* 相向双指针方法，基于元素顺序可以改变的题目描述改变了元素相对位置，确保了移动最少元素
* 时间复杂度：O(n)
* 空间复杂度：O(1)
*/
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int leftIndex = 0;
        int rightIndex = nums.size() - 1;
        while (leftIndex <= rightIndex) {
            // 找左边等于val的元素
            while (leftIndex <= rightIndex && nums[leftIndex] != val){
                ++leftIndex;
            }
            // 找右边不等于val的元素
            while (leftIndex <= rightIndex && nums[rightIndex] == val) {
                -- rightIndex;
            }
            // 将右边不等于val的元素覆盖左边等于val的元素
            if (leftIndex < rightIndex) {
                nums[leftIndex++] = nums[rightIndex--];
            }
        }
        return leftIndex;   // leftIndex一定指向了最终数组末尾的下一个元素
    }
};
```


## 相关题目推荐

* 26.删除排序数组中的重复项
* 283.移动零
* 844.比较含退格的字符串
* 977.有序数组的平方

## 其他语言版本


Java：
```java
class Solution {
    public int removeElement(int[] nums, int val) {
        // 快慢指针
        int slowIndex = 0;
        for (int fastIndex = 0; fastIndex < nums.length; fastIndex++) {
            if (nums[fastIndex] != val) {
                nums[slowIndex] = nums[fastIndex];
                slowIndex++;
            }
        }
        return slowIndex;
    }
}
```
```java
//相向双指针法
class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        int right = nums.length - 1;
        while(right >= 0 && nums[right] == val) right--; //将right移到从右数第一个值不为val的位置
        while(left <= right) {
            if(nums[left] == val) { //left位置的元素需要移除
                //将right位置的元素移到left（覆盖），right位置移除
                nums[left] = nums[right];
                right--;
            }
            left++;
            while(right >= 0 && nums[right] == val) right--;
        }
        return left;
    }
}
```

Python：


``` python 3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
```




Go：
```go
func removeElement(nums []int, val int) int {
    length:=len(nums)
    res:=0
    for i:=0;i<length;i++{
        if nums[i]!=val {
            nums[res]=nums[i]
            res++
        }
    }
    nums=nums[:res]
    return res
}
```

JavaScript:
```javascript
//时间复杂度：O(n)
//空间复杂度：O(1)
var removeElement = (nums, val) => {
    let k = 0;
    for(let i = 0;i < nums.length;i++){
        if(nums[i] != val){
            nums[k++] = nums[i]
        }
    }
    return k;
};
```

TypeScript：

```typescript
function removeElement(nums: number[], val: number): number {
    let slowIndex: number = 0, fastIndex: number = 0;
    while (fastIndex < nums.length) {
        if (nums[fastIndex] !== val) {
            nums[slowIndex++] = nums[fastIndex];
        }
        fastIndex++;
    }
    return slowIndex;
};
```

Ruby:

```ruby
def remove_element(nums, val)
    i = 0
    nums.each_index do |j|
        if nums[j] != val
            nums[i] = nums[j]
            i+=1
        end
    end
    i
end
```
Rust:
```rust
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut slowIdx = 0;
        for pos in (0..nums.len()) {
            if nums[pos]!=val {
                nums[slowIdx] = nums[pos];
                slowIdx += 1;
            }
        }
        return (slowIdx) as i32;
    }
}
```

Swift:

```swift
func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
    var slowIndex = 0

    for fastIndex in 0..<nums.count {
        if val != nums[fastIndex] {
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        }
    }
    return slowIndex
}
```

PHP:
```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val) {
        if (count($nums) == 0) {
            return 0;
        }
        // 快慢指针
        $slow = 0;
        for ($fast = 0; $fast < count($nums); $fast++) {
            if ($nums[$fast] != $val) {
                $nums[$slow] = $nums[$fast];
                $slow++;
            }
        }
        return $slow;
    }
```

C:
```c
int removeElement(int* nums, int numsSize, int val){
    int slow = 0;
    for(int fast = 0; fast < numsSize; fast++) {
        //若快指针位置的元素不等于要删除的元素
        if(nums[fast] != val) {
            //将其挪到慢指针指向的位置，慢指针+1
            nums[slow++] = nums[fast];
        }
    }
    //最后慢指针的大小就是新的数组的大小
    return slow;
}
```

Kotlin:
```kotlin
fun removeElement(nums: IntArray, `val`: Int): Int {
        var slowIndex = 0 // 初始化慢指针
        for (fastIndex in nums.indices) {
            if (nums[fastIndex] != `val`) nums[slowIndex++] = nums[fastIndex] // 在慢指针所在位置存储未被删除的元素
        }
        return slowIndex
    }
```

Scala:
```scala
object Solution {
  def removeElement(nums: Array[Int], `val`: Int): Int = {
    var slow = 0
    for (fast <- 0 until nums.length) {
      if (`val` != nums(fast)) {
        nums(slow) = nums(fast)
        slow += 1
      }
    }
    slow
  }
}
```

C#:
```csharp
public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int slow = 0;
        for (int fast = 0; fast < nums.Length; fast++) {
            if (val != nums[fast]) {
                nums[slow++] = nums[fast];
            }
        }
        return slow;
    }
}
```

<p align="center">
<a href="https://programmercarl.com/other/kstar.html" target="_blank">
  <img src="../pics/网站星球宣传海报.jpg" width="1000"/>
</a>