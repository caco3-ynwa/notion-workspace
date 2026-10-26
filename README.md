# notion-workspace

同一个仓库容纳 Python 和 Go，各自管理依赖和构建。现有同步功能仍由 Python 实现，Go 目录为后续开发预留。

```text
notion-workspace/
├── python/
│   ├── pyproject.toml
│   ├── environment.yml
│   ├── src/notion_workspace/
│   ├── tests/
│   └── notebooks/
├── go/
│   ├── go.mod
│   ├── cmd/notion-sync/
│   └── internal/
├── scripts/
├── .env.example
├── .env                  # 本地配置，不提交
├── build/                # 构建中间文件，不提交
└── dist/                 # python/ 与 go/ 分开存放，不提交
```

## Python 开发

在仓库根目录执行，先激活项目环境。ECS 上继续使用 Python 3.12 的 `notion` 环境。
目录移动后，需要重新执行 editable 安装以更新环境内的源码位置：

```bash
python -m pip install -e ./python
```

需要打包时：

```bash
python -m pip install -e './python[build]'
```

Windows PowerShell 中可同样运行以上命令。在 VS Code 中仍需选择自己的 Conda 解释器。
已有终端需要重新打开以读取新的 PYTHONPATH。未安装项目时，也可以临时设置：

```powershell
$env:PYTHONPATH = "$PWD/python/src"
```

Linux 临时设置：`export PYTHONPATH="$PWD/python/src"`。

## 配置和运行

保留仓库根目录现有 `.env`；新环境可复制 `.env.example` 并填写自己的 Token。
未指定 `--env-file` 时，源码默认读取仓库根目录 `.env`；打包后读取可执行文件旁边的 `.env`。
显式指定文件会替换自动读取的默认配置，进程已有的同名环境变量始终优先。

```bash
python -m notion_workspace.main --data-sync sync_dota_records
python -m notion_workspace.main --env-file /root/config/notion.env --schedule
```

可用 `python -m notion_workspace.main --help` 查看参数。相对日志路径相对于当前工作目录；
ECS 建议在 `.env` 中为 LOG_FILE 配置绝对路径。

## 打包与部署

Linux ECS，在仓库根目录执行：

```bash
bash scripts/build_python.sh
./dist/python/notion-sync --env-file /root/config/notion.env --data-sync sync_dota_records
```

脚本在找到 `~/miniconda-24/etc/profile.d/conda.sh` 时自动激活 `notion` 环境；
可通过 CONDA_SH、CONDA_ENV_NAME、PYTHON_BIN 自定义。否则使用当前 Python 环境。
从任何目录调用脚本均可，路径由脚本自身定位。

Windows，在已激活的项目环境内执行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_python.ps1
.\dist\python\notion-sync.exe --data-sync sync_dota_records --env-file .\.env
```

Windows 与 Linux 需要分别打包，不会打包 `.env`。
Linux 安装前先停止旧程序，再运行 `bash scripts/install.sh`，它会打包并安装到 `/usr/local/bin/notion-sync`。
`bash scripts/run.sh /root/config/notion.env` 启动定时任务；
`bash scripts/run_dota_sync.sh /root/config/notion.env` 使用已安装命令执行一次同步。

## Go 开发

Go 模块路径：`github.com/caco3-ynwa/notion-workspace/go`。目前仅预留目录，没有迁移 Python 业务逻辑。
添加 `go/cmd/notion-sync/main.go` 后，在 `go/` 下运行 `go run ./cmd/notion-sync`；
或执行 `bash scripts/build_go.sh`，产物为 `dist/go/notion-sync`。

## 缓存与历史文件

`archives/` 和已有 `logs/` 保留在仓库根目录。旧的 Python 缓存和 egg-info 已随 src 移动，
不属于业务源码，不应提交；`.gitignore` 已忽略。已经被 Git 跟踪的缓存仍需单独取消跟踪。
