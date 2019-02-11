# coding: UTF-8

import hashlib
import json
from time import time

class Blokchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

    # ジェネシスブロックを作る
    self.new_block(previous_hash=1, proof=100)
  
  """
  ブロックチェーンに新しいブロックを作る
  :param proof: <int> プルーフ・オブ・ワークアルゴリズムから得られるプルーフ
  :param previous_hash: (オプション) <str> 前のブロックのハッシュ
  :return: <dict> 新しいブロック
  """
  def new_block(self, proof, previous_hash=None):
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1]),
    }

    # 現在のトランザクションリストをリセット
    self.current_transactions = []

    self.chain.append(block)
    return block

  """
  次に採掘されるブロックに加える新しいトランザクションを作る
  :param sender: <str> 送信者のアドレス
  :param recipient: <str> 受信者のアドレス
  :param amount: <int> 量
  :return: <int> このトランザクションを含むブロックのアドレス
  """
  def new_transcation(self, sender, recipient, amount):
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount,
    })

    return self.last_block['index'] + 1
  
  """
  ブロックの SHA-256 ハッシュを作る
  :param block: <dict> ブロック
  :return <str>
  """
  @staticmethod
  def hash(block):
    # 必ずディクショナリ（辞書型のオブジェクト）がソートされている必要がある。そうでないと一貫性のないhashとなってしまう
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
  
  @property
  def last_block(self):
    # チェーンの最後のブロックをリターンする
    return self.chain[-1]

  """
  シンプルなProof of Workのアルゴリズム
  - hash(pp')の最初の4つが0となるようなp'を探す。
  - p は1つ前のブロックのプルーフ、 p'は新しいブロックのプルーフ
  :param last_proof: <int>
  :return: <int>
  """
  def proof_of_work(self, last_proof):
    proof = 0
    while self.valid_proof(last_proof, proof) is False:
      proof += 1
    
    return proof

  """
  プルーフが正しいかを確認する: hash(last_proof, proof)の最初の4つが0となっているか？
  :param last_proof: <int> 前のプルーフ
  :param proof: <int> 現在のプルーフ
  :return: <bool> 正しければ true 、そうでなれけば false
  """
  @staticmethod
  def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    return guess_hash[:4] == "0000"

