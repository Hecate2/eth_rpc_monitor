'Thanks to https://github.com/michaelroycummings/aave_health_factor_checker'

from web3 import Web3
from functools import wraps
import traceback
from typing import Union
from requests.exceptions import HTTPError


class AaveHealthFactor:
    '''
    Contains functions to access the "Lending Pool" contract of the Aave DAO
    and return the Health factor of a given account.
    Resources
    ---------
    Aave Deployed Contracts: https://docs.aave.com/developers/v/2.0/deployed-contracts/deployed-contracts
    Lending Pool functions: https://docs.aave.com/developers/v/2.0/the-core-protocol/lendingpool
    '''

    def __init__(self, w3 = None):
        self.blockchain_name = 'ethereum'
        self.blockchain_net = 'mainnet'
        self.lending_pool_abi_filename = 'lending_pool_abi.json'
        self.lending_pool_address = '0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9'
        self.infura_nodes = ['https://rpc.ankr.com/eth']
        ## Constants
        self.max_sol_hex = '0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        self.w3 = w3


    def connect(self, infura_id: str = None):
        ''' Return a web3 session object or False if a faulty Infura ID is provided. '''
        # print('Attempting to connect to Ethereum node.')
        for node in self.infura_nodes:
            endpoint = Web3.HTTPProvider(f'{node}/{infura_id}')
            w3 = Web3(endpoint)
            is_connected = w3.isConnected()
            if is_connected is True:
                return w3
        print('Connection failed.')
        return False


    def get_lending_pool_abi(self):
        """
        ## Try to Get ABI from Etherscan
        # Hmm... this is on the farthest backburner for web3.py (https://github.com/ethereum/web3.py/issues/1711)
        # Could build a web scarper for Etherscan in the future.

        ## Load Saved ABI
        self.lending_pool_abi_filename
        try:
            with open(self.lending_pool_abi_filename) as json_file:
                abi = json.load(json_file)
        except FileNotFoundError:
            print('Please move the executable to the same folder as the `lending_pool_abi.json` file.')
            if self.exe:
                input('Press enter to exit the program.')
        return abi
        """
        true = True
        false = False
        return [{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"onBehalfOf","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"borrowRateMode","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"borrowRate","type":"uint256"},{"indexed":true,"internalType":"uint16","name":"referral","type":"uint16"}],"name":"Borrow","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"onBehalfOf","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"uint16","name":"referral","type":"uint16"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"initiator","type":"address"},{"indexed":true,"internalType":"address","name":"asset","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"premium","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"FlashLoan","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"collateralAsset","type":"address"},{"indexed":true,"internalType":"address","name":"debtAsset","type":"address"},{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"debtToCover","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"liquidatedCollateralAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"liquidator","type":"address"},{"indexed":false,"internalType":"bool","name":"receiveAToken","type":"bool"}],"name":"LiquidationCall","type":"event"},{"anonymous":false,"inputs":[],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":true,"internalType":"address","name":"user","type":"address"}],"name":"RebalanceStableBorrowRate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"repayer","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Repay","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":false,"internalType":"uint256","name":"liquidityRate","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"stableBorrowRate","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"variableBorrowRate","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"liquidityIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"variableBorrowIndex","type":"uint256"}],"name":"ReserveDataUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":true,"internalType":"address","name":"user","type":"address"}],"name":"ReserveUsedAsCollateralDisabled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":true,"internalType":"address","name":"user","type":"address"}],"name":"ReserveUsedAsCollateralEnabled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"rateMode","type":"uint256"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"reserve","type":"address"},{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"FLASHLOAN_PREMIUM_TOTAL","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"LENDINGPOOL_REVISION","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_NUMBER_RESERVES","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_STABLE_RATE_BORROW_SIZE_PERCENT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"interestRateMode","type":"uint256"},{"internalType":"uint16","name":"referralCode","type":"uint16"},{"internalType":"address","name":"onBehalfOf","type":"address"}],"name":"borrow","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"onBehalfOf","type":"address"},{"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"balanceFromBefore","type":"uint256"},{"internalType":"uint256","name":"balanceToBefore","type":"uint256"}],"name":"finalizeTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"receiverAddress","type":"address"},{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"uint256[]","name":"modes","type":"uint256[]"},{"internalType":"address","name":"onBehalfOf","type":"address"},{"internalType":"bytes","name":"params","type":"bytes"},{"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"flashLoan","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAddressesProvider","outputs":[{"internalType":"contract ILendingPoolAddressesProvider","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"}],"name":"getConfiguration","outputs":[{"components":[{"internalType":"uint256","name":"data","type":"uint256"}],"internalType":"struct DataTypes.ReserveConfigurationMap","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"}],"name":"getReserveData","outputs":[{"components":[{"components":[{"internalType":"uint256","name":"data","type":"uint256"}],"internalType":"struct DataTypes.ReserveConfigurationMap","name":"configuration","type":"tuple"},{"internalType":"uint128","name":"liquidityIndex","type":"uint128"},{"internalType":"uint128","name":"variableBorrowIndex","type":"uint128"},{"internalType":"uint128","name":"currentLiquidityRate","type":"uint128"},{"internalType":"uint128","name":"currentVariableBorrowRate","type":"uint128"},{"internalType":"uint128","name":"currentStableBorrowRate","type":"uint128"},{"internalType":"uint40","name":"lastUpdateTimestamp","type":"uint40"},{"internalType":"address","name":"aTokenAddress","type":"address"},{"internalType":"address","name":"stableDebtTokenAddress","type":"address"},{"internalType":"address","name":"variableDebtTokenAddress","type":"address"},{"internalType":"address","name":"interestRateStrategyAddress","type":"address"},{"internalType":"uint8","name":"id","type":"uint8"}],"internalType":"struct DataTypes.ReserveData","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"}],"name":"getReserveNormalizedIncome","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"}],"name":"getReserveNormalizedVariableDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReservesList","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getUserAccountData","outputs":[{"internalType":"uint256","name":"totalCollateralETH","type":"uint256"},{"internalType":"uint256","name":"totalDebtETH","type":"uint256"},{"internalType":"uint256","name":"availableBorrowsETH","type":"uint256"},{"internalType":"uint256","name":"currentLiquidationThreshold","type":"uint256"},{"internalType":"uint256","name":"ltv","type":"uint256"},{"internalType":"uint256","name":"healthFactor","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getUserConfiguration","outputs":[{"components":[{"internalType":"uint256","name":"data","type":"uint256"}],"internalType":"struct DataTypes.UserConfigurationMap","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"address","name":"aTokenAddress","type":"address"},{"internalType":"address","name":"stableDebtAddress","type":"address"},{"internalType":"address","name":"variableDebtAddress","type":"address"},{"internalType":"address","name":"interestRateStrategyAddress","type":"address"}],"name":"initReserve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract ILendingPoolAddressesProvider","name":"provider","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"collateralAsset","type":"address"},{"internalType":"address","name":"debtAsset","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"debtToCover","type":"uint256"},{"internalType":"bool","name":"receiveAToken","type":"bool"}],"name":"liquidationCall","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"address","name":"user","type":"address"}],"name":"rebalanceStableBorrowRate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rateMode","type":"uint256"},{"internalType":"address","name":"onBehalfOf","type":"address"}],"name":"repay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"configuration","type":"uint256"}],"name":"setConfiguration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"val","type":"bool"}],"name":"setPause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"address","name":"rateStrategyAddress","type":"address"}],"name":"setReserveInterestRateStrategyAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"bool","name":"useAsCollateral","type":"bool"}],"name":"setUserUseReserveAsCollateral","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"rateMode","type":"uint256"}],"name":"swapBorrowRateMode","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"withdraw","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]


    def get_health_factor_at_block(self, borrower_address: str, block_number: int):
        # For the latest value, you can also use self.lending_pool_contract.functions.getUserAccountData(borrower_address).call()
        (
            totalCollateralETH, totalDebtETH, availableBorrowsETH,
            currentLiquidationThreshold, ltv, health_factor
        ) = self.lending_pool_contract.caller(block_identifier=block_number).getUserAccountData(borrower_address)
        return health_factor


    def exe_wait(function):
        '''
        A decorator that catches and print an exception and pauses for the user to see,
        before ending the execution and closing the program.
        '''
        @wraps(function)
        def exe_wait_wrapper(self, *args, **kwargs):
            try:
                return function(self, *args, **kwargs)
            except Exception:
                traceback.print_exc()
                input('Press enter to exit the program.')
        return exe_wait_wrapper

    @exe_wait
    def run(self, borrower_address: str = None, infura_id: str = None, block_number: Union[int, None] = None, exe: bool = False):
        ''' Cleans Inputs, queries the Health Factor, and handing query exceptions. '''
        self.exe = exe
        ## Clean Inputs - Borrower Address
        # while True:
            # if infura_id is None:
            #     infura_id = input('Please provide an "infura_id" below... \n')
            # self.w3 = self.connect(infura_id=infura_id)
            # if self.w3 is not False:
            #     print("Connected to Infura's Ethereum Node")
            #     break
            # else:
            #     infura_id = input('The "infura_id" provided is faulty. Please provide a working Infura Project ID address below... \n')

        ## Clean Inputs - Borrower Address
        # while True:
            # if self.w3.isAddress(borrower_address) is True:
            #     borrower_address = Web3.toChecksumAddress(borrower_address)
            #     break
            # if borrower_address is None:
            #     borrower_address = input('Please provide a "borrower_address" below... \n')
            # else:
            #     borrower_address = input('The "borrower_address" provided is not an Ethereum address. Please provide an Ethereum address below... \n')

        ## Clean Inputs - Block Number
        while True:
            if block_number is not None:
                break
            block_number = self.w3.eth.getBlock('latest').number
            # response = input('Please enter a block number, or press enter to return the health factor of the latest block. \n')
            # if response == '':
            #     block_number = Web3.eth.get_block('latest')
            #     break
            # try:
            #     block_number = int(response)
            #     break
            # except ValueError:
            #     print('An integer value or no value must be given.')

        ## Get Aave Lending Pool Contract
        lending_pool_abi = self.get_lending_pool_abi()
        self.lending_pool_contract = self.w3.eth.contract(address=self.lending_pool_address, abi=lending_pool_abi)

        ## Get Health Factor for Address
        try:
            health_factor = self.get_health_factor_at_block(borrower_address, block_number)
        except HTTPError:
            print('Sorry, the Ethereum node provided does not allow historical access to a block that far back.')
            if self.exe:
                input('Press enter to exit the program.')
            return

        ## Return Health Factor to User
        # if Web3.toHex(health_factor) == self.max_sol_hex:
        #     print(f'The address "{borrower_address}" has no outstanding borrow position on Aave.\n')
        # else:
        #     print(f'Health factor is {health_factor}: \n - for address {borrower_address} \n - at block {block_number}')
        # if self.exe:
        #     input('Press enter to exit the program.')
        return health_factor