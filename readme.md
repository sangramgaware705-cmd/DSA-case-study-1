# Case Study: E-Commerce Product Sorting & Google Calendar Event Scheduling

## 1. Introduction

This case study demonstrates two fundamental algorithmic design paradigms implemented in Python:

1. **Divide and Conquer Strategy:** Applied to an **E-Commerce Product Catalog** to efficiently sort large volumes of products by attributes such as price and rating.
2. **Greedy Strategy:** Applied to a **Google Calendar Application** to solve the Interval Scheduling Optimization problem, maximizing non-overlapping event appointments within a single workday.

---

## 2. Objectives

* Understand and implement **Merge Sort** and **Quick Sort** using the Divide and Conquer strategy.
* Analyze time complexity and performance advantages of $\mathcal{O}(n \log n)$ sorting algorithms for large-scale e-commerce datasets.
* Implement the **Interval Scheduling Algorithm** using a Greedy approach.
* Demonstrate proof of optimality for greedy choice selection (*Earliest Finish Time First*).

---

## 3. Case Study 1: E-Commerce Product Sorting (Divide and Conquer)

### Problem Description
E-commerce platforms (like Amazon or eBay) display thousands of products that customers filter by price, rating, or popularity. Using suboptimal $\mathcal{O}(n^2)$ algorithms (e.g., Bubble Sort) causes severe rendering lag. 

### Algorithmic Breakdown

#### A. Merge Sort
* **Divide:** Split the array of products into two halves at index $\lfloor n/2 \rfloor$.
* **Conquer:** Recursively sort both sub-lists.
* **Combine:** Merge the two sorted halves into a single ordered list.
* **Property:** Guaranteed $\mathcal{O}(n \log n)$ performance and stable sorting.

#### B. Quick Sort
* **Divide:** Pick a pivot product (e.g., median element) and partition products into sub-arrays: elements smaller than the pivot and elements greater than the pivot.
* **Conquer:** Recursively sort left and right partitions.
* **Combine:** Concatenate `quick_sort(left) + [pivot] + quick_sort(right)`.

---

## 4. Case Study 2: Google Calendar Scheduling (Greedy Strategy)

### Problem Description
Users receive overlapping meeting requests throughout the day. Google Calendar needs to select the maximum number of mutually compatible (non-overlapping) events.

### Algorithmic Breakdown (Earliest Finish Time First)

1. **Greedy Choice Criterion:** Always select the event that finishes earliest ($f_i$). This leaves the maximum possible remaining time for subsequent events.
2. **Algorithm Steps:**
   * Sort all candidate events by their ending time in ascending order.
   * Select the first event.
   * Iterate through remaining events, selecting an event if its start time $s_j \ge f_{last\_selected}$.

---

## 5. Summary of Complexity & Efficiency

| Problem / Domain | Strategy | Algorithm | Time Complexity | Space Complexity |
|---|---|---|---|---|
| E-Commerce Sorting | Divide & Conquer | Merge Sort | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ |
| E-Commerce Sorting | Divide & Conquer | Quick Sort | Average: $\mathcal{O}(n \log n)$<br>Worst: $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ |
| Google Calendar | Greedy Strategy | Interval Scheduling | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ or $\mathcal{O}(n)$ |

---

## 6. How to Run

1. Make sure Python 3.x is installed on your computer.
2. Execute the Python script:

```bash
python ecommerce_calendar.py
```

---

## 7. Sample Output

### Product Sorting (Merge Sort - Low to High Price)
```text
--- Sorted Products by Price (Merge Sort - Low to High) ---
[P107] USB-C Hub              | Price: $18.45   | Rating: 4.1/5.0
[P109] Webcam 1080p           | Price: $45.20   | Rating: 3.8/5.0
[P100] Wireless Earbuds       | Price: $89.99   | Rating: 4.5/5.0
[P101] Gaming Laptop          | Price: $1150.00 | Rating: 4.8/5.0
```

### Calendar Optimization (Greedy - Maximize Non-Overlapping Meetings)
```text
--- Optimized Calendar Schedule (Greedy - Max non-overlapping) ---
[E1] Team Daily Standup        | Time: 09:00 - 10:00
[E4] 1-on-1 Sync               | Time: 11:00 - 12:00
[E5] Lunch with Mentor         | Time: 12:00 - 13:00
[E7] Architecture Review       | Time: 13:00 - 14:00
[E8] Code Refactoring Session  | Time: 14:00 - 15:30

Total Scheduled Events: 5 / 8
```

---

## 8. Conclusion

This case study demonstrates how selecting appropriate algorithmic strategies directly optimizes real-world computational systems. **Divide and Conquer** guarantees efficient dataset organization for consumer applications, while **Greedy Strategies** provide provably optimal solutions for temporal scheduling and resource allocation problems.