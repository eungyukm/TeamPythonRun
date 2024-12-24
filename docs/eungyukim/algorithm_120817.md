# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 배열의 평균값          | [배열의 평균값](https://school.programmers.co.kr/learn/courses/30/lessons/120817) |

### Source Code
```python
def solution(numbers):
    sum = 0
    for n in numbers:
        sum += n
    answer = sum / len(numbers)
    return answer
```
