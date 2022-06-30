import profile
import sqlite3
from tkinter import N

#from matplotlib.style import use
#from eth_utils.curried import keccak
#from eth_keys import keys
from web3 import Account, HTTPProvider
from bdb import effective
import streamlit as st
import pandas as pd
from turtle import pu
from attr import validate
from PIL import Image
import pathlib as Path
#from questionary import form
from eth_account import account, Account
from eth_typing.evm import Address
#from bip44 import Wallet
import secrets
from dotenv import load_dotenv
from gzip import READ
import os 
import json
import streamlit as st
from eth_account import account
from eth_typing.evm import Address
from matplotlib import pyplot as plt
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from web3 import Web3
from mnemonic import Mnemonic
import hashlib
import time
import base64
from numpy import asarray
from PIL import Image
#from numpy import asarrayjuimport matplotl#ib.image as img
from PIL import Image as im
import re
import streamlit as st







def main():
    st.set_page_config(layout="centered", page_icon=":link:", initial_sidebar_state="expanded", page_title="Metaverse/Swapmeet")
	
    st.markdown(
     "## Your Ξthereum Block BackΞd Global Charity")

menu = ["Review Donations", "New Donation"]

choice = st.sidebar.selectbox("Menu", menu)
    
if choice == "New Donation":
    st.subheader("New Donation")
    nameofD = st.sidebar.text_input("Donatiors Name")
    messageforD = st.text_area('Donatiors Message')

    durationOf  = st.sidebar.selectbox("Duration of allowance",['3 Months','6 Months', '9 Months', '12 Months'])
    
    ammountAllowed = st.sidebar.selectbox("Percentage allowed", ['1%','5%','10%','25%','50%','75%','100%'])
    
    new_donationTyte = st.sidebar.selectbox("Select Cryto", ['BTC', 'ETH', 'CRO', 'ATOM', 'ALGO', 'MATIC'])
    locationOfimpact = st.selectbox("Select Location of Impact", ['City', 'County', 'State', 'Country', 'Global'])

    if st.checkbox("Coomit Donation"):
        c_web3 = Web3(Web3.HTTPProvider(os.getenv("HTTP://127.0.0.1:8545")))
        c_web3.eth.defaultAddress = '0x56F0274dA73FC6e58D5fF92cb08C85d639f47751' # not sure which this would be / most likely a sc
        
