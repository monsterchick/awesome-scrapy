import os


class FileDirectory():
    def __init__(self):
        pass
    def get_currentdir(self):
        currentdir = os.getcwd()
        return currentdir
    def get_rootdir(self):
        """
        通过查找项目标识文件来确定项目根目录
        常见的项目标识包括 .git, setup.py, requirements.txt 等

        Returns:
            str: 项目根目录路径
        """
        current_path = os.getcwd()

        # 定义项目标识文件/目录
        project_markers = ['.git', 'setup.py', 'requirements.txt', 'pyproject.toml', 'README.md']

        # 从当前目录向上查找
        while current_path != os.path.dirname(current_path):  # 未到达根目录
            for marker in project_markers:
                if os.path.exists(os.path.join(current_path, marker)):
                    # print("项目根目录：", current_path)
                    return current_path
                # print("未找到项目标识文件：", marker)
            current_path = os.path.dirname(current_path)

        # 如果没找到标识，返回当前工作目录
        return current_path
    def get_filedir(self, filename):
        """
        在目录中递归搜索文件
        :param filename: 要搜索的文件名
        :return: 文件的绝对路径，如果未找到则返回 None
        """
        if not filename:
            raise ValueError("文件名不能为空")
        search_path = self.get_rootdir()
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                filedir = os.path.join(root, filename)
                return filedir
