import base64
import json
from typing import Dict

import eth_account.messages
from web3.auto import w3


class Web3Token:
    def __init__(self, token: str):
        json_data = json.loads(base64.b64decode(token))
        self.signature = json_data['signature']
        body_parts = json_data['body'].split('\n\n')
        self.message = body_parts[-1]
        self.statement = body_parts[0] if len(body_parts) > 1 else None
        self.__body_hash = None
        self.__signer = None

    @property
    def body(self) -> str:
        if self.statement is not None:
            return self.statement + '\n\n' + self.message
        return self.message

    @property
    def body_hash(self) -> 'eth_account.messages.HexBytes':
        """
        Convert the body into a message hash, to be signed.
        """
        if self.__body_hash is None:
            self.__body_hash = eth_account.messages.defunct_hash_message(
                text=self.body
            )
        return self.__body_hash

    def get_signer(self, validate: bool = True) -> str:
        """
        Get the address of the account that signed the message.
        Returns address of etherium wallet
        """
        if self.__signer is None:
            signer = w3.eth.account.recoverHash(
                self.body_hash,
                signature=self.signature
            )
            if validate and not w3.isAddress(signer):
                raise Exception(f'Invalid Token')
            self.__signer = signer
        return self.__signer

    def get_data(self) -> Dict[str, str]:
        """
        Get dict representation of signed message
        """
        return dict(
            map(
                lambda s: s.split(': '),
                self.message.split('\n')
            )
        )


if __name__ == '__main__':
    token_ = input(f'Enter your token: ')
    web3token = Web3Token(token_)
    print('Signer:', web3token.get_signer(validate=True))
    print('Data:', web3token.get_data())
    print('Statement:', web3token.statement)
