import streamlit as st
import pandas as pd

def table(df):
    # Add a serial number column
    df.insert(0, 'Serial No', range(1, len(df) + 1))

    # Define CSS styles for the table
    table_style = """
        <style>
        table.custom-table {
            font-family: Arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }
        table.custom-table thead th {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 8px;
            text-align: left;
        }
        table.custom-table tbody td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        table.custom-table tbody tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        table.custom-table tbody tr:hover {
            background-color: #ddd;
        }
        </style>
    """

    # Display the styled table dynamically
    st.markdown(table_style, unsafe_allow_html=True)

    # Generate HTML for the table
    table_html = '<table class="custom-table"><thead><tr>'
    table_html += '<th>#</th>'
    table_html += ''.join([f'<th>{col}</th>' for col in df.columns[1:]])
    table_html += '</tr></thead><tbody>'
    for row in df.itertuples(index=False):
        table_html += '<tr>'
        table_html += ''.join([f'<td>{cell}</td>' for cell in row])
        table_html += '</tr>'
    table_html += '</tbody></table>'
    return table_html
    # Display the table using HTML
    # st.write(table_html, unsafe_allow_html=True)