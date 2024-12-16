-- LV1
-- SUM, MAX, MIN
-- 가장 비싼 상품 구하기

-- oracle
SELECT
    MAX(PRICE) MAX_PRICE
FROM PRODUCT

-- mysql
SELECT
*
FROM PRODUCT
ORDER BY PRICE DESC
limit 1