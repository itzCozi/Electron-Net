import os
import time


class Globals:
  hub_dir: str = 'sites/Holy-Unblocker'
  van_dir: str = 'sites/Vanadium'
  lud_dir: str = 'sites/Ludicrous'
  holy_ub: list = ['npm install', 'npm start']
  vanadium: list = ['npm install', 'npm start']
  ludicrous: list = ['npm install', 'npm run build', 'npm start']


def run_npm_commands(command_list: list, cd_dir: str = '') -> None:
  if cd_dir != '':
    os.chdir(cd_dir)

  for cmd in command_list:
    print(f'Running command: "{cmd}".')
    print('---------------------------------------------')
    os.system(cmd)
    print('---------------------------------------------')


def determine_network() -> None:
  # have to fix the preset calls
  cur_dir: str = os.getcwd().replace('\\', '/')
  dir_list: list = cur_dir.split('/')
  if dir_list[-1] == Globals.hub_dir:
    run_npm_commands(Globals.holy_ub)

  elif dir_list[-1] == Globals.van_dir:
    run_npm_commands(Globals.vanadium)

  elif dir_list[-1] == Globals.lud_dir:
    run_npm_commands(Globals.ludicrous)

  else:
    folder_list: list = []
    for item in os.listdir(f'{cur_dir}/sites'):
      if os.path.isdir(f'{cur_dir}/sites/{item}'):
        item: str = item.replace('\\', '/')
        print(item)
        folder_list.append(item)

    usr_input: str = input(
      f'\nWhat site would you like to run? (1-{len(folder_list)}): '
    )
    if not usr_input.isdigit():
      print('Please provide a digit.')
      time.sleep(2)
      determine_network()

    else:
      folder: int = folder_list[int(usr_input) - 1]
      if folder == Globals.hub_dir:
        preset: list = Globals.holy_ub
      if folder == Globals.van_dir:
        preset: list = Globals.vanadium
      if folder == Globals.lud_dir:
        preset: list = Globals.ludicrous
      run_npm_commands(preset, folder)


determine_network()
