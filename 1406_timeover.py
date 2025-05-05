import sys

input_data = sys.stdin.readline

init_str = input_data().rstrip()

class Editor:
    def __init__(self, init_str):
        self.current_str = init_str
        self.cursor_pos = len(self.current_str)
    
    def run_command(self, cmd_type, insert=None):
        if cmd_type == 'L':
            # 커서가 맨 앞이 아니면 왼쪽으로 이동
            if self.cursor_pos > 0:
                self.cursor_pos -= 1
        
        elif cmd_type == 'D':
            # 커서가 맨 뒤가 아니면 오른쪽으로 이동
            if self.cursor_pos < len(self.current_str):
                self.cursor_pos += 1
        
        elif cmd_type == 'B':
            # 커서가 맨 앞이 아니면 왼쪽 문자 삭제
            if self.cursor_pos > 0:
                self.current_str = self.current_str[:self.cursor_pos-1] + self.current_str[self.cursor_pos:]
                # 문자열을 새 메모리에 복사한다음 문자열 연결하는 방식인데
                # 새 문자열을 자꾸 새로 만드니까 메모리도 비효율적이고
                # 특히 +로 문자열 연결할 때 len() 만큼 시간이 소요된다고 함.
                self.cursor_pos -= 1  # 커서 왼쪽으로 이동
        
        elif cmd_type == 'P':
            # 커서 왼쪽에 문자 추가
            self.current_str = self.current_str[:self.cursor_pos] + insert + self.current_str[self.cursor_pos:]
            self.cursor_pos += 1  # 커서 오른쪽으로 이동

editor = Editor(init_str)
M = int(input_data().rstrip())

for _ in range(M):
    command = input_data().rstrip()
    if len(command) >= 2:
        editor.run_command(command[0], command[2])
    else:
        editor.run_command(command[0])
        
print(editor.current_str)