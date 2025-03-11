# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 옷가게 할인 받기         | [옷가게 할인 받기](https://school.programmers.co.kr/learn/courses/30/lessons/120818) |

### Source Code
```python
def solution(price):
    if price >= 500000:
        discount = 0.20
    elif price >= 300000:
        discount = 0.10
    elif price >= 100000:
        discount = 0.05
    else:
        discount = 0.0
    
    return int(price * (1 - discount))
```
