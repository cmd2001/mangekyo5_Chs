# mangekyo5_Chs

### About

A little tool to create Machine Translation for 美少女万華鏡5.

Special Thanks to: [hz86/filepack](https://github.com/hz86/filepack)

Only translate dialogue text, will not modify program UI and option tabs.

**This version does not work with official 1.01 update (with `pack8.pack`)**

### Useage

1. Unpack `/GameData/pack6.pack` with `filepack`.

2. Find the directory which contains files in `ls.txt`, copy `ls.txt, main.py, work.py, BaiduTrans.py` into the directory.

3. Fill `appid, secretKey` in `BaiduTrans.py` with your Baidu Translation API ID.

4. Run `main.py` with python3.

5. remove prmgram files, pack `pack6.pack` back and enjoy the game.

If you want to create a version which works with 1.01 update, you need to find text files in `pack8.pack` and modify `ls.txt`.

### License

GPL.