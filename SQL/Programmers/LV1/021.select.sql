-- LV1
-- SELECT
-- 잔챙이 잡은 수 구하기

-- mysql
SELECT
    COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE LENGTH IS NULL;