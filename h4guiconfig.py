#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict

def configure(self):

    self.debug=False # turn on for network messaging debugging
    self.activatesounds=True # turn on to play sounds
    self.sumptuous_browser=True # turn on to use browser tabs for DQM display

    self.pubsocket_bind_address='tcp://*:5566' # address of GUI PUB socket

    self.nodes=[ # addresses of connected nodes
        ('RC','tcp://pcethtb2.cern.ch:6002'),
#        ('RC','tcp://pcminn03.cern.ch:6002'),
        ('RO1','tcp://pcethtb1.cern.ch:6002'),
        # ('RO1','tcp://pcethtb1.cern.ch:6002'),
        # ('RO2','tcp://pcethtb1.cern.ch:6032'),
        # ('RO3','tcp://pcethtb1.cern.ch:6042'),
        # ('RO4','tcp://pcethtb1.cern.ch:6052'),
        # ('RO5','tcp://pcethtb1.cern.ch:6072'),
        # ('RO6','tcp://pcethtb1.cern.ch:6082'),
        # ('RO2','tcp://cms-h4-03:6002'),
        ('EVTB','tcp://pcethtb2.cern.ch:6502'),
#        ('EVTB','tcp://pcminn03.cern.ch:6502'),
#        ('DRCV1','tcp://localhost:6502'),
        ('DRCV1','tcp://cms-h4-04.cern.ch:6502'),
        ('DRCV2','tcp://cms-h4-05.cern.ch:6502'),
#        ('table','tcp://cms-h4-01:6999')
#        ('table','tcp://128.141.77.89:6999')
        ('table','tcp://128.141.77.125:6999') 
        ]

    self.keepalive={} # nodes to monitor (comment to remove, never put False)
    self.keepalive['RC']=True
    self.keepalive['RO1']=True
    # self.keepalive['RO2']=True
    # self.keepalive['RO3']=True
    # self.keepalive['RO4']=True
    # self.keepalive['RO5']=True
    # self.keepalive['RO6']=True
#    self.keepalive['RO2']=False
    self.keepalive['EVTB']=True
    self.keepalive['DRCV1']=True
    self.keepalive['DRCV2']=True
#    self.keepalive['table']=True

    self.temperatureplot=None # 'http://blabla/tempplot.png' to be displayed for temperature history

# DQM plots, to be filled if not using tabbed browsing support
#        self.dqmplots=[] # [('tabname','http://plotname','http://largeplotname.png'),...]
#        self.dqmplots=[
#            ('tab1','/home/cmsdaq/DAQ/H4GUI/plots/canv11.png','/home/cmsdaq/DAQ/H4GUI/plots/canv21.png')
#            ]


    self.scripts={ # scripts linked to GUI buttons
        'sync_clocks': '../H4DAQ/scripts/syncclocks.sh',
        'free_space': None,
#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --dr=pcethtb1 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_07_ECAL', #std config for h4
        #'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --dr=pcethtb1 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_07_ECAL_LOW_FREQ', #std config for h4 with digitizer frequency of 2.5 GHz
#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --dr=pcethtb1 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_09_ECAL_SPIKES_LOW_FREQ', #config for ecal spikes with digitizer frequency of 2.5 GHz
#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --dr=pcethtb1 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_09_ECAL_SPIKES', #config for ecal spikes
#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --dr=pcethtb1 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_07_ECAL_CSI', #std config for h4

        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --dr=pcethtb1 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2017_06_MTD', #std config for h4
        # 'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --dr=pcethtb1:3:4:5:7:8: --eb=pcethtb2 --drcv=cms-h4-04,cms-h4-05 --tag=H4_2017_06_TIA_TEST --gitbranch=vfe_dev', #std config for VFEs
        #'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --gitbranch=vfe_dev --rc=pcethtb2 --eb=pcethtb2 --dr=pcethtb1 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_07_ECAL_CSI', #std config for h4
        #'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --tag=H4_2016_07_ECAL_CSI', #std config for h4

#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --dr=pcethtb1',
#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb1 --eb=pcethtb1 ',
#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcminn03 --eb=pcminn03 --drcv=localhost --tag=H2_2016_06',
#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --dr=pcethtb1 --eb=pcethtb2 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_06',
#       'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_06',
#       'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2  --drcv=cms-h4-04,cms-h4-05 --drcvrecompile --tag=H4_2016_06_LYSO',
#       'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb2 --drcv=cms-h4-04,cms-h4-05 --drcvrecompile',
#        'start_daemons': '../H4DAQ/scripts/startall.sh -v3 --rc=pcethtb2 --eb=pcethtb1 --dr=pcethtb1 --drcv=cms-h4-05 --drcvrecompile',
        'kill_daemons': '../H4DAQ/scripts/killall.sh --tag=H4_2016'
        }
