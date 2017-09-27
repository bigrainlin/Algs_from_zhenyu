## Question

>Given an array of integers, every element appears twice except for one. Find that single one.

## Method 1 (My original solution)

Loop through the list Use a set to record the num that appears before. If a num is not in the set, add the num, else substract the num.

example nums = [a, b, c, a, b], we need to find c:
c = a+b+c-a-b


```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a_set = set()
        sum = 0
        for v in nums:
            if v not in a_set:
                sum += v
                a_set.add(v)
            else:
                sum -= v
        return sum
```

## Method 2 (Math Formula)
example nums = [a, b, c, a, b], we need to find c:

c = 2*(a+b+c) - (a+b+c+a+b)


```python
# set(list) will give a non-duplicate set
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2*sum(set(nums)) - sun(nums)
```



## ! Method 3 (Bit Manipulation) 

Utilize the `exclusive or` bit operation (XOR). XOR has follow attributes:
- commutative `a^b = b^a`
- associative `a^b^c = a^(b^c)`
- `a^a = 0`
- `a^0 = a`

So, we finnally have:

`a^b^c^d^a^b^c`

`= a^a^b^b^c^c^d`

`= 0^d = 0`


```python
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = 0
    for v in nums:
        ret ^= v
    return ret
```