-- LV2
-- GROUP BY
-- 진료과별 총 예약 횟수 출력하기

-- MySQL
SELECT
    MCDP_CD AS '진료과코드',
    COUNT(MCDP_CD) AS '5월예약건수'
FROM
    APPOINTMENT
WHERE
    APNT_YMD LIKE '2022-05%'
GROUP BY
    MCDP_CD
ORDER BY
    COUNT(MCDP_CD) ASC, MCDP_CD ASC

SELECT
    MCDP_CD as '진료과코드',
    COUNT(APNT_NO) as '5월예약건수'
FROM
    APPOINTMENT
WHERE
    DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY
    MCDP_CD
ORDER BY
    COUNT(APNT_NO) ASC, MCDP_CD ASC