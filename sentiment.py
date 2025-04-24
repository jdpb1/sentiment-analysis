from transformers import pipeline

# Load the classification pipeline with the specified model
pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

# Classify a new sentence
sentence = "I don't know if this product is good or bad"
result = pipe(sentence)

# Print the result
print(result)
