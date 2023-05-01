
###############################################################################################
##                                  Verificador Mágico                                       ##
###############################################################################################

Lines = []
for line in open(r"C:\Users\Saede\Documents\Proyecto compresor\LaBiblia.txt", 'r').readlines():
  Lines.append(line)
Lines2 = []
for line in open(r"C:\Users\Saede\Documents\Proyecto compresor\descomprimido-elmejorprofesor.txt", 'r').readlines():
  Lines2.append(line)
if(Lines == Lines2):
  print("Ok")
else:
  print("Nok")