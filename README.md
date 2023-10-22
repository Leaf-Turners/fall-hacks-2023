# Python API Wraper
Fall hacks 2023.

## Description

## File Structure

## Steps

## Build

Run the command: `python setup.py sdist bdist_wheel`

## Usage

1. Use `pip` to install the module from the `dist` folder, for example: `pip install path/to/local/installation/dist/sfuapiwrapper-1.0.0.tar.gz`
2. Use the module like this:

```python
import sfu_api_wrapper
import asyncio


async def main():
    data = await sfu_api_wrapper.course_offering('cmpt', '120', 'd100')
    print(data.instructors[0].name)


if __name__ == '__main__':
    asyncio.run(main())
```

```
fall-hacks-2023
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ ORIG_HEAD
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           ├─ HEAD
│  │           └─ main
│  ├─ objects
│  │  ├─ 00
│  │  │  └─ a4906ad4fbb0e600915455759098259cc720e4
│  │  ├─ 01
│  │  │  └─ d2d870144a33aeb05c544e7d237d7710c832b1
│  │  ├─ 03
│  │  │  ├─ 46f2a13a4a84db78e241364bacf11c35b59c22
│  │  │  ├─ ba1fb255e6da15ce7820ad639dcdad3cb5e2cc
│  │  │  └─ ebaddc1dd20a9a99ac7ba6d6cc9d4b4efcdd6a
│  │  ├─ 05
│  │  │  └─ c3c3ebddc12f4fa38b4210882310eebdc1b88d
│  │  ├─ 06
│  │  │  └─ d692f1ad22684f3bf50cf708008456925efa32
│  │  ├─ 08
│  │  │  └─ aa1f039a2b40f5306ca0fdc8606202a1fffa27
│  │  ├─ 0c
│  │  │  ├─ 3b37a75178b1fbb7fef4cdf1b6837abe21a6c4
│  │  │  └─ 410900ced25802cdbe4accbd179fea7ad972bf
│  │  ├─ 0e
│  │  │  └─ 36f8b93586173eeec197fbed2044ed8bf1c2b1
│  │  ├─ 10
│  │  │  └─ 1dcf234a869ab7eaa0e6fad1edbb003e832906
│  │  ├─ 13
│  │  │  └─ 0e05af56acca051e25f6099a34533fc588a175
│  │  ├─ 14
│  │  │  ├─ 45411222ed2c58dffea2fdbbd08a993c9d0b2a
│  │  │  └─ 796b3aabcc53463f0a8ddee705ed3f46d1e8d6
│  │  ├─ 15
│  │  │  ├─ 0706a9941c950133a5dac9430a52dfa87d7ff8
│  │  │  └─ 6252c614ebec635fcc6920326c2a509a6b6605
│  │  ├─ 16
│  │  │  └─ 63356bdfbb11d0efd905a7c31c3486e4ea8296
│  │  ├─ 19
│  │  │  └─ 1780e345ef4d25fa104fefd90db7b5e6be29fa
│  │  ├─ 1a
│  │  │  └─ 30b26af381239994cfc9fda43dea7f98f72e21
│  │  ├─ 1b
│  │  │  └─ fcebb5e8907fe3b3965c202625d7a7b9d997e1
│  │  ├─ 1c
│  │  │  └─ cc1f098507d75d305cd6d19196be70bc762009
│  │  ├─ 1e
│  │  │  └─ e865fcd5a561064c49b08f8fae233690bbd762
│  │  ├─ 21
│  │  │  └─ 5519fa7aabb5afd0878cf47d3d3508838aa92e
│  │  ├─ 22
│  │  │  └─ 0d2ec0196e114fe0bec0d31a6662c68b995acd
│  │  ├─ 23
│  │  │  ├─ 8d08398e820e905d4b8f6f7708dd69a989786a
│  │  │  └─ fea13f0ea641c8f0744d2063e99058ace14538
│  │  ├─ 24
│  │  │  ├─ 80178c7e54a1057dfcf89898f2244d495e355b
│  │  │  └─ edf9e677826c9828cdba25e504966f98f1f788
│  │  ├─ 26
│  │  │  ├─ 5638cbc0ec6aca39616cac84c5c904c0ccd423
│  │  │  └─ fdeef88c5134757e174f02c24e06a8fc8c9ad5
│  │  ├─ 27
│  │  │  ├─ 02cad90f5e9d576b053c481079541c097e806a
│  │  │  └─ 65b22dcbbcb8a4d6fe900ff011c76afa296ef9
│  │  ├─ 28
│  │  │  └─ 4aff3f7daf4ef760f0a3a3b14365120b6e5f30
│  │  ├─ 2a
│  │  │  └─ fe4f4a748e9322713fdbbfde94482e747fa150
│  │  ├─ 2d
│  │  │  ├─ 3be9999199d9a1bddc730212315cbb1a0ea747
│  │  │  └─ caace12c889801f9a387704815368aa17eae4e
│  │  ├─ 2e
│  │  │  └─ 41cc4a4d6672e2590caa87cdade078658c5f38
│  │  ├─ 30
│  │  │  └─ f905c92d658566495ceb4b4a05abc34fb03520
│  │  ├─ 33
│  │  │  └─ 9b4df0e64a27ef93d4b2d2325c96ece892f932
│  │  ├─ 36
│  │  │  └─ b822e4aa75a1971436d4dad628df5456789eb6
│  │  ├─ 37
│  │  │  ├─ 25f125b00546fcda2278227819aede6e9136eb
│  │  │  └─ eabf9bd45151fb17820b97dcf79bef8d30a0ea
│  │  ├─ 39
│  │  │  └─ 1dfa3919e93c92e62af3b1872dc4ab59b0240d
│  │  ├─ 3c
│  │  │  └─ 7dd38e9d1db86de5c40be60fb15c2f946cb6fa
│  │  ├─ 3d
│  │  │  └─ 6f77376d40da63bef5c41ac143ad06cee9a654
│  │  ├─ 3e
│  │  │  └─ 3a99ab8ccbe6c96ab30bfa727c8c641584d451
│  │  ├─ 3f
│  │  │  └─ e7096b2c90eda11bc543479203b00918761a35
│  │  ├─ 44
│  │  │  └─ e4872a966128899fec7ef4c0e7e8b31ce72850
│  │  ├─ 45
│  │  │  └─ 6b9d0ecea340f6787b4113bf50b2e41cfdda4f
│  │  ├─ 49
│  │  │  └─ 28fb85a6f04e0d2486add1278e0371a15481dc
│  │  ├─ 4c
│  │  │  ├─ 29eb16aee71c29705594e7384410afaa192c12
│  │  │  ├─ 708eff4390f92e7ec90d6642e177c857bec830
│  │  │  └─ 8c5f5d67f22251e6c61da00a88e9769ff531f1
│  │  ├─ 4f
│  │  │  └─ db492aa7e184c10c4ccb0c8c71a61823dbe345
│  │  ├─ 50
│  │  │  └─ b51a701d2e016ce74ed14994b1babfa4c5131e
│  │  ├─ 52
│  │  │  ├─ 6a0066c3eeeade75f289e3f9aedbc063677bac
│  │  │  └─ 84edc6fa364aa4f46828caeeacb70b69b9ec5e
│  │  ├─ 53
│  │  │  └─ 95bacc5efa1e56f15ca54d317aede00427d3f3
│  │  ├─ 55
│  │  │  └─ de1a7f16709fcb8ab5111161b623b94957c345
│  │  ├─ 56
│  │  │  ├─ 900b5e8278369036504016d732765b003a3586
│  │  │  └─ a6be676977524177cb3368d01c11a7b734b9ee
│  │  ├─ 57
│  │  │  └─ f25356bcada976498e7e8c9e72550d81c74c68
│  │  ├─ 58
│  │  │  └─ f2d6f8a54d11739a7b9c6b18e5d438d22da728
│  │  ├─ 59
│  │  │  ├─ ae873d104d34b34f9e289f90e1c8b350e07211
│  │  │  └─ baa9d74f2a76a7c9e42efd92b75fb66e172243
│  │  ├─ 5b
│  │  │  └─ ecc17c04a9e3ad1c2a15f53252b7bb5a7517e7
│  │  ├─ 5c
│  │  │  ├─ 2850a166a9ffa2afc7326a7084fcb5cf3d98eb
│  │  │  └─ 970195c33fdcd07b72a62196fe8057ab9e82aa
│  │  ├─ 5e
│  │  │  └─ fe232df96ffbd9f01b565dd08d7cb52805b9e9
│  │  ├─ 5f
│  │  │  └─ a2885a9714ac4f19db4540a18713367b3fb03c
│  │  ├─ 61
│  │  │  └─ e5a22ab3a6bbf43f2ef558876c5435c78bce55
│  │  ├─ 62
│  │  │  ├─ ad8c7cf9a7b48bf76b384f8154ab87bc7c8e80
│  │  │  ├─ c893550adb53d3a8fc29a1584ff831cb829062
│  │  │  └─ fcdd9483c19d14a46d9c04f461050ceb3fac2b
│  │  ├─ 63
│  │  │  └─ eea914028d82b2eb883a37c9544d40da7ed80c
│  │  ├─ 66
│  │  │  └─ 492e22ce852983569533b12b92453af8dab59b
│  │  ├─ 6c
│  │  │  ├─ aacf74b275972f718e99645104b1ba86bd57ac
│  │  │  └─ ff1b101f96439e76aa36d1852f3044cc47a3e5
│  │  ├─ 6d
│  │  │  └─ cac2e68b8558477dcf9921fafa9b95fd5f5a94
│  │  ├─ 6e
│  │  │  └─ 66632f4354155ba792a7aa11a86e05cc87533b
│  │  ├─ 6f
│  │  │  └─ dfa7c9744d7c400d949d99dc6f35fe841e2d5e
│  │  ├─ 71
│  │  │  └─ eccb6555d5358bee315fe6554a346cb3495028
│  │  ├─ 72
│  │  │  ├─ 8ff56ac99cf1214c2de006830098c3708c49aa
│  │  │  ├─ 958c5c91aab3598579acbb10d658ad0d93694b
│  │  │  └─ f6a4b054419084eb81773efa853b210ebfddf8
│  │  ├─ 74
│  │  │  └─ de166a5ac6d72c778270dcb3e74e0ac448648f
│  │  ├─ 78
│  │  │  └─ 69c5d2acf5d6ee444f5bda9304528cb2332177
│  │  ├─ 79
│  │  │  └─ c81cf670329de793246a4ed2f9f88444d0d326
│  │  ├─ 7b
│  │  │  └─ 2fdc3fdbe1505a3fd5a97e2a65f9630bd9591f
│  │  ├─ 7c
│  │  │  └─ 3356e3ce7956651a2d5589255ccdc7ebbc902f
│  │  ├─ 7f
│  │  │  └─ b4cea0681df64a699a0111d4474d9fc4f35875
│  │  ├─ 80
│  │  │  ├─ 09894c4c2b30a46576c0a7411e7d0d282b6f4c
│  │  │  ├─ 5920b51bd70052d80d987bf67a5e6d525797b7
│  │  │  └─ 5c6950adb76b9b1add51385e449c66ea5c1518
│  │  ├─ 81
│  │  │  └─ 652bdcf623ba590ea2b21a4ff3f50d4fee1267
│  │  ├─ 83
│  │  │  └─ 74b3ff83a477bf29fd602f8fde80b703e37252
│  │  ├─ 88
│  │  │  └─ 5c419ac0f8507bee30f34d20094fdc284f7d00
│  │  ├─ 89
│  │  │  └─ 028a81a161e27c62c04c2ecf8ef45d98b3f353
│  │  ├─ 8a
│  │  │  ├─ 0297eca882d097408d44677f02ab782f045f0b
│  │  │  └─ f244589bffebc9e4897e7716159111f2c7ee95
│  │  ├─ 8c
│  │  │  ├─ 0bc88642d410cbc930620f6ffa88f742b5eb6a
│  │  │  ├─ 2eb7aa4c3deb60ef8803f735616d5fc7c18881
│  │  │  └─ e98205777b27639cea3e5ab6a0466d209c438e
│  │  ├─ 8d
│  │  │  ├─ 4be17565fad76b7b93d8b65722d01640af5552
│  │  │  └─ 76541e5b68562d8e667c73f2e683e5a7d76ad8
│  │  ├─ 8f
│  │  │  └─ 1c0e7a7d04c5a35ee6a8ec2413b048b4075da9
│  │  ├─ 91
│  │  │  ├─ 60d13ff997db81eb2ff8bb00d014c58e88e2b6
│  │  │  ├─ 6e4a6f46f8992007c23d268d748665365304dc
│  │  │  ├─ d347d9891e88fce5604850ca5676b313b1b412
│  │  │  └─ ea7e8d2e4964f5a43e04d6292911ad61a30fc8
│  │  ├─ 93
│  │  │  ├─ 70c4df99919a64535f86aa8ba921665a8b8367
│  │  │  ├─ 8eb13501b55ec32b54daafde083674fabeacdd
│  │  │  ├─ 90b516732d562b7a65e7726e6d19c96ba9b556
│  │  │  └─ d4f7818a6ed1c177cc6bf064852bfb2c1e266e
│  │  ├─ 94
│  │  │  └─ e61139777ebf67c29029c8184f0d75d391b5d4
│  │  ├─ 96
│  │  │  └─ 9f594eed24702c9ac6a4f48226e557d004c26a
│  │  ├─ 99
│  │  │  └─ 1e5bb7d03bd9a8432f221cbf6025ba5c9654b1
│  │  ├─ 9b
│  │  │  └─ eea6e7cc9677dfe361d025529e8a5657f55b5d
│  │  ├─ 9c
│  │  │  └─ 4a3c2434753e00353780ab8b5e132f3ac9a7c5
│  │  ├─ 9d
│  │  │  ├─ 1f3eb9bdab535e316a7f8f0e4a5dfcd1eee019
│  │  │  └─ 634102faecf9a183c377257dbec61b2fb1f0e9
│  │  ├─ 9e
│  │  │  ├─ 432bae9a5ae5337562af4ffd0c361767bc0a9a
│  │  │  └─ 53b64d72a7386a9abc91eb860e2216578ea2d2
│  │  ├─ a0
│  │  │  └─ 42e04583ec1275c1bdf83660790e45b91171ad
│  │  ├─ ac
│  │  │  └─ 50f040a6fafcdb7a787a7507197fd83bf809bc
│  │  ├─ ad
│  │  │  ├─ 77d8e855492d2d00f8fc3125bea851a94a762f
│  │  │  └─ 8d0668e0fc78af8149b68a47af3766a0af432c
│  │  ├─ b1
│  │  │  └─ c6e6d93ee0b5714d47df598c6b8f61145c641c
│  │  ├─ b2
│  │  │  └─ 0480528008cf56b611f5a74163898210e46fa0
│  │  ├─ b3
│  │  │  └─ 35c6e8c5d3942c1b1b7c1e586c1e3842b6d410
│  │  ├─ b7
│  │  │  ├─ 59186d2ccdb80d1030711f83fb4d64103749eb
│  │  │  └─ e61386d043cc565674671c608d0998c6721027
│  │  ├─ b8
│  │  │  └─ e6b9cf8405c192a4f208faee9d0f75af9c779f
│  │  ├─ b9
│  │  │  └─ 89d4087ffd51fb41b8cd31f9953ed2861d09c4
│  │  ├─ bb
│  │  │  ├─ 0e421c5da42f9c4a08f719f8944605d39e748e
│  │  │  ├─ 126a0e0de4d2c52ee1b651083c60a8c22c6511
│  │  │  └─ c182fc9ea8268eb173f3c94bd945af37d366d9
│  │  ├─ bc
│  │  │  ├─ 86698044c540af6d1718883e11585a2c848275
│  │  │  └─ c8c2753d48a7313e230949af5bab0789243076
│  │  ├─ bd
│  │  │  └─ 9bb8b8b38812662294e4d683be6d3cbac941eb
│  │  ├─ be
│  │  │  ├─ a6d384b7d933cd7efb13ca401312c7b89bffc3
│  │  │  └─ c465762fc501b819da14607ee8d769a03d59ff
│  │  ├─ bf
│  │  │  └─ f7fbe33d568a5c38e5eeda1ccacc3bed7b4608
│  │  ├─ c1
│  │  │  └─ 4df677920593856231b4d160de7055bf4d8901
│  │  ├─ c2
│  │  │  └─ e34962c845dbdcc457251f49719c1c4cbf3b9c
│  │  ├─ c3
│  │  │  └─ 7934294986b413deffbb80f6893278c0e0e734
│  │  ├─ c5
│  │  │  └─ f94b3918623e876a965a0da9c0541759b7be3c
│  │  ├─ c6
│  │  │  └─ 52817a63e8b55ff3eec98665da98a19dbaf753
│  │  ├─ c8
│  │  │  └─ a64792db427918dc121bef5b01fc7a6cc6e940
│  │  ├─ cc
│  │  │  └─ 34c2f61bb5fac142641d8ee7101e368695ce01
│  │  ├─ cf
│  │  │  ├─ 1d71acef082fe68b512ce35b39e7c6f3336dca
│  │  │  ├─ ba998146d20eb3001bb00e5b0e3d08a5df607f
│  │  │  ├─ d5b15fbc489c79105c259ca1de24ca5862973f
│  │  │  └─ e24f48ccacde2b33d9eb6dff5c25abed1a6e70
│  │  ├─ d1
│  │  │  ├─ 6f5713aafe8fcc8ef8d389c75a3c9d5c60dbfe
│  │  │  └─ ed187527102794681337a029fb5b355fe3eb89
│  │  ├─ d2
│  │  │  └─ 7375513d13a719249f81e014c13c7cdd0449fb
│  │  ├─ d3
│  │  │  ├─ 4d576c31a563eb1f2d45dae53b6e9c310f206b
│  │  │  └─ 929523b127c37cd720a60e13693392ae562620
│  │  ├─ d4
│  │  │  └─ 9883dec131bd3fe31f0e3d37f98839b917832a
│  │  ├─ d8
│  │  │  └─ 8b81a70070eb961a0f82bb5a0c6c7ec9824475
│  │  ├─ e4
│  │  │  ├─ b052a5b77fde74708ff7dcde649a143284c009
│  │  │  └─ e096610e17b44e87de1f8a0bcd70275f7f07d2
│  │  ├─ e6
│  │  │  ├─ 64964d6f494fc14a84898424ecaace752d5f52
│  │  │  ├─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  │  └─ e92efd5bd6a31efc84c1713dafe81b7acc57d1
│  │  ├─ e7
│  │  │  └─ 99874dc1e9d3eb30bdc4dcc7bb62cc050a3c5e
│  │  ├─ e8
│  │  │  └─ 6afc0d1a8fe5e06401c406f0be3f5a3d84f89d
│  │  ├─ ea
│  │  │  ├─ 8b22a606f776bc3372cc6661166f421046450d
│  │  │  └─ a2b2dbd3335991c2b1ee7e2c8234b92af914ef
│  │  ├─ eb
│  │  │  └─ 3ec5cc52978c05e931c167e00a23d22268d5e8
│  │  ├─ ec
│  │  │  └─ f90fb4e76d038ce149c1fe3e89ca3792d8d039
│  │  ├─ ed
│  │  │  ├─ 0c632adfd7bf06e513a54ef5b31439118e40f8
│  │  │  ├─ 36c478428a8cd46613c28587050a3d655db541
│  │  │  └─ c9171ed1667d0d248b766050ab946425c3f617
│  │  ├─ f0
│  │  │  └─ 74d2a5c5609251c8644eb656c39417070d4160
│  │  ├─ f2
│  │  │  ├─ 09a5fc69b4558b7e80cb12363ef0290243e829
│  │  │  ├─ 5a9f000451b10d56c4d21b51c7124e23e0cf5b
│  │  │  ├─ 5b0beaa9d062a941e0ee8f168b6f1e737b85e9
│  │  │  └─ cf249478cc2256f9a3cafdf98084b41e842f67
│  │  ├─ f3
│  │  │  └─ c8761e9f2ae66a449c828826e2221f031a6547
│  │  ├─ f4
│  │  │  └─ d2bee493e22d8f6e0b18b0143e1873fd62bb6f
│  │  ├─ f5
│  │  │  └─ e30c26cfd56aa2d4aa6a295574a1c708a18a3a
│  │  ├─ f8
│  │  │  └─ f2cf8d7fc1c6b2fc08fc16f36f7972f7c5d2d3
│  │  ├─ fc
│  │  │  └─ d5c3182247ef8e574be5682302b14bf8f048e3
│  │  ├─ ff
│  │  │  └─ e52fed41b4707bd38668cfe94c279a1be37b8e
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-812cd49c0773294843ea816d05499a0ae10bf289.idx
│  │     └─ pack-812cd49c0773294843ea816d05499a0ae10bf289.pack
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     └─ main
│     └─ tags
├─ .gitignore
├─ README.md
├─ SFU-Course-Diggers-Web-Scraper-master
│  ├─ .gitignore
│  ├─ LICENSE
│  ├─ README.md
│  └─ scraper.py
├─ dist
│  ├─ sfuapiwrapper-1.0.0-py3-none-any.whl
│  └─ sfuapiwrapper-1.0.0.tar.gz
├─ requirements.txt
├─ setup.py
└─ sfu_api_wrapper
   ├─ __init__.py
   ├─ api_classes
   │  ├─ __init__.py
   │  ├─ course.py
   │  ├─ instructor.py
   │  └─ schedule.py
   ├─ course_names_to_ids.json
   ├─ grades.py
   ├─ requests.py
   ├─ scraper.py
   ├─ version.py
   └─ wrapper_functions
      ├─ __init__.py
      ├─ course_offering.py
      ├─ departments.py
      ├─ terms.py
      └─ years.py

```