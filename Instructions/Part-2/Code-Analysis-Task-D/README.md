# Resume Analysis

## Your Task

Complete the documentation in the Jupyter with clear descriptions of what is happening in each cell. There is no need for you to code as that part is already done for you. You only need to document what is happening. Carefully consider the set data structure is used when operating on Unique and Non-unique elements and also for comparison purposes.

## Helpful Information

This script will analyze a resume text file via the following steps:

* Read the resume file as text using the `with` statement.
* Create a list containing all words in the resume.
  * Convert each word to lowercase to normalize the data.
* Use `split` to remove and trailing punctuation so only words remain.
* Create a set of unique words from the resume using `set()`.
* Use set operations to filter out all remaining punctuation from the set of words.
  * Create a set from `string.punctuation` to use in the difference operation.
* Use the cleaned set (no punctuation) to find all of the words from the resume that match the required skills.
* Use the cleaned set (no punctuation) to find all of the words that match the desired skills.
* Count the number of occurrences for each word in the resume and print the top 10 occuring words in the resume.
  * Use a dictionary data structure to hold the counts for each word.
  * Remove punctuation and [stop words](https://en.wikipedia.org/wiki/Stop_words)
