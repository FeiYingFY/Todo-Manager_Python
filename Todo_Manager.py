class Todo:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, description):
        todo = Todo(description)
        self.todos.append(todo)

    def complete_todo(self, index):
        if index < 0 or index >= len(self.todos):
            print("无效的索引！")
            return
        todo = self.todos[index]
        todo.completed = True

    def get_todos(self):
        for i, todo in enumerate(self.todos):
            status = "完成" if todo.completed else "未完成"
            print(f"{i}. {status}: {todo.description}")


def main():
    todo_list = TodoList()

    while True:
        print("\n待办事项管理系统")
        print("1. 添加待办事项")
        print("2. 完成待办事项")
        print("3. 查看待办事项")
        print("4. 退出")

        choice = input("请选择操作：")

        if choice == "1":
            description = input("请输入待办事项的描述：")
            todo_list.add_todo(description)
            print("待办事项已添加！")

        elif choice == "2":
            index = int(input("请输入要完成的待办事项的索引："))
            todo_list.complete_todo(index)
            print("待办事项已完成！")

        elif choice == "3":
            todo_list.get_todos()

        elif choice == "4":
            print("退出系统，再见！")
            break

        else:
            print("无效的选择，请重新输入！")

if __name__ == "__main__":
    main()
