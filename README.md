## 勉強中

### メモ

#### ブロックチェーンとは
それまでの流れのhashを自身の中に保持している。  
攻撃者が途中のblockを破壊するとそれ以降のhashが崩れる。

#### ジェネシスブロック
一番最初のblock。  
blockchainがインスタンス化されるときに一緒にシードする必要がある

新しいblockを作る理由はいくつかある。  
マイニングや(鋳造　(forged) )? など

#### Proof of Work(PoW)
新しいブロックが 作られる or 採掘される かを表している。  
誰からも見つけるのは難しく、確認するのは簡単でないといけない

例:)
整数xを整数yと乗算した値のhashが0で終わる場合を求める。  
`hash(x*y) = ***0`

```
from hashlib import sha256

x = 5
y = 0  # まだこのyがどの数字であるべきかはわからない

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1

print(f'The solution is y = {y}')
```

bitcoinではProof of Workのアルゴリズムは`Hashcash`という。

Hashcashは採掘者が競い合い、新しいブロックを作るための問題を解くというもの。  
解いた報酬としてコインがもらえる。