#

    self.tableposdictionary = OrderedDict()
# PWO matrix 216
#     self.tableposdictionary['CRYSTAL_A0']=(287.5,201.0)
#     self.tableposdictionary['CRYSTAL_A1']=(287.5,228.0)
#     self.tableposdictionary['CRYSTAL_A2']=(287.5,250.0)
#     self.tableposdictionary['CRYSTAL_A3']=(287.5,272.0)
#     self.tableposdictionary['CRYSTAL_A4']=(287.5,294.0)
#     self.tableposdictionary['CRYSTAL_A5']=(287.5,316.0)
#     self.tableposdictionary['CRYSTAL_B0']=(262.5,201.0)
#     self.tableposdictionary['CRYSTAL_B1']=(262.5,228.0)
#     self.tableposdictionary['CRYSTAL_B2']=(262.5,250.0)
#     self.tableposdictionary['CRYSTAL_B3']=(262.5,272.0)
#     self.tableposdictionary['CRYSTAL_B3_right']=(252.5,272.0)
#     self.tableposdictionary['CRYSTAL_B3_down']=(262.5,282.0)
#     self.tableposdictionary['CRYSTAL_B3_up']=(262.5,262.0)
#     self.tableposdictionary['CRYSTAL_B3_left']=(272.5,272.0)
#     self.tableposdictionary['CRYSTAL_B4']=(262.5,294.0)
#     self.tableposdictionary['CRYSTAL_B5']=(262.5,316.0)
#     self.tableposdictionary['CRYSTAL_C0']=(237.5,201.0)
#     #self.tableposdictionary['CRYSTAL_C0_N']=(237.5,196.0)
#     #self.tableposdictionary['CRYSTAL_C0_W']=(242.5,201.0)
#     #self.tableposdictionary['CRYSTAL_C0_E']=(232.5,201.0)
#     #self.tableposdictionary['CRYSTAL_C0_S']=(237.5,206.0)
#     self.tableposdictionary['CRYSTAL_C1']=(237.5,228.0)
#     self.tableposdictionary['CRYSTAL_C2']=(237.5,250.0)
#     self.tableposdictionary['CRYSTAL_C3']=(237.5,272.0)
#     self.tableposdictionary['CRYSTAL_C3_right']=(227.5,272.0)
#     self.tableposdictionary['CRYSTAL_C3_down']=(237.5,282.0)
#     self.tableposdictionary['CRYSTAL_C3_up']=(237.5,262.0)
#     self.tableposdictionary['CRYSTAL_C3_left']=(247.5,272.0)
#     #self.tableposdictionary['CRYSTAL_C3_E']=(227.5,272.0)
#     #self.tableposdictionary['CRYSTAL_C3_S']=(237.5,282.0)
#     #self.tableposdictionary['CRYSTAL_C3_N']=(237.5,262.0)
#     #self.tableposdictionary['CRYSTAL_C3_W']=(227.5,272.0)
#     self.tableposdictionary['CRYSTAL_C4']=(237.5,294.0)
#     self.tableposdictionary['CRYSTAL_C5']=(237.5,316.0)
#     self.tableposdictionary['CRYSTAL_D0']=(212.5,201.0)
#     self.tableposdictionary['CRYSTAL_D1']=(212.5,228.0)
#     self.tableposdictionary['CRYSTAL_D2']=(212.5,250.0)
#     self.tableposdictionary['CRYSTAL_D3']=(212.5,272.0)
#     self.tableposdictionary['CRYSTAL_D4']=(212.5,294.0)
#     self.tableposdictionary['CRYSTAL_D5']=(212.5,316.0)
#     self.tableposdictionary['CRYSTAL_E0']=(187.5,201.0)
#     self.tableposdictionary['CRYSTAL_E1']=(187.5,228.0)
#     self.tableposdictionary['CRYSTAL_E2']=(187.5,250.0)
#     self.tableposdictionary['CRYSTAL_E3']=(187.5,272.0)
#     self.tableposdictionary['CRYSTAL_E4']=(187.5,294.0)
#     self.tableposdictionary['CRYSTAL_E5']=(187.5,316.0)
# #
#     # 2017 ECAL matrix position (TIA VFE test)
#     self.tableposdictionary = OrderedDict()
#     self.tableposdictionary['ZERO-TABLE']=(0.0,0.0)
# #    self.tableposdictionary['ECAL_CENTER']=(240.0,272.0)
#     # 2017 SPACAL Positions                                                                                                  
#     self.tableposdictionary['SPACAL-CENTER-YAG']=(175.0,149.5)
#     self.tableposdictionary['SPACAL-CH0-20ppm']=(157.5,132.0)
#     self.tableposdictionary['SPACAL-CH1-Y11']=(192.5,132.0)
#     self.tableposdictionary['SPACAL-CH2-500ppm']=(157.5,167.0)
#     self.tableposdictionary['SPACAL-CH3-125ppm']=(192.5,167.0)
#    self.tableposdictionary['SPACAL-CH6-Pr']=(337.5,52.0)
#    self.tableposdictionary['SPACAL-TOP-P0']=(290.,52.0)
#    self.tableposdictionary['SPACAL-TOP-P1']=(260.,52.0)
#    self.tableposdictionary['SPACAL-TOP-P2']=(230.,52.0)
#    self.tableposdictionary['SPACAL-TOP-P3']=(200.,52.0)
#    self.tableposdictionary['SPACAL-TOP-P4']=(170.,52.0)
#    self.tableposdictionary['SPACAL-TOP-P5']=(140.,52.0)
#    self.tableposdictionary['SPACAL-TOP-P6']=(110.,52.0)
#    self.tableposdictionary['SPACAL-MID-P0']=(290.,132.0)
#    self.tableposdictionary['SPACAL-MID-P1']=(260.,132.0)
#    self.tableposdictionary['SPACAL-MID-P2']=(230.,132.0)
#    self.tableposdictionary['SPACAL-MID-P3']=(200.,132.0)
#    self.tableposdictionary['SPACAL-MID-P4']=(170.,132.0)
#    self.tableposdictionary['SPACAL-MID-P5']=(140.,132.0)
#    self.tableposdictionary['SPACAL-MID-P6']=(110.,132.0)
#    self.tableposdictionary['SPACAL-BOT-P0']=(290.,167.0)
#    self.tableposdictionary['SPACAL-BOT-P1']=(260.,167.0)
#    self.tableposdictionary['SPACAL-BOT-P2']=(230.,167.0)
#    self.tableposdictionary['SPACAL-BOT-P3']=(200.,167.0)
#    self.tableposdictionary['SPACAL-BOT-P4']=(170.,167.0)
#    self.tableposdictionary['SPACAL-BOT-P5']=(140.,167.0)
#    self.tableposdictionary['SPACAL-BOT-P6']=(110.,167.0)
#

    # 2016 ECAL matrix positions
