import os
import time


class Globals:
  hub_dir: str = 'Holy-Unblocker'
  van_dir: str = 'Vanadium'
  lud_dir: str = 'Ludicrous'
  met_dir: str = 'Metallic'
  holy_ub: list = ['npm install', 'npm start']
  vanadium: list = ['npm install', 'npm start']
  ludicrous: list = ['npm install', 'npm run build', 'npm start']
  metallic: list = ['npm install', 'npm run build', 'npm start']


def run_npm_commands(command_list: list, cd_dir: str = '') -> None:
  if cd_dir != '':
    os.chdir(cd_dir)

  for cmd in command_list:
    print(f'Running command: "{cmd}".')
    print('---------------------------------------------')
    os.system(cmd)
    print('---------------------------------------------')


def determine_network() -> None:
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
    ticker: int = 0
    for item in os.listdir(f'{cur_dir}/sites'):
      if os.path.isdir(f'{cur_dir}/sites/{item}'):
        ticker += 1
        item: str = item.replace('\\', '/')
        print(f'{ticker} | {item}')
        folder_list.append(item)

    usr_input: int = int(input(
      f'\nWhat site would you like to run? (1-{len(folder_list)}): '
    ))
    if not str(usr_input).isdigit():
      print('Please provide a digit.')
      time.sleep(2)
      determine_network()
    if usr_input > len(folder_list) or usr_input < 1:
      print('Please provide a valid digit.')
      time.sleep(2)
      determine_network()

    else:
      print(f'({usr_input}) : {folder_list[int(usr_input) - 1]}\n')
      folder: int = folder_list[int(usr_input) - 1]
      if folder == Globals.hub_dir:
        preset: list = Globals.holy_ub

      elif folder == Globals.van_dir:
        preset: list = Globals.vanadium

      elif folder == Globals.lud_dir:
        preset: list = Globals.ludicrous

      elif folder == Globals.met_dir:
        preset: list = Globals.metallic

      run_npm_commands(preset, f'sites/{folder}')


determine_network()
