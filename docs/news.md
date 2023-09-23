## September 23. 2023

Hi guys, here is my proposition what to do and discuss together with Yama, 
but at the same time ensure that this goes in line with Marco and his targets.

1. Engage a bit more with SBOT Analyzer as already discussed

2. Set up "mydex" together and enhance it a bit like this:

a. Extract the smart contracts and hardhat to a seperate project.

b. Use a testnet instead of the local hardhat node, then deploy it to the web

c Develop some sort of distributed authentication mechanism to this, using
a Merkle proof for ethereum addresses. So the array of authorized addresses
should be hel off chain, where a smart contract does the authorization 
check, storing only a Merkle root.


What do you think? Wuld that be a way to go for me and Yama?





## September 22, 2023
### 📣 Exciting Updates! 🚀

I've been hard at work refining our `SBOT CODALYZER` Solidity analysis tools. Here's a quick rundown of the latest changes:

1️⃣ Moved the check_structures to a dedicated module named bloodhounds.py for better modularity.  

2️⃣ Enhanced the code to dynamically accept the key (like "initial") and paths directly from the command line, making it more flexible and user-friendly.

3️⃣ Introduced a shell script to seamlessly run our Python analyzer, ensuring a smoother user experience.

Big thanks to the OpenAI assistant for guiding us through these improvements! Stay tuned for more updates. 🛠️✨

[Learn more ...](https://github.com/lyrx/sbot)

