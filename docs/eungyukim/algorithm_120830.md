# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 양꼬치         | [양꼬치](https://school.programmers.co.kr/learn/courses/30/lessons/120830) |

### Source Code
```python
def solution(n, k):
    x = (int)(n/10)
    answer = n * 12000 + (k - x) * 2000
    return answer
```
