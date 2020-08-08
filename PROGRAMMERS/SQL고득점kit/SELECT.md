### **SELECT**

1. 모든 레코드 조회하기

```
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

1. 역순 정렬하기

```
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```

1. 아픈 동물 찾기

```
SELECT animal_id, name
FROM animal_ins
WHERE intake_condition = 'sick'
ORDER BY animal_id
```

1. 어린 동물 찾기

```
SELECT animal_id, name
FROM animal_ins
WHERE intake_condition != 'aged'
ORDER BY animal_id
```

1. 동물의 아이디와 이름

```
SELECT animal_id, name
FROM animal_ins
ORDER BY animal_id
```

1. 여러 기준으로 정렬하기

```
SELECT animal_id, name, datetime
FROM animal_ins
ORDER BY name ASC, datetime DESC
```

1. 상위 n개 레코드

```
SELECT name
FROM animal_ins
ORDER BY datetime
LIMIT 1
```

### **SUM,MAX,MIN**

1. 최댓값 구하기

```
SELECT datetime
FROM animal_ins
ORDER BY datetime DESC
LIMIT 1
```

1. 최솟값 구하기

```
SELECT datetime
FROM animal_ins
ORDER BY datetime ASC
LIMIT 1
```

1. 동물 수 구하기

```
SELECT COUNT(*)
FROM animal_ins
```

1. 중복 제거하기

```
SELECT COUNT(DISTINCT name)
FROM animal_ins
```

### **GROUP BY**

1. 고양이와 개는 몇 마리 있을까 ✔️

```
SELECT animal_type, COUNT(animal_type)
FROM animal_ins
GROUP BY animal_type
ORDER BY animal_type
```

1. 동명 동물 수 찾기

```
SELECT name, COUNT(name) as 'count'
FROM animal_ins
GROUP BY name
HAVING count > 1
ORDER BY name 
```

> GROUP으로 묶은 후에는 GROUP에 조건을 줄때는 WHERE절이 아니라 HAVING절을 사용하게 됩니다.