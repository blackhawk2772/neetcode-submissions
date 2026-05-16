from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        size = [1] * len(accounts)

        email_to_account = {}

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return

            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]

        # Step 1: Union accounts that share an email
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]

                if email not in email_to_account:
                    email_to_account[email] = i
                else:
                    union(i, email_to_account[email])

        # Step 2: Group emails by final parent account
        account_emails = defaultdict(list)

        for email, account_index in email_to_account.items():
            root = find(account_index)
            account_emails[root].append(email)

        # Step 3: Build answer
        res = []

        for account_index, emails in account_emails.items():
            name = accounts[account_index][0]
            res.append([name] + sorted(emails))

        return res