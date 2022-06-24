# by billythegoat356

# https://github.com/billythegoat356/Parasite



from os.path import isfile
from pystyle import Anime, Colorate, Colors, Center, System, Write
from zlib import compress


def Parasite(content):
    ncontent = compress(content)
    return f"eval(compile(__import__('zlib').decompress({ncontent})))"




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

  with open(file, mode='rb') as f:
    content = f.read()


  if mode not in ('c', 'd'):
    print(Colorate.Error("Please enter 'c' or 'd'!"))
    return

  content = Parasite(content)

  with open(file='new-' + (file.split('\\')[-1] if '\\' in file else file.split('/')[-1]), mode='w', encoding='utf-8') as f:
      f.write(content)

  print()

  Write.Input(f"Done! Old file size: [{olen} bytes] - New file size: [{nlen} bytes]", Colors.green_to_yellow, interval=0.005)
  return exit()


if __name__ == '__main__':
  init()
  while True:
    main()
