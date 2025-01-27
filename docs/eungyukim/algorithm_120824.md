# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 짝수 홀수 개수         | [짝수 홀수 개수](https://school.programmers.co.kr/learn/courses/30/lessons/120824) |

### Source Code
```python
def solution(num_list):
    even_number = 0
    odd_number = 0
    for n in num_list:
        if n % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
        
    answer = [even_number, odd_number]
    return answer
```
