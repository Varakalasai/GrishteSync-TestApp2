# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import gradio as gr
from gradio import Blocks
import json

with Blocks() as demo:
    gr.Markdown("<h1>Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com</h1>")
    gr.Markdown("<img src='https://i.ibb.co/RGmb4FKk/1781072041102.png' width='100'>")
    board = [
        {"id": 1, "title": "Card 1", "description": "This is card 1", "status": "todo"},
        {"id": 2, "title": "Card 2", "description": "This is card 2", "status": "in_progress"},
        {"id": 3, "title": "Card 3", "description": "This is card 3", "status": "done"}
    ]
    columns = ["todo", "in_progress", "done"]
    with gr.Columns() as columns_component:
        for column in columns:
            with gr.Column() as column_component:
                gr.Markdown(f"## {column.capitalize()}")
                with gr.Box() as box:
                    for card in board:
                        if card['status'] == column:
                            with gr.Box() as card_component:
                                gr.Markdown(f"### {card['title']}")
                                gr.Markdown(card['description'])
    gr.Markdown("<h1>Footer: Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com</h1>")
    gr.Markdown("<img src='https://i.ibb.co/RGmb4FKk/1781072041102.png' width='100'>")
demo.launch(server_name='0.0.0.0', server_port=7860)