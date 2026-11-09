"""A few lines of text mining: tokenize, drop stopwords, count words and bigrams.

Run it with:  python text_mining.py
Uses only the Python standard library.
"""
import re
from collections import Counter

text = """Text mining turns unstructured text into structured data.
Text mining helps us find patterns, topics and keywords in large text collections,
and large language models build on many of the same text mining ideas."""

STOPWORDS = {"a", "an", "and", "the", "in", "into", "of", "on", "us", "same", "many"}

# 1. Tokenize: lowercase the text and keep only runs of letters.
tokens = re.findall(r"[a-z]+", text.lower())

# 2. Filter: remove common words that carry little meaning.
words = [t for t in tokens if t not in STOPWORDS]

# 3. Count single words (term frequency).
print("Top words:  ", Counter(words).most_common(5))

# 4. Count word pairs (bigrams) to find phrases like "text mining".
bigrams = Counter(zip(words, words[1:]))
print("Top bigrams:", bigrams.most_common(3))
