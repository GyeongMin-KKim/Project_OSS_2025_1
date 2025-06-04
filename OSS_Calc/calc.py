import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")  # 높이 조금 늘림

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 목록에 변환 버튼 둘 다 추가
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['HP→W', 'W→HP', '=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'HP→W':
            # 마력 → 와트 변환
            try:
                hp = float(self.expression)
                w = hp * 745.7
                self.expression = f"{w:.2f} W"
            except ValueError:
                self.expression = "에러"
        elif char == 'W→HP':
            # 와트 → 마력 변환
            try:
                # 입력에 단위 붙어있으면 떼기
                w_str = self.expression.split()[0]
                w = float(w_str)
                hp = w / 745.7
                self.expression = f"{hp:.2f} HP"
            except ValueError:
                self.expression = "에러"
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
