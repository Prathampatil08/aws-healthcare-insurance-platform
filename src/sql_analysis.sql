-- Query 1: Top 10 most expensive drugs in 2024
SELECT brnd_name, tot_spndng_2024 
FROM medicare_drugs 
ORDER BY tot_spndng_2024 DESC 
LIMIT 10;

-- Query 2: Total Medicare spending per year
select sum(tot_spndng_2020) as "2020_total", sum(tot_spndng_2021) as "2021_total", sum(tot_spndng_2022) as "2022_total", sum(tot_spndng_2023) as "2023_total", sum(tot_spndng_2024) as "2024_total" from medicare_drugs;

-- Query 3: New vs existing drugs count
SELECT is_new_drug, COUNT(*)
FROM medicare_drugs
GROUP BY is_new_drug;

-- Query 4: Average spending per patient by drug type
SELECT is_new_drug, AVG(avg_spndng_per_bene_2024) FROM medicare_drugs GROUP BY is_new_drug;

-- Query 5: CTE with window function - top 5 drugs by rank
 with top_drugs as (
SELECT
    brnd_name,
    tot_spndng_2024,
    RANK() OVER (ORDER BY tot_spndng_2024 DESC) as spending_rank
FROM medicare_drugs
) select * from top_drugs where spending_rank <=5;


