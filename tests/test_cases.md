# Test Cases

1. Test Case 1
Input values: Valid customer with age 30, income 80000, expenses 30000, EMI 10000, score 780, segment Premium.
Expected output or decision: Monthly savings 40000, Medium Value, Low Risk.
Reason for expected output: Savings 50% and EMI ratio 12.5% with score 780 satisfy the Low Risk thresholds. Income (80000) is below the 150000 High Value threshold, but it is above 60000, so the customer is Medium Value, not High Value.

2. Test Case 2
Input values: Valid customer with age 24, income 50000, expenses 30000, EMI 12000, score 680, segment Standard.
Expected output or decision: Medium Risk.
Reason for expected output: Credit score and savings are acceptable but not strong enough for Low Risk (savings% = 16%, fails the 25% Low Risk requirement).

3. Test Case 3
Input values: Valid customer with age 22, income 25000, expenses 18000, EMI 6000, score 590, segment Standard.
Expected output or decision: High Risk.
Reason for expected output: Credit score (590) is below the 650 minimum for Medium Risk, so the customer falls to High Risk regardless of savings.

4. Test Case 4
Input values: Product quantity 3, unit price 2000, discount 10, GST 18, delivery 120.
Expected output or decision: Final bill is Rs. 6,372.00. Delivery charge is waived.
Reason for expected output: Amount after discount (5400) exceeds the 5000 waiver threshold, so delivery is free even though a delivery charge of 120 was entered.

5. Test Case 5
Input values: Product quantity 1, unit price 1200, discount 5, GST 18, delivery 100.
Expected output or decision: Delivery charge of 100 is applied.
Reason for expected output: Amount after discount (1140) is below the 5000 waiver threshold, so the entered delivery charge is added to the final bill.

6. Test Case 6
Input values: Customer from Premium segment, High Value, savings 30 percent.
Expected output or decision: Premium Upsell Campaign.
Reason for expected output: Premium segment and High Value match the first campaign rule, which is checked before any other rule.

7. Test Case 7
Input values: Customer from Lucknow, savings 18 percent, Medium Value, segment Standard.
Expected output or decision: Cashback Campaign.
Reason for expected output: City is a target city and savings percentage (18%) is at least 15%, and the Premium Upsell rule does not apply first since segment is Standard.

8. Test Case 8
Input values: Customer age 20.
Expected output or decision: Loan Rejected.
Reason for expected output: Age below 21 fails the minimum age rule, before any other factor is checked.

9. Test Case 9
Input values: Age entered as -5.
Expected output or decision: Error message and re-entry prompt.
Reason for expected output: Negative age is invalid input.

10. Test Case 10
Input values: Credit score entered as 950.
Expected output or decision: Error message and re-entry prompt.
Reason for expected output: Credit score must stay within 300 to 900.

11. Test Case 11
Input values: Quantity entered as 0.
Expected output or decision: Error message and re-entry prompt.
Reason for expected output: Quantity must be greater than 0.

12. Test Case 12
Input values: Discount percentage entered as 120.
Expected output or decision: Error message and re-entry prompt.
Reason for expected output: Discount percentage must be within 0 to 100.

13. Test Case 13
Input values: Age 28, income 100000, existing EMI 5000, score 780, savings 25 percent, requested loan 200000.
Expected output or decision: Loan Approved.
Reason for expected output: Credit score (780), savings percentage (25%), and projected EMI ratio (13.33%) all clear the Approved thresholds (>=750, >=20%, <=40%).

14. Test Case 14
Input values: Age 26, income 50000, existing EMI 5000, score 680, savings 12 percent, requested loan 150000.
Expected output or decision: Manual Review Required.
Reason for expected output: Score (680) and savings (12%) clear the Manual Review thresholds (>=650, >=10%) and the projected EMI ratio (22.5%) is within 55%, but the savings percentage falls short of the 20% needed for full Approval.

15. Test Case 15
Input values: Customer segment Standard, city Pune, savings 8 percent, Medium Value.
Expected output or decision: Loan Offer Campaign.
Reason for expected output: Segment/value combination does not match Premium Upsell, city is not a target cashback city, but the customer is still Medium Value, so the Loan Offer Campaign rule applies.

16. Test Case 16
Input values: Customer segment Standard, city Pune, savings 5 percent, Low Value.
Expected output or decision: No Campaign.
Reason for expected output: Customer does not match the Premium Upsell rule, is not in a cashback city with sufficient savings, and is not Medium or High Value, so no campaign applies.

17. Test Case 17
Input values: Customer segment entered as "Business".
Expected output or decision: Error message and re-entry prompt.
Reason for expected output: "Business" is not one of the allowed segment values (Standard, Premium, Enterprise).
