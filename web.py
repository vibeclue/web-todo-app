import streamlit as st
import functions


def add_todo():
    new_todo = st.session_state["new_todo"]
    if new_todo:
        todos.append(new_todo + '\n')
        functions.update_todo_list(todos)
        st.session_state["new_todo"] = ""

st.title("Наш список дел.")
st.subheader("Что нужно:")

# todos list
todos: list = functions.get_todos()
for index, todo in enumerate(todos):
    checked_todo = st.checkbox(todo, key=todo)
    # delete todo from the list
    if checked_todo:
        todos.pop(index)
        functions.update_todo_list(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo: ",
              label_visibility='hidden',
              placeholder="Введи напоминалку...",
              on_change=add_todo,
              key="new_todo")
