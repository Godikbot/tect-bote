import subprocess


async def update(*_) -> str:
    commands = [
        'git fetch',
        'git reset --hard origin/master'
    ]
    fail = False
    for cmd in commands:
        if subprocess.run(cmd, shell=True).returncode != 0:
            fail = True
    return '❌ Что-то пошло не так' if fail else (
        "Обновка прошла успешно, перезагрузить можно командой\nCtrl+C\nзатем пишите\npython3 start.py "
    )
