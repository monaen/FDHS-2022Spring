## Arithmetic Operators

* <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">+</code>: **Addition**

* <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">-</code>: **Subtraction**

* <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">*</code>: **Multiplication**

* <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">/</code>: **Division**

* <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">%</code>: **Mod**: give the remainder after dividing

* <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">**</code>: **Exponentiation** (note that <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">^</code> does not do this operation, as you might have seen in other languages)

* <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">//</code>: **Integer division**: Divides and rounds down to the nearest integer

* <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">^</code>: **Bitwise XOR**

The usual order of mathematical operations holds in Python. Bitwise operators are special operators in Python that you can learn more about [here](https://wiki.python.org/moin/BitwiseOperators) if you'd like.


## Variables and Assignment Operators
Variables are used all the time in Python! Below is an example:

```python
mv_population = 74728
```

Here <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">mv_population</code> is a **variable**, which holds the value of 74728. The equal sign <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">=</code> is an **assignment operator** which assigns the item on the right to the variable name on the left, which is actually a little different than mathematical equality, as 74728 does not hold the value of mv_population.

In any case, whatever term is on the left side, is now a name for whatever value is on the right side. Once a value has been assigned to a variable name, you can access the value from the variable name.

Example:
```python
x = 2
y = x
print(y)

>>> 2
```
If you try to access a variable that was never defined, you will get the following error message:
```python
NameError: name 'z' is not defined
```

#### Multiple assignment
Python allows compact assignment, for example, the following two are equivalent in terms of assignment:
```python
x = 3
y = 4
z = 5
```
and
```python
x, y, z = 3, 4, 5
```
However, the above isn't a great way to assign variables in most cases, because our variable names should be descriptive of the values they hold.


Besides writing variable names that are descriptive, there are a few things to watch out for when naming variables in Python.

1. Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.

2. **You can’t use reserved words or built-in identifiers** that have important purposes in Python, which you’ll learn about throughout this course. A list of python reserved words is described [here](https://pentangle.net/python/handbook/node52.html). Creating names that are descriptive of the values often will help you avoid using any of these words. A quick table of these words is also available below.

 **Keywords** in Python programming language

|         |          |         |          |        |
| ------- | -------- | ------- | -------- | ------ |
| False   | class    | finally | is       | return |
| None    | continue | for     | lambda   | try    |
| True    | def      | from    | nonlocal | while  |
| and     | del      | global  | not      | with   |
| as      | elif     | if      | or       | and    |
| assert  | else     | import  | pass     |        |
| break   | execpt   | in      | raise    |        |

3. The pythonic way to name variables is to use all lowercase letters and underscores to separate words. For examples,
```python
my_height = 58
my_lat = 40
my_long = 105
```

#### Assignment Operators

1. The equal sign <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">=</code> assigns the value on the right side to the variable on the left side.

2. The equal sign <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">+=</code> e.g., The equal sign <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">x += 2</code> is equivalent to <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">x = x + 2</code>.

3. The equal sign <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">-=</code> e.g., <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">x -= 2</code> is equivalent to <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">x = x - 2</code>.

The above three assignment operators are the most commonly used ones. There are some other assignment operators from the video. For example, you can also use <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">*=</code> in a similar way, but this is less common than the operations shown above. You can find some practice with much of what we have already covered [here](https://www.programiz.com/python-programming/operators).


## Summary
####  Operator Cheat Sheet

1) **Arithmetic operators**:

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

| Operator  | Meaning  | Example  |
| --------- | -------- | -------- |
| +  |Add two operands or unary plus| x + y + 2 |
| -  |Subtract right operand from the left or unary minus| x - y - 2 |
| *  |Multiply two operands|x * y |
| /  |Divide left operand by the right one (always results into float)|x / y|
| %  |Modulus - remainder of the division of left operand by the right|x % y (remainder of x/y)|
| //  |Floor division - division that results into whole number adjusted to the left in the number line|x // y|
| **  |Exponent - left operand raised to the power of right|x**y (x to the power y)|


2) **Comparison operators**:

Comparison operators are used to compare values. It returns either **True** or **False** according to the condition.

| Operator | Meaning | Example |
| ------------ | ------------ | ------------ |
| >  |Greater than - True if left operand is greater than the right|x > y|
| <  |Less than - True if left operand is less than the right|x < y|
| == |Equal to - True if both operands are equal|x == y|
| != |Not equal to - True if operands are not equal|x != y|
| >= |Greater than or equal to - True if left operand is greater than or equal to the right|x >= y|
| <= |Less than or equal to - True if left operand is less than or equal to the right|x <= y|

3) **Logical operators**:

Logical operators are the <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">and</code>, <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">or</code>, <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">not</code> operators.

| Operator | Meaning | Example |
| ------------ | ------------ | ------------ |
| and  | True if both the operands are true | x and y  |
| or  | True if either of the operands is true  | x or y  |
| not  | True if operand is false (complements the operand)  | not x  |


4) **Bitwise operators**:

 Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

 For example, 2 is <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">10</code> in binary and 7 is <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">111</code>.

 In the table below: Let <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">x = 10</code> (<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">0000 1010</code> in binary) and <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">y = 4</code> (<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">0000 0100</code> in binary)

| Operator  | Meaning  | Example  |
| ------------ | ------------ | ------------ |
| &   | Bitwise AND         | x & y = 0 (<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">0000 0000</code>)  |
| \|  | Bitwise OR          | x | y = 14 (<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">0000 1110</code>) |
| ~   | Bitwise NOT         | ~x = -11 (<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">1111 0101</code>)   |
| ^   | Bitwise XOR         | x ^ y = 14 (<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">0000 1110</code>) |
| >>  | Bitwise right shift | x >> 2 = 2 (<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">0000 0010</code>)  |
| <<  | Bitwise left shift  | x << 2 = 40 (<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">0010 1000</code>)  |

5) **Assignment operators**:

 Assignment operators are used in Python to assign values to variables.

 <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">a = 5</code> is a simple assignment operator that assigns the value **5** on the right to the variable **a** on the left.

 There are various compound operators in Python like <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">a += 5</code> that adds to the variable and later assigns the same.
 It is equivalent to <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">a = a + 5</code>.

| Operator     | Meaning       |  Equivalent to |
| ------------ | ------------- | -------------- |
| =    | x = 5   | x = 5       |
| +=   | x += 5  | x = x + 5   |
| -=   | x -= 5  | x = x - 5   |
| \*=  | x \*= 5 | x = x * 5   |
| /=   | x /= 5  | x = x / 5   |
| %=   | x %= 5  | x = x % 5   |
| //=  | x //= 5 | x = x //= 5 |
| \*\*=| x \*\*= 5 | x = x \*\* 5 |
| &=   | x &= 5  | x = x & 5   |
| \|=  | x \|= 5 | x = x \| 5  |
| ^=   | x ^= 5  | x = x ^ 5   |
| >>=  | x >>= 5 | x = x >> 5  |
| <<=  | x <<= 5 | x = x << 5  |

6) **Identity operators**:

is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

| Operator  | Meaning  |  Example |
| ------------ | ------------ | ------------ |
| is  | True if the operands are identical (refer to the same object)  | x is True |
| is not  | True if the operands are not identical (do not refer to the same object)  | x is not True |


7) **Membership operators**:

<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">in</code> and <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">not in</code> are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

 In a dictionary we can only test for presence of key, not the value.

| Operator  | Meaning  |  Example |
| ------------ | ------------ | ------------ |
| in  | True if value/variable is found in the sequence  | 5 in x |
| not in  |True if value/variable is not found in the sequence | 5 not in x |
