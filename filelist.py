# -*- coding: utf-8 -*-
import os
import time
import sys

u"""To jest funkcja która listuje podany katalog
level oznacza poziom zagłębienia rekurencyjnego wywołania, reprezentowany iloscią spacji, użytych do wcięcia"""
def list(katalog, level):
   lista = os.listdir(katalog)
   pos =1
   lspace=0
   spaces=""
   while lspace < level:
      spaces=spaces+" "
      lspace = lspace+1
   for el in lista:
      if os.path.isdir(katalog+'/'+el):
         print "%s--+>%s/" % (spaces,el)
         list(katalog+'/'+el, level+2)
      else:
         try:
            (st_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime) = os.stat(katalog+'/'+el)
         except OSError:
            st_size = 0
            st_ctime = 0
            st_mtime = 0
         if len(sys.argv)>1 and sys.argv[1]=="-all":
            print "%s+%s  (size: %s B,  crtime: %s,  lmtime: %s)" % (spaces, el, st_size, time.ctime(st_ctime), time.ctime(st_mtime))
         else:
            print "%s+%s" % (spaces, el)
         pos=pos+1

u""" Skrypt nie działa w 100%, gdyż formatowanie nie jest zbyt przyjazne, coś się gdzieś zepsuło
aby wylistować katalog domowy, muszę go skopiować do tego katalogu - skrypt listuje katalog, w którym się znajduje"""

if __name__ == "__main__":
   if len(sys.argv)>1 and sys.argv[1]=="-help":
      print u"""      FileList v2.0 by Tomasz Bajorek
      ---------------------------------
      1. Wywołanie:
         python filelist.py [parametry]
      ---------------------------------
      2. Parametry:
        -help  wyświetla pomoc
        -all   wyświetla pełen zestaw informacji o listowanych elementach
      ---------------------------------
      3. Oznaczenia na liście plików:
        * crtime data i godzina utworzenia
        * lmtime data i godzina ostatniej modyfikacji
        * size   rozmiar"""
   else:
      print u"""Witaj. Wylistuję teraz podany katalog
      ---------------------------------------------
      %s
      ---------------------------------------------""" % os.getcwd()
      list(os.getcwd(), 0)
