from collections import Counter             
import math      
import string    
import matplotlib.pyplot as plt

# Load the data (syllabus for AI&ML training) - reduced to two days

documents = [
    "Shallow copy and deep copy Python Indentation Comments Casting Find the address of variable Get input from user",
    "Operator and copy  Looping"
]

# Function to create term-frequency vectors with basic preprocessing
def create_term_frequency(doc): 
    # Convert to lowercase and remove punctuation]
    doc = doc.lower().translate(str.maketrans("", "", string.punctuation))        
    words = doc.split()         
    return Counter(words)

# Function to compute cosine similarity
def cosine_similarity(vec1, vec2):
    common = set(vec1.keys()) & set(vec2.keys())
    if not common:
        return 0.0
    dot_product = sum(vec1[word] * vec2[word] for word in common)
    norm1 = math.sqrt(sum(freq * freq for freq in vec1.values()))
    norm2 = math.sqrt(sum(freq * freq for freq in vec2.values()))
    return dot_product / (norm1 * norm2) if norm1 * norm2 != 0 else 0.0

# Load and process data
tf_vectors = [create_term_frequency(doc) for doc in documents]

# Compare Day 1 and Day 2
vec_day1 = tf_vectors[0]  # Day 1
vec_day2 = tf_vectors[1]  # Day 2

dot_product = sum(vec_day1[word] * vec_day2[word] for word in set(vec_day1.keys()) & set(vec_day2.keys()))
similarity = cosine_similarity(vec_day1, vec_day2)
distance = 1 - similarity

print(f"Dot Product between Day 1 and Day 2: {dot_product}")
print(f"Cosine Similarity between Day 1 and Day 2: {similarity:.3f}")
print(f"Cosine Distance between Day 1 and Day 2: {distance:.3f}")

# Visualization using Matplotlib
days = ['Day 1', 'Day 2']
similarities = [1.0, similarity]  # Default similarity to 1.0 for distance, adjusted for plot
plt.scatter(range(len(days)), similarities, color='blue') 
plt.xticks(range(len(days)), days)
plt.ylabel('Similarity (1 - Distance)')
plt.title('Document Similarity Visualization')
plt.ylim(0, 1.1)  # Set y-axis limit from 0 to 1.1 for clarity
for i, txt in enumerate(days):
    plt.annotate(txt, (i, similarities[i]), xytext=(0, 5), textcoords='offset points', ha='center')
plt.show()
