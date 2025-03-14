# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 숨어있는 숫자의 덧셈 (1)        | [숨어있는 숫자의 덧셈 (1)](https://school.programmers.co.kr/learn/courses/30/lessons/120851) |

### Source Code
```python
import re

def solution(my_string):
    words = my_string.split()
    answer = 0
    for word in words:
        numbers = re.findall(r'[1-9]', word)  
        answer += sum(map(int, numbers))
    
    return answer
```
