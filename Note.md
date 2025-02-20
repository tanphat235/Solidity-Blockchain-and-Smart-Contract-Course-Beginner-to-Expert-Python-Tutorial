Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial

Link Course: https://www.youtube.com/watch?v=M576WGiDBdQ
Doc: https://github.com/smartcontractkit/full-blockchain-solidity-course-py

-----------------------------------------------------------------------------------------------------------------------
Bitcoin, blockchain có ý nghĩa gì? 0 - 24:55

Cách hoạt động của Blockchain, Gas fee, Gwei, Private key, Public key, transaction,POW POS 24:55 - 1:29:30

-----------------------------------------------------------------------------------------------------------------------
Lesson 1: Simple Storage 1:29:30 - 2:09:20 (SOLIDITY)
- pragma solidity ^0.6.0; => Dùng dấu ^ để code có thể chạy trong mọi version 0.6 khác chứ k chỉ 1 version 0.6.0
- public function: là function có thể  gọi bởi bất kì ai
- External function: là function chỉ có thể gọi bởi những function khác ngoài function gốc
- Internal function: là function chỉ có thể được gọi bởi các function bên trong function gốc
- Private function: là function chỉ được hiển thị bởi contract deploy
- View: là từ để chỉ rằng function này chỉ để xem. 
- Pure: là từ chỉ function này để view nhưng có thể tính toán giá trị bên trong nhưng k thể thay đổi giá trị của nó.
- Các function hay variables màu xanh là chỉ để view. CÁc function màu vàng là để tương tác thay đổi
- Memory: là lưu dữ liệu khi hàm được chạy thôi, chạy xong là k còn lưu nữa 
- Storage: là lưu dữ liệu cứng luôn, có thể dùng đi dùng lại ở những chỗ khác
- // SPDX-License-Identifier: MIT – là câu để chỉ code này có thể được sử dụng free mà k bị bản quyền
- Injected Web3: là để liên kết với ví như metamask
- Web3 Provider: là để chạy blockchain của riêng mình, như chạy node…

-----------------------------------------------------------------------------------------------------------------------
Lesson 2: Storage Factory 2:09:20 – 2:24:00 (SOLIDITY)
- Factory Pattern
- Import file giữa 2 file .sol
- Dùng file .sol khác để gọi file .sol được import. Và gọi cả các function trong file đó. 
- SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])) là câu lệnh để lấy ra address của index bên trong array. Để chỉ cho máy tính hiểu là cần tương tác với phần tử nào, địa chỉ nào. (mỗi phần tử trong array sẽ được deploy bởi 1 address khác nhau)
- Bất kì khi nào interact với Contract thì cần phải có 2 thứ {Address, ABI}
- Inheritance : 2:24:00 - 2:26:24
- Cách inheritance function

-----------------------------------------------------------------------------------------------------------------------
Lesson 3: Fund me 2:26:24 – 3:03:00 Part 1 (SOLIDITY)
- Payable: là kiểu function có thể gán thêm value vào mỗi khi run function (Payable HIển thị trên Remix là màu đỏ)
- Msg.sender là người gọi function để send token.
- Msg.value là số lượng của msg.sender gửi đi
- Cách để dùng API của Chainlink lấy được giá BTC hiện  tại. Deploy DataConsumerV3 để lấy được giá 
- ABI:  Application Binary Interface: Là dùng để nói cho Solidity hoặc ngôn ngữ khác cách function có thể gọi bằng contract khác. Tức là muốn gọi nó phải làm đúng theo ABI chỉ thì mới gọi được. Có nghĩa là khi tương tác với contract thì phải bắt buộc có ABI
- Hướng dẫn sử dụng API Chainlink để lấy được giá của token hiện tại.

Lesson 3: Fund me 2:26:24 – 3:26:36 Part 2 (SOLIDITY)
- Tính toán biến đổi Wei, Gwei, ETH
- Require để đặt min transaction
- Withdraw code
- This: là để chỉ contract đang tương tác. Address(this) là address của contract 
- Constructor() public {} : hàm này giống như init. Nó sẽ execute ngay khi deploy contract
- Gửi token đến và rút token ra. Và update lại balance.
- Tạo 1 array để lưu danh sách các funders. Và tạo 1 array mới để delete hết các funders cũ đã lưu sau khi withdraw

-----------------------------------------------------------------------------------------------------------------------
Lesson 4: Web3.py simple storage 3:26:36 - 3:57:10 (PYTHON DEPLOY)
- Setup môi trường, thư viện để deploy từ python lên blockchain
- Cách ghi và đọc file sol từ python
- Dùng và tra cứu document của thư viện Web3.py (https://web3py.readthedocs.io/en/stable/web3.contract.html)
- Cách truy vấn dữ liệu từ file bytecode được deploy (lấy abi, object...)
- Dùng Ganache để fake blockchain chạy trên local thay cho testnet