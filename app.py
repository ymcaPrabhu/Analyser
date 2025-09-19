# app.py
import gradio as gr
from app_core import analyze

def predict(text):
    out = analyze(text)
    return f"{out['label']} ({out['score']:.2%})"

with gr.Blocks() as demo:
    gr.Markdown("# 📊 Mini Sentiment Analyzer")
    inp = gr.Textbox(label="Enter text")
    btn = gr.Button("Analyze")
    out = gr.Textbox(label="Prediction", interactive=False)
    btn.click(predict, inp, out)
    inp.submit(predict, inp, out)

if __name__ == "__main__":
    demo.launch()
