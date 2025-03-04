# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 모음 제거         | [모음 제거](https://school.programmers.co.kr/learn/courses/30/lessons/120849) |

### Source Code
```python
def solution(my_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    result_list = []
    
    for char in my_string:
        if char not in vowels:
            result_list.append(char)
    
    answer = ''.join(result_list)
    return answer
```
