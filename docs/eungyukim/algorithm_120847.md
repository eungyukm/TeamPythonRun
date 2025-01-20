# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 최댓값 만들기(1)        | [최댓값 만들기(1)](https://school.programmers.co.kr/learn/courses/30/lessons/120847) |

### Source Code
```python
def solution(numbers):
    maxValue1 = max(numbers)
    numbers.remove(maxValue1)
    maxValue2 = max(numbers)
    return maxValue1 * maxValue2
```
