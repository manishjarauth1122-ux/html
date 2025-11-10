from transformers import pipeline

summarizer = pipeline("summarization")
text = """India is a country with a rich cultural heritage..."""
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
print(summary[0]['summary_text'])