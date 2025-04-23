import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# 创建 MCP Server
mcp = FastMCP("TXT 文件统计器")


@mcp.tool()
def count_desktop_txt_files() -> int:
    """获取桌面上txt文件的数量"""
    # Get the desktop path
    username = os.getenv("USER") or os.getenv("USERNAME")
    desktop_path = Path(f"C:/Users/{username}/Desktop")

    # Count .txt files
    txt_files = list(desktop_path.glob("*.txt"))
    return len(txt_files)


@mcp.tool()
def list_desktop_txt_files() -> str:
    """读取桌面上的txt文件，返回文件列表"""
    # Get the desktop path
    username = os.getenv("USER") or os.getenv("USERNAME")
    desktop_path = Path(f"C:/Users/{username}/Desktop")

    # Get all .txt files
    txt_files = list(desktop_path.glob("*.txt"))

    # Return the filenames
    if not txt_files:
        return "No .txt files found on desktop."

    # Format the list of filenames
    file_list = "\n".join([f"- {file.name}" for file in txt_files])
    return f"Found {len(txt_files)} .txt files on desktop:\n{file_list}"


@mcp.tool()
def read_file_content() -> str:
    """读取桌面上txt文件的内容"""
    # Get the desktop path
    username = os.getenv("USER") or os.getenv("USERNAME")
    desktop_path = Path(f"C:/Users/{username}/Desktop")

    # Get all .txt files
    txt_files = list(desktop_path.glob("*.txt"))
    file_contents = ''
    for txt_file in txt_files:
        try:
            with open(txt_file, "r", encoding='utf-8') as file:
                content = file.read()
                file_contents += f"File: {txt_file.name}\nContent:\n{content}\n\n"
        except FileNotFoundError:
            print("file not exist")
    return file_contents


if __name__ == "__main__":
    # Initialize and run the server
    print('[mcp server] fileserver init')
    mcp.run()
