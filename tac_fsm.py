import Controlo_carro as ctrl_carro
import Projeto_visao_2 as  visao

STATES_LEN = 8

class tac_states():
    idle = 0
    init = 1
    shearch = 2
    navigate = 3
    dock = 4
    platform = 5
    release = 6
    dummy = 7

state = tac_states.init
n_state = tac_states.init

def switch_state ():
    state = n_state

#---------------------------------------------------------------------------------------------
def encode_state():
    if state == tac_states.idle:
        init_state()

    elif state == tac_states.init:
        n_state = tac_states.shearch

    elif state == tac_states.shearch:
        n_state = tac_states.shearch

    elif state == tac_states.navigate:
        n_state == tac_states.navigate

    elif state == tac_states.dock:
        n_state = tac_states.dock

    elif state == tac_states.platform:
        n_state == tac_states.platform

    elif state == tac_states.release:
        n_state == tac_states.release

    else :
        state = tac_states.init
#---------------------------------------------------------------------------------------------
def idle_state():
    n_state = tac_states.idle
    #stop the car
    ctrl_carro.ser.write(bytearray('STOP\n', "ascci"))
    #wait for user
    str=ctrl_carro.ser.read(7)
    #set next state
    n_state = tac_states.shearch

#---------------------------------------------------------------------------------------------
def init_state():
    n_state = tac_states.shearch
    #init the device



    #init the sys on STM32
    ctrl_carro.ser.write(bytearray('START\n', "ascci"))

#---------------------------------------------------------------------------------------------
def shearch_state():
    n_state = tac_states.shearch

    #activate recon

    #start rotating    
    str = 'MNT 5.00 -5.00\n'
    ctrl_carro.ser.write(bytearray(str, "ascci"))
    #detect the target with QR code


    #stop rotating
    str = 'MNT 0.00 0.00\n'
    ctrl_carro.ser.write(bytearray(str, "ascci"))
    #set the new state
    n_state = tac_states.navigate


#---------------------------------------------------------------------------------------------
def navigate_state():
    n_state = tac_states.navigate
    #start to control the car by vision


    #stop the car
    ctrl_carro.ser.write(bytearray('MNT 0.00 0.00\n', "ascci"))
    #set new state


#---------------------------------------------------------------------------------------------
def docking_state():
    n_state = tac_states.docking
    #stop control by vision ## ?
    
    #activate the IR sensors

    #start control by IR

    #stop the car
    ctrl_carro.ser.write(bytearray('MNT 0.00 0.00\n', "ascci"))
    #stop the IR sensors


    #set the next state


#---------------------------------------------------------------------------------------------
def platform_state():
    n_state = tac_states.platform
    #send command to pull up the paltform

    #set next state
    n_state = tac_states.platform

#---------------------------------------------------------------------------------------------
def release_state():
    n_state = tac_states.release
    #send command to release the platform
    
    #wait for the platform to be released
    
    #set next state
    n_state = tac_states.idle

