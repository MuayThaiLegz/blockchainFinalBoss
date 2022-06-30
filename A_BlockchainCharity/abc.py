import profile
import sqlite3
from tkinter import N
from dataBasefunctions import *
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
from blockchainConnect import  emailcheck, Newpasswordcheck, waitForReceipt, REGISTRATION_abi, REGISTRATION_bytecode
import hashlib
from blockchainConnect import connectToWeb3_viaGeth, listing_transfer, Swap_Listing
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
HTTP_web3 = Web3(Web3.HTTPProvider(os.getenv("HTTP://127.0.0.1:8545")))

choice = st.sidebar.selectbox("Menu", menu)
    
if choice == "New Donation":
    st.subheader("New Donation")
    nameofD = st.sidebar.text_input("Donatiors Name")
    messageforD = st.text_area('Donatiors Message')

    durationOf  = st.sidebar.selectbox("Duration of allowance",['3 Months','6 Months', '9 Months', '12 Months'])
    
    ammountAllowed = st.sidebar.selectbox("Percentage allowed", ['1%','5%','10%','25%','50%','75%','100%'])
    
    donationTyte = st.selectbox("Select Cryto", ['BTC', 'ETH', 'CRO', 'ATOM', 'ALGO', 'MATIC'])
    locationOfimpact = st.selectbox("Select Location of Impact", ['City', 'County', 'State', 'Country', 'Global'])

    signUpButtom = st.checkbox("Place Donation")
    
    if signUpButtom:
        st.write(f"You have successfully, Allowed {ammountAllowed}")
        
        payload = {
            'from': '0x4175fB9d51366B59D51B81767000E0D9D40A6B48',
            'to': "0x0c5D5E629B7E287feC56a48AE28De392db74e058",
            'value': 40000000000000000}
        
 # Submit the transaction to the Ethereum node, the ** node will return the hash value of the transaction**
        tx_hash = HTTP_web3.eth.send_transaction(payload)
#sendTransaction(payload)
        print(f'tx hash => {0}{tx_hash}')


	    
        
