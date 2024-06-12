SELECT * FROM MS_stock

WHERE "Open" NOT LIKE '%Dividend%'
AND "Open" NOT LIKE '%Stock%';