#     self.tableposdictionary['ECAL_CENTER']=(240.0,272.0)
# # PWO matrix 216
#     self.tableposdictionary['CSI_CENTER']=(222.0,255.0)
#     self.tableposdictionary['CRYSTAL_E3']=(190.0,272.0)
#     self.tableposdictionary['CRYSTAL_D3']=(215.0,272.0)
#     self.tableposdictionary['CRYSTAL_C3']=(240.0,272.0)
#     self.tableposdictionary['CRYSTAL_C3_E']=(222.5,272.0)
#     self.tableposdictionary['CRYSTAL_C3_S']=(240.0,283.0)
#     self.tableposdictionary['CRYSTAL_C3_N']=(240.0,261.0)
#     self.tableposdictionary['CRYSTAL_B3']=(265.0,272.0)
#     self.tableposdictionary['CRYSTAL_A3']=(290.0,272.0)
#     self.tableposdictionary['CRYSTAL_A2']=(290.0,250.0)
#     self.tableposdictionary['CRYSTAL_B2']=(265.0,250.0)
#     self.tableposdictionary['CRYSTAL_C2']=(240.0,250.0)
#     self.tableposdictionary['CRYSTAL_D2']=(215.0,250.0)
#     self.tableposdictionary['CRYSTAL_E2']=(190.0,250.0)
#     self.tableposdictionary['CRYSTAL_A1']=(290.0,228.0)
#     self.tableposdictionary['CRYSTAL_B1']=(265.0,228.0)
#     self.tableposdictionary['CRYSTAL_C1']=(240.0,228.0)
#     self.tableposdictionary['CRYSTAL_D1']=(215.0,228.0)
#     self.tableposdictionary['CRYSTAL_E1']=(190.0,228.0)
#     self.tableposdictionary['CRYSTAL_A0']=(287.0,201.0)
#     self.tableposdictionary['CRYSTAL_B0']=(262.0,201.0)
#     self.tableposdictionary['CRYSTAL_C0']=(237.0,201.0)
#     self.tableposdictionary['CRYSTAL_C0_N']=(237.0,196.0)
#     self.tableposdictionary['CRYSTAL_C0_W']=(242.0,201.0)
#     self.tableposdictionary['CRYSTAL_C0_E']=(232.0,201.0)
#     self.tableposdictionary['CRYSTAL_C0_S']=(237.0,206.0)
#     self.tableposdictionary['CRYSTAL_D0']=(212.0,201.0)
#     self.tableposdictionary['CRYSTAL_E0']=(187.0,201.0)
#     self.tableposdictionary['CRYSTAL_A4']=(290.0,294.0)
#     self.tableposdictionary['CRYSTAL_B4']=(265.0,294.0)
#     self.tableposdictionary['CRYSTAL_C4']=(240.0,294.0)
#     self.tableposdictionary['CRYSTAL_D4']=(215.0,294.0)
#     self.tableposdictionary['CRYSTAL_E4']=(190.0,294.0)
#     self.tableposdictionary['CRYSTAL_A5']=(290.0,316.0)
#     self.tableposdictionary['CRYSTAL_B5']=(265.0,316.0)
#     self.tableposdictionary['CRYSTAL_C5']=(240.0,316.0)
#     self.tableposdictionary['CRYSTAL_D5']=(215.0,316.0)
#     self.tableposdictionary['CRYSTAL_E5']=(190.0,316.0)

    # CeF3 matrix 
    # self.tableposdictionary['CEF3_CENTER']=(224.0,294.5)
   # self.tableposdictionary['CRYSTAL_1']=(190.0,311.5)
   # self.tableposdictionary['CRYSTAL_2']=(207.0,311.5)
   # self.tableposdictionary['CRYSTAL_3']=(224.0,311.5)
   # self.tableposdictionary['CRYSTAL_4']=(241.0,311.5)
   # self.tableposdictionary['CRYSTAL_5']=(258.0,311.5)
   # self.tableposdictionary['CRYSTAL_6']=(190.0,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS']=(207.0,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_NE']=(202.7,290.2)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_NW']=(211.2,290.2)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_SE']=(202.7,298.8)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_SW']=(211.2,298.8)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_W']=(215.0,294.5) # 8 mm left
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_3DEG']=(218.9,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_5DEG']=(226.8,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_5DEG_EAST']=(218.8,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_5DEG_WEST']=(234.8,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_5DEG_NORTH']=(226.8,286.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_5DEG_SOUTH']=(226.8,302.5)
   # self.tableposdictionary['CRYSTAL_11_5DEG']=(243.8,294.5)
   # self.tableposdictionary['CRYSTAL_11_5DEG_EAST']=(235.8,294.5)
   # self.tableposdictionary['CRYSTAL_11_5DEG_WEST']=(251.8,294.5)
   # self.tableposdictionary['CRYSTAL_11_5DEG_NORTH']=(243.8,286.5)
   # self.tableposdictionary['CRYSTAL_11_5DEG_SOUTH']=(243.8,302.5)
  
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_7.5DEG']=(236.6,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_10DEG']=(246.4,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_10DEG_EAST']=(238.4,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_10DEG_WEST']=(254.4,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_10DEG_NORTH']=(246.4,286.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_10DEG_SOUTH']=(246.4,302.5)
   # self.tableposdictionary['CRYSTAL_11_10DEG']=(263.4,294.5)
   # self.tableposdictionary['CRYSTAL_11_10DEG_EAST']=(255.4,294.5)
   # self.tableposdictionary['CRYSTAL_11_10DEG_WEST']=(271.4,294.5)
   # self.tableposdictionary['CRYSTAL_11_10DEG_NORTH']=(263.4,286.5)
   # self.tableposdictionary['CRYSTAL_11_10DEG_SOUTH']=(263.4,302.5)
  
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_15DEG']=(265.7,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_15DEG_EAST']=(257.7,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_15DEG_WEST']=(273.7,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_15DEG_NORTH']=(265.7,286.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_15DEG_SOUTH']=(265.7,302.5)
  
   # self.tableposdictionary['CRYSTAL_11_15DEG']=(282.7,294.5)
   # self.tableposdictionary['CRYSTAL_11_15DEG_EAST']=(274.7,294.5)
   # self.tableposdictionary['CRYSTAL_11_15DEG_WEST']=(300.7,294.5)
   # self.tableposdictionary['CRYSTAL_11_15DEG_NORTH']=(282.7,286.5)
   # self.tableposdictionary['CRYSTAL_11_15DEG_SOUTH']=(282.7,302.5)
  
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_12.5DEG']=(256.1,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_15DEG']=(265.7,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_3DEG_EAST']=(210.9,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_3DEG_WEST']=(226.9,294.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_3DEG_NORTH']=(218.9,286.5)
   # self.tableposdictionary['CRYSTAL_FOUR_FIBERS_3DEG_SOUTH']=(218.9,302.5)
   # self.tableposdictionary['CRYSTAL_11_3DEG_EAST']=(227.9,294.5)
   # self.tableposdictionary['CRYSTAL_11']=(224.0,294.5)
   # self.tableposdictionary['CRYSTAL_11_3DEG']=(235.9,294.5)
   # self.tableposdictionary['CRYSTAL_11_5DEG']=(243.8,294.5)
   # self.tableposdictionary['CRYSTAL_11_7.5DEG']=(253.6,294.5)
   # self.tableposdictionary['CRYSTAL_11_10DEG']=(263.4,294.5)
   # self.tableposdictionary['CRYSTAL_11_12.5DEG']=(273.1,294.5)
   # self.tableposdictionary['CRYSTAL_11_15DEG']=(282.7,294.5)
   # self.tableposdictionary['CRYSTAL_12']=(241.0,294.5)
   # self.tableposdictionary['CRYSTAL_13']=(258.0,294.5)
   # self.tableposdictionary['CRYSTAL_14']=(190.0,277.5)
   # self.tableposdictionary['CRYSTAL_15']=(207.0,277.5)
   # self.tableposdictionary['CRYSTAL_16']=(224.0,277.5)
   # self.tableposdictionary['CRYSTAL_17']=(241.0,277.5)
   # self.tableposdictionary['CRYSTAL_18']=(258.0,277.5)
   # self.tableposdictionary['CRYSTAL_11_N']=(224.0,286.5) # 8 mm up
   # self.tableposdictionary['CRYSTAL_11_S']=(224.0,302.5) # 8 mm down
   # self.tableposdictionary['CRYSTAL_11_E']=(216.0,294.5) # 8 mm right
   # self.tableposdictionary['CRYSTAL_11_W']=(232.0,294.5) # 8 mm left

    
    
    otherxtals = OrderedDict() # coordinates seen from the rear face
 #   otherxtals['CAMERONE_1']= (-10.0,-10)
 #   otherxtals['CAMERONE_2']= (+10,-10)
 #   otherxtals['CAMERONE_3']= (-10,+10)
 #   otherxtals['CAMERONE_4']= (+10,+10)

#    otherxtals['BGO_CRY_1']= (-20.0,25.1)
#    otherxtals['BGO_CRY_2']= (2.0,25.0)
#    otherxtals['BGO_CRY_3']= (25.0,22.0)
#    otherxtals['BGO_CRY_4']= (-25.0,2.0)
#    otherxtals['BGO_CRY_5']= (25.0,-2.0)
#    otherxtals['BGO_CRY_6']= (-24.0,-20.0)
#    otherxtals['BGO_CRY_7']= (-2.0,-25.0)
#    otherxtals['BGO_CRY_8']= (21.0,-25.0)
#    otherxtals['BGO_CRY_9']= (-47.0,51.0)
#    otherxtals['BGO_CRY_10']= (-22.0,49.0)
#    otherxtals['BGO_CRY_11']= (2.0,48.0)
#    otherxtals['BGO_CRY_12']= (27.0,45.0)
#    otherxtals['BGO_CRY_13']= (51.0,47.0)
#    otherxtals['BGO_CRY_14']= (-46.0,28.0)
#    otherxtals['BGO_CRY_15']= (50.0,22.0)
#    otherxtals['BGO_CRY_16']= (-50.0,3.0)
#    otherxtals['BGO_CRY_17']= (50.0,0.0)
#    otherxtals['BGO_CRY_18']= (-49.0,-22.0)
#    otherxtals['BGO_CRY_19']= (46.0,-24.0)
#    otherxtals['BGO_CRY_20']= (-49.0,-46.0)
#    otherxtals['BGO_CRY_21']= (-25.0,-45.0)
#    otherxtals['BGO_CRY_22']= (0.0,-49.0)
#    otherxtals['BGO_CRY_23']= (24.0,-49.0)
#    otherxtals['BGO_CRY_24']= (49.0,-49.0)
##

    # CeF3 single channel 
    # ARASH: once you are sure about the center edit the CEF3_CENTER position only from the FIRST line below 
    self.tableposdictionary['CEF3_CENTER']=(194.0,254.0)
    self.tableposdictionary['CEF3_CENTER_ALT']=(224.0,294.5)
    otherxtals['CEF3_UP3']= (0.0,15.0)
    otherxtals['CEF3_UP2']= (0.0,10.0)
    otherxtals['CEF3_UP1']= (0.0,5.0)
    otherxtals['CEF3_DOWN1']= (0.0,-5.0)
    otherxtals['CEF3_DOWN2']= (0.0,-10.0)
    otherxtals['CEF3_DOWN3']= (0.0,-15.0)
    
    otherxtals['CEF3_LEFT3']= (-15.0,0.0)
    otherxtals['CEF3_LEFT2']= (-10.0,0.0)
    otherxtals['CEF3_LEFT1']= (-5.0,0.0)
    otherxtals['CEF3_RIGHT1']= (5.0,0.0)
    otherxtals['CEF3_RIGHT2']= (10.0,0.0)
    otherxtals['CEF3_RIGHT3']= (15.0,0.0)

    otherxtals['CEF3_DIAG_SW4']= (-12.0,-12.0)
    otherxtals['CEF3_DIAG_SW3']= (-9.0,-9.0)
    otherxtals['CEF3_DIAG_SW2']= (-6.0,-6.0)
    otherxtals['CEF3_DIAG_SW1']= (-3.0,-3.0)
    otherxtals['CEF3_DIAG_NE1']= (3.0,3.0)
    otherxtals['CEF3_DIAG_NE2']= (6.0,6.0)
    otherxtals['CEF3_DIAG_NE3']= (9.0,9.0)
    otherxtals['CEF3_DIAG_NE3_CH']= (14.0,13.0)
    otherxtals['CEF3_DIAG_NE4']= (12.0,12.0)

    otherxtals['CEF3_DIAG_NW4']= (-12.0,12.0)
    otherxtals['CEF3_DIAG_NW3']= (-9.0,9.0)
    otherxtals['CEF3_DIAG_NW2']= (-6.0,6.0)
    otherxtals['CEF3_DIAG_NW1']= (-3.0,3.0)
    otherxtals['CEF3_DIAG_SE1']= (3.0,-3.0)
    otherxtals['CEF3_DIAG_SE2']= (6.0,-6.0)
    otherxtals['CEF3_DIAG_SE3']= (9.0,-9.0)
    otherxtals['CEF3_DIAG_SE4']= (12.0,-12.0)

##
    for i,j in otherxtals.iteritems():
        self.tableposdictionary[i]=(self.tableposdictionary['CEF3_CENTER'][0]+j[0],self.tableposdictionary['CEF3_CENTER'][1]-j[1])
#        self.tableposdictionary[i]=(self.tableposdictionary['CAMERONE_CENTER'][0]+j[0],self.tableposdictionary['CAMERONE_CENTER'][1]-j[1])
