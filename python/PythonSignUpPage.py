
import os 
import json
import streamlit as st
from eth_account import account
from eth_typing.evm import Address
from tensorflow.python.framework.dtypes import as_dtype
from tensorflow.python.ops.gen_math_ops import bucketize
from tensorflow.python.ops.gen_string_ops import string_format
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from web3 import Web3
import streamlit as st
from bip44 import Wallet
from web3 import Account
from mnemonic import Mnemonic

#date = time.time()
#from solc import compile_standard

import requests

load_dotenv()
mnemonic = os.getenv("MNEMONIC")

ganache_url = "HTTP://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(ganache_url))
# The user will create their wallet address, and account address.
with wallet_info:

    
    if st.button("Create Digital Address") == True:

        if mnemonic is None:
            mnemo = mnemonic("english")  
            mnemonic = mnemo.generate(strength=256)
        mnemonic_seed_phrase = st.write(
            f"""This is your Mnemonic seed phrase.
            Do not share with anyone.
            When used in sequence it will  allow access to the wallet we've just created for you.
            ---> {mnemonic}""")
        wallet = Wallet(mnemonic)
        wallet_obj = st.write(
            f""" With the help of the bip44 package and your Mnemonic seed phrase
            we created this universal wallet instance.
            {wallet}""")
        private, public = wallet.derive_account('eth')
        st.write(
            f"""{private} <-----
            This is an encoded represantiation of your private key and the only way you should store in your device""")
        account = Account.privateKeyToAccount(private)
        st.write(
            f"""{account.address} <----- This is the address associated with your new Ethereum account.
            We are using this address to store all your tokenized collectables and swaped for collectables on the Ethereum blockchain.""")





    
    if st.button('Finalize Registration'):
        if mnemonic is None:
            mnemo = Mnemonic("english")  
            mnemonic = mnemo.generate(strength=256)

        mnemonic_seed_phrase = st.write(
            f"""This is your Mnemonic seed phrase.
            Do not share with anyone.
            When used in sequence it will  allow access to the wallet we've just created for you.
            ---> {mnemonic}""")

        wallet = Wallet(mnemonic)

        wallet_obj = st.write(
            f""" With the help of the bip44 package and your Mnemonic seed phrase
            we created this universal wallet instance.
            {wallet}""")

        private, public = wallet.derive_account('eth')

        st.write(
            f"""{private} <-----
            This is an encoded represantiation of your private key and the only way you should store in your device""")

        account = Account.privateKeyToAccount(private)
        
        st.write(
            f"""{account.address} <----- This is the address associated with your new Ethereum account.
            We are using this address to store all your tokenized collectables and swaped for collectables on the Ethereum blockchain.""")



    # trasaction of deal not sing up 
      # contract address for now   
    def sol_function_cal():
        accounts = w3.eth.accounts
        account = accounts[2]
        proprietor = st.text_input('Enter your digital address')
        collectable_details = st.text_input("Deed Details", value="Deed To Collectable")
        token_id = st.number_input("Enter a Certificate Token ID to display", value=0, step=1) 
        
        if st.button('New Deed'):
            itm_hash = contract.functions.deedForItem(proprietor, collectable_details).transact({'from' : account, 'to' : proprietor,  'gas': 2812493})
            print(itm_hash)
            print("hello")
            
            token_owner = contract.functions.ownerOf(token_id).transact({'from' : account, 'to' : proprietor})
            st.write(f"The Swap Deed Owner {token_owner}")
        
            token_uri = contract.functions.tokenURI(token_id).transact({'from' :account, "to" : proprietor})
            st.write(f"The Deed's tokenURI metadata is {token_uri}")
            print("champ shit")

            balanceOf = contract.functions.balanceOf(proprietor).transact({'from' :account, "to" : proprietor})

            st.write(f"Balance {balanceOf}")
            print(balanceOf)
            print("champ shit")


sol_function_cal()


    #receiver = st.text_input('Input item information')

    message_seller = st.text_input('Write a message to the lister of the item, Dont share sensetive info')

contact_seller()






    #def sol_function_cal():
        #proprietor =  account_address
        #contract_sender = st.text_input('Enter the contract sender')
        #tokenURI =  st.text_input('enter tokenURI')
        ##c_add  = st.write(eval("enter add"))
        # if proprietor == True:
        #receipt = False
        #if st.button('New Deed'):
        #    print("I'm HERE")
         #   itm_hash = contract.functions.deedForItem(
         #       proprietor,
          #      tokenURI
           # ).transact({'to' : proprietor, 'from' : contract_sender, 'gas': 1000000})
            #receipt = Web3.eth.waitForTransactionReceipt(itm_hash)
        #print(f'{contract_sender, receipt}')







