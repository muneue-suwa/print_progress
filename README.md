# Print Progress

進捗を表示するパッケージである．

## Installation

```bash:installation
pip install -e [THIS_GITHUB_REPOSITORY_URL]
```

## Example

使用例と動作内容をしめす．

```python:example
from time import sleep
from print_progress.print_progress import PrintProgress

pp = PrintProgress("Example", 10)
pp.print_start()
for i in range(10):
    pp.print_progress(i + 1)
    sleep(1)
pp.print_completed()
```

![example](image/example.gif)
