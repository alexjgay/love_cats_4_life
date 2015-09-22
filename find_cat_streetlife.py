#!/usr/bin/python

import csv, sys, array
from random import randint


print 'Argument List:', str(sys.argv)

print 'Numbers of cat : ', str(sys.argv[1])
print 'Numbers of owner : ', str(sys.argv[1])


#################################
####### Vars ####################
#################################


tfl_sta = csv.reader(open("tfl_stations.csv","rb"))

nbr_cats = int(sys.argv[1])
nbr_owners = int(sys.argv[1])

#### Init cat and owner arrays

cats = [[] for i in xrange(nbr_cats)]

owners = [[] for j in xrange(nbr_owners)]

#### Init cat random position
for k in range(nbr_cats):
 
 cats[k] = [randint(1,303)]

print 'cats are in stations : ', cats

#### Init owner random position
for l in range(nbr_owners):
 owners[l] = [randint(1,303)]

print 'owners are in station : ', owners

list_stations_found = []

############Function move cat
###### Cats move to the corresponding connection
###### all corresponding connection at time t are put in a list 

def move_cat ():
 pcat = 0
##Search connections
 for cat in cats:
#############################
#  print(cat)

#########search if owner is in same station than cat
  
  if cats[pcat] == owners[pcat]:
#   print "##############YYYYYYYYYESSS  cat has found his owner"
#   print "cats[pcat]",cats[pcat]
#   print "owners[pcat]",owners[pcat]
   list_stations_found.append(int(str(cats[pcat]).strip('[]')))


  list_conn = [ [] for j in xrange(20)]
  p = 0
  tfl_co = csv.reader(open("tfl_connections.csv","rb"))
 #print cat[0]
 
  for row in tfl_co:
   if str(cat).strip('[]').replace("'", "") == row[0]:
    list_conn[p] = str(row[1]).replace("'", "")
### New station of the cat 
    p +=1
    p2 = p-1
    rand_npos = randint(0,p2)
    #print "randint : ", rand_npos 
    cats[pcat]=[int(list_conn[rand_npos])]

  pcat += 1
  #print "cat number : ", pcat

  #print list_conn
  #print "tab of cats"

 #print cats
   
##
############Function move owner 
######  Owners move to the corresponding connection
###### all corresponding connection at time t are put in a list 


def move_owner ():
 powner = 0
##Search connections
 for owner in owners:
#############################
#########search if owner is in same station than cat
  
  if owners[powner] == cats[powner]:
#   print "owners[powner]",owners[powner]
   list_stations_found.append(int(str(cats[powner]).strip('[]')))


  list_conn = [ [] for j in xrange(20)]
  p = 0
  tfl_co = csv.reader(open("tfl_connections.csv","rb"))
 #print cat[0]

  for row in tfl_co:
   if str(owner).strip('[]').replace("'", "") == row[0]:
    list_conn[p] = str(row[1]).replace("'", "")
### New station of the cat
    p +=1
    p2 = p-1
    rand_npos = randint(0,p2)
    #print "randint : ", rand_npos
    owners[powner]=[int(list_conn[rand_npos])]

  powner += 1


##

z = 0

# While loop condition.
while z < 1000:
    move_cat()
    move_owner()
    z += 1
 
#for rows in cr:    
#    print rows
 

print "Number of cats found :", len(list(set(list_stations_found)))
print "List of stations where owners have found their cats"
print list(set(list_stations_found)) 
