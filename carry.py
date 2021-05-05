#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:34:10 2021

@author: christianemilbach
"""

import matplotlib.pyplot as plt
import numpy as np
import json

#Size of pitch in yards (!!!!)
pitchLengthX=120
pitchWidthY=80

#ID for Barcelona vs Sevilla in the 17/18 La Liga season
match_id_required = 9673
home_team_required ="Barcelona"
away_team_required ="Sevilla"

#Load in the data
file_name =str(match_id_required)+'.json'

#Load in all match events
with open('Statsbomb/data/events/'+file_name) as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)
    
#Get the nested structure into a dataframe
#Store the dataframe in a dictionary with the match id as key
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(matchid = file_name[:-5])

#A dataframe of carries
carries = df.loc[df['type_name'] == 'Carry'].set_index('id')

#Draw the pitch
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX, pitchWidthY,'yards','gray')

messi= 'Lionel Andrés Messi Cuccittini'
    
#Draw the pitch and plot in carries by Messi
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
for i,carry in carries.iterrows():
    #if thepass['team_name']==away_team_required: #
    if carry['player_name']==messi:
        x=carry['location'][0]
        y=carry['location'][1]
        carryCircle=plt.Circle((x,pitchWidthY-y),1,color="blue")      
        carryCircle.set_alpha(.2)   
        ax.add_patch(carryCircle)
        dx=carry['carry_end_location'][0]-x
        dy=carry['carry_end_location'][1]-y
        
        carryArrow=plt.Arrow(x,pitchWidthY-y,dx,-dy,width=2,color="blue")
        ax.add_patch(carryArrow)

plt.text(1,85,messi[0:6] + messi[12:19] + ' carries vs ' + away_team_required, 
         fontsize=12, fontfamily= 'serif', fontweight=700)

plt.show()

        
        