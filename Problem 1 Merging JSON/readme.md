## Code Complexity
Note: The currrent code is dynamic and can merge JSON with different keys

Assumptions:
If a input file contains n keys 
And the output file already contains m keys
We are checking m*n times to find if the keys are matching
And if there are k number of input files then this operation repeats for (k-1) times

If we assume that all k files have the same n common keys then
The complexity is O (n * n * k)

Specific to implementation:
But since we are using Dicts, getting value of key operation is O(1)
So checking if key is present is reduced from O(m*n) to just O(n)

Finally the complexity is O(n * k)


### Sample CLI command
python mergeUtil.py 'C:\\Users\jalahith\Desktop\Assignment Tuple\data' data out 100