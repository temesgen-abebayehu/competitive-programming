class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions_by_name = defaultdict(list)
        invalid = []  

        # First pass: parse all transactions
        for trans in transactions:
            name, time_str, amount_str, city = trans.split(',')
            time, amount = int(time_str), int(amount_str)
            transactions_by_name[name].append((time, amount, city, trans))

        # Second pass: check all conditions
        for name, trans_list in transactions_by_name.items():
            # Check each transaction
            for i, (time1, amount1, city1, trans1) in enumerate(trans_list):
                # Condition 1: Check amount
                if amount1 > 1000:
                    invalid.append(trans1) 
                     # Add to list, duplicates allowed
                    continue
                
                # Condition 2: Check for time/city conflicts                
                for j, (time2, amount2, city2, trans2) in enumerate(trans_list):
                    if city1 != city2 and abs(time1 - time2) <= 60:
                        invalid.append(trans1)
                        break

        return invalid