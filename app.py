from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

tasks = load_tasks()

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        save_tasks(tasks)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks): 
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)