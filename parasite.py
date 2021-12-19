# by billythegoat356

# https://github.com/billythegoat356/Parasite



from os.path import isfile
from pystyle import Anime, Colorate, Colors, Center, System, Write


class function:
    ...


class Parasite:


    def run(file: str, mode: function) -> tuple:
        with open(file=file, mode='r', encoding=Parasite.encoding) as f:
            content = f.read()


        result = mode(content=content)


        with open(file='new-' + (file.split('\\')[-1] if '\\' in file else file.split('/')[-1]), mode='w', encoding=Parasite.encoding) as f:
            f.write(result)

        return (len(content), len(result))

    spchar = "ඝ"
    encoding = "utf-8"

    def compress(content: str) -> str:
        result = ""

        while True:
            char = content[0]
            if len(content) == 1:
                result += char
                break
            content = content[1:]
            x = 1
            while content[0] == char:
                if len(content) == 1:
                    break
                x += 1
                content = content[1:]
            if x > 3:
                result += f'{char}{Parasite.spchar}{x}{Parasite.spchar}'
            else:
                result += char * x
        return result

    def decompress(content: str) -> str:
        # a finir
        result = ""
        ncontent = content.split(Parasite.spchar)

        while True:
          if len(ncontent) == 1:
            result += ncontent[0]
            break
          else:
            result += ncontent[0][:-1]
            result += ncontent[0][-1] * int(ncontent[1])
            ncontent = ncontent[2:]
            
        return result



banner = r'''
                                  _      ____ _                   
                             --'""             """"""---              
                   _   --""                               `-                
                 -'           :'::::;:::%: ::::::_;;:        `- 
              -'         ::::''"''   _   ---'"""":::+;_::       `        
            '        ::::'      _ -""               :::)::        ` 
                  ;:::'     _ -'                       f::'::    o  _
        /      :::%'      -"                         -   ::;;:    /" "x
       '  "":: ::'     -"     _ --'"""-            (   )  :: ::  |_ -' |
      '    ::;:'     '      -"  d@@b    \           `-'   ::%::   \_ _/     
     '    :,::'    /     _'    8@@@@8   j       -'       :::::      " o
    |    : %:'    j     (_)    `@@@P'   '    -"         :: ::       f
    |    ::::     (        -  ____   -'   -"           ::::'       /
    |    `:`::    `                   --'            ::'::        /
    j     `:::::    `- _____   ---""              ::%:::'        '   
     \      :: :%                               :,::::'        '
      \       `:::`:                      :::: ::::'        -'           
       \        ``:::%::`::       :::::%:: ::::''        -'
        `           ``::::::%:::: ::;;:::::'"'      _ -'           
          `-                ````''"''           _ -'                 
              ""--   ____        ______      --'                      
                         """"""""'''[1:]


ascii = '''
                                                                  < >
\o_ __o       o__ __o/  \o__ __o      o__ __o/      __o__    o     |        o__  __o
|    v\     /v     |    |     |>    /v     |      />  \    <|>    o__/_   /v      |>
/ \    <\   />     / \  / \   < >   />     / \     \o       / \    |      />      //
\o/     /   \      \o/  \o/         \      \o/      v\      \o/    |      \o    o/
|     o     o      |    |           o      |        <\      |     o       v\  /v __o
/ \ __/>     <\__  / \  / \          <\__  / \  _\o__</     / \    <\__     <\/> __/>
\o/
|
/'''[1:]


def init():
  System.Title("Parasite")
  System.Size(180, 50)
  Anime.Fade(text=Center.Center(banner), color=Colors.green_to_yellow, mode=Colorate.Vertical, enter=True)


def main():
  System.Clear()
  print("\n"*2)
  print(Colorate.Diagonal(Colors.green_to_yellow, Center.XCenter(ascii)))
  print("\n"*5)

  file = Write.Input("Drag a file -> ", Colors.green_to_yellow, interval=0.005)
  print()

  if not isfile(file):
      print(Colorate.Error("Error! This file does not exist!"))
      return

  mode = Write.Input("Compress or decompress this file [c/d] -> ", Colors.green_to_yellow, interval=0.005)
  print()


  if mode not in ('c', 'd'):
    print(Colorate.Error("Please enter 'c' or 'd'!"))
    return

  try:
    if mode == 'c':
      olen, nlen = Parasite.run(file=file, mode=Parasite.compress)
    elif mode == 'd':
      olen, nlen = Parasite.run(file=file, mode=Parasite.decompress)
  except Exception as e:
      print(Colorate.Error(f"An error occured: [{e}]! Maybe your file isn't compatible with Parasite."))
      return


  print()

  Write.Input(f"Done! Old file size: [{olen} bytes] - New file size: [{nlen} bytes]", Colors.green_to_yellow, interval=0.005)
  return exit()


if __name__ == '__main__':
  init()
  while True:
    main()