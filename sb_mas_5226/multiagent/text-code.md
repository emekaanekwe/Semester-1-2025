## On-policy: 
The agent updates Q-values based on actions taken from its current policy (e.g., ε-greedy).




λ (lambda): Controls how much credit to assign to prior states/actions. Recent ones get more credit.




Eligibility trace (E[s][a]): A decaying memory of how recently each (s, a) was visited.





Q-value update: All Q-values are updated proportionally to their 
eligibility and the TD error.