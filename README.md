🚀 LeetCode Solutions in Python

Welcome to my **LeetCode Solutions** repository! 🎯
This repo contains my Python implementations of popular LeetCode problems, categorized by topic and difficulty.
It’s part of my journey to strengthen **problem-solving skills** and prepare for **coding interviews**.



 📂 Repository Structure


leetcode-solutions/
│── arrays/
│── strings/
│── linkedlist/
│── dynamic_programming/
│── ...
```

* arrays/ → Problems related to arrays
* strings/ → Problems related to string manipulation
* linkedlist/ → Linked list challenges
* dynamic_programming/ → DP-based solutions
* More categories will be added as I progress!



 🛠️ How to Use

1. Clone this repository:
   
   git clone https://github.com/ahmadmayar89/leetcode-solutions.git
 
2. Navigate to the folder of your choice.
3. Run the solution file with Python:

   python filename.py
   

 💡 Example Problem

Two Sum (Easy)
Find indices of two numbers such that they add up to the target.


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i


🎯 Goals

* ✅ Upload Python solutions regularly
* ✅ Organize problems by **topic** and **difficulty**
* 🔜 Add **C++ solutions**
* 🔜 Add **unit tests** for verification



 🤝 Contributing

This is primarily for my personal learning, but suggestions and improvements are welcome!
Feel free to open an **issue** or a **pull request**.


