from flask import Flask

# 初始化Flask应用
app = Flask(__name__)

# 定义路由：访问网站根目录（/）时触发
@app.route('/')
def home():
    return "Hello, Flask! 这是通过 app/main.py 运行的服务"

# 启动服务器（仅在本地运行时生效，部署时由Render等平台管理）
if __name__ == '__main__':
    # 允许外部访问（host=0.0.0.0），端口使用环境变量或默认5000
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
