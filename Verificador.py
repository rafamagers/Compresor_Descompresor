import sys
###############################################################################################
##                                  Verificador Mágico                                       ##
###############################################################################################

Lines = []
for line in open(sys.argv[1], 'r').readlines():
  Lines.append(line)
Lines2 = []
for line in open("descomprimido-elmejorprofesor.txt", 'r').readlines():
  Lines2.append(line)
if(Lines == Lines2):
  print("Ok")
else:
  print("Nok")