if next.button("Finalize Registration") == True:
    import pathlib as Path
    # pulls the general info of the users and saves it to a dataframe(csv)
    general_info_list = []
    general_info_list.append({"First Name": first_name, "Last Name": last_name, "Email": email_address, "Year": year, "Make": make, "Model": model, "Miles": miles, "Certification": certification})
    general_path = Path("../Project_3_Swapout/csv_data/general_info.csv")
    general_info_df=pd.read_csv(general_path)
    general_info_df.append(general_info_list)


    # pulls the private info of the users and saves it to a dataframe(csv)
    private_info_list = []
    private_info_list.append({"Digital Address": account_address, "Password": confirm_password, "Physical Address": mailing_address, })
    private_path = Path("../Project_3_Swapout/csv_data/private_info.csv")
    private_info_df=pd.read_csv(private_path)
    private_info_df.append(private_info_list)
    





    import requests

load_dotenv()
mnemonic = os.getenv("MNEMONIC")

ganache_url = "HTTP://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(ganache_url))

bytecode = ('')


genaralReg  = w3.eth.contract(abi = abi, bytecode = bytecode)


if st.button('Finalize Registration'):
        if mnemonic is None:
            mnemo = Mnemonic("english")  
            mnemonic = mnemo.generate(strength=256)

        mnemonic_seed_phrase = st.write(
            f"""This is your Mnemonic seed phrase.
            Do not share with anyone.
            When used in sequence it will  allow access to the wallet we've just created for you.
            ---> {mnemonic}""")

        wallet = Wallet(mnemonic)

        wallet_obj = st.write(
            f""" With the help of the bip44 package and your Mnemonic seed phrase
            we created this universal wallet instance.
            {wallet}""")

        private, public = wallet.derive_account('eth')

        st.write(
            f"""{private} <-----
            This is an encoded represantiation of your private key and the only way you should store in your device""")

        account = Account.privateKeyToAccount(private)
        
        st.write(
            f"""{account.address} <----- This is the address associated with your new Ethereum account.
            We are using this address to store all your tokenized collectables and swaped for collectables on the Ethereum blockchain.""")

def Swap_DeeD():
    web3 = Web3(Web3.HTTPProvider(ganache_url))
    web3.eth.defaultAccount  = web3.eth.accounts[0]
    contract_location = web3.eth.defaultAccount
    accounts = web3.eth.accounts 
    Deed_InNameof = st.selectbox("Select Address of Ownership", options=accounts)
    DeeDEtails = st.text_input("Deed Details", value="Deed To Collectable")
    token_id = st.number_input("Enter a Swap Token ID to display", value=0, step=1)
    if Deed_InNameof:
        st.write(f'This DeeD is in the name of {Deed_InNameof}')

    if  DeeDEtails:
        st.write(f'Details of DeeD  {Deed_InNameof}')

    if token_id:
        st.write(f" You selected {token_id}")

        if st.button('Create Tokenized DeeD'):
            DeeD_hash = genaralReg.functions.deedForItem(Deed_InNameof, DeeDEtails).transact({'from' : contract_location, 'to' : Deed_InNameof})
            DeeD_receipt = web3.eth.waitForTransactionReceipt(DeeD_hash)
            print(DeeD_hash, DeeD_receipt)
            st.write(f'This is your transactionHash {DeeD_hash},Here is your TransactionReceipt {DeeD_receipt}')
            
            token_owner = genaralReg.functions.ownerOf(token_id).transact({'from' : contract_location, 'to' : Deed_InNameof})
            token_receipt = web3.eth.waitForTransactionReceipt(token_owner)
            print(token_owner, token_receipt)
            st.write(f'This is your token hash {token_owner},Here is your receipt of tokenization {token_receipt}')
        
            token_uri = genaralReg.functions.tokenURI(token_id).transact({'from' :contract_location, "to" :  Deed_InNameof})
            receipt_uri = web3.eth.waitForTransactionReceipt(token_uri)
            print(token_uri, receipt_uri)
            st.write(f'This is your URI hash {token_uri},Here is your URI receipt {receipt_uri}')

Swap_DeeD()