
"""
# 1. 进入本地项目目录
cd /path/to/your/local-project

# 2. 初始化本地仓库
git init

# 3. 添加所有文件到暂存区（空项目可跳过，但建议创建初始文件）
touch README.md  # 创建初始文件
git add .

# 4. 提交初始版本
git commit -m "Initial commit"

# 5. 添加远程仓库地址
git remote add origin https://github.com/your-username/your-repo.git

# 6. 验证远程仓库是否添加成功
git remote -v

# 7. 推送代码到远程仓库（首次推送需设置上游分支）
git push -u origin main  # 或 master（根据你的默认分支名）


"""