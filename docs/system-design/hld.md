

# HLD

## Basics

| Term          | Size                                      | Notes                                          |
| ------------- | ----------------------------------------- | ---------------------------------------------- |
| **Bit**       | 1 bit                                     | Smallest unit of data, either 0 or 1           |
| **Nibble**    | 4 bits                                    | Half a byte. One hex digit represents a nibble |
| **Byte**      | 8 bits = 2 nibbles                        | Can represent values from 0 to 255             |
| **Hex Digit** | 4 bits = 1 nibble                         | E.g., `F` = `1111`, `A` = `1010`               |
| **Word**      | 16 bits (2 bytes) (in some architectures) | Architecture-dependent                         |

### word = 2 Byte = 16 bit = 4 nibbles(hexDigit)  


![](../../assets/images/HDL/biteTrick.png)


| Zeros    | Traffic         | Storage   |
|----------|----------------|-----------|
| 3 zeros  | thousand       | KB        |
| 6 zeros  | million        | MB        |
| 9 zeros  | billion        | GB        |
| 12 zeros | trillion       | TB        |
| 15 zeros | quadrillion    | PB        |


## Netowrk protocols
What is client server Model
What is Peer to Peer to model
Http ,tcp, udp, FTP, SMTP

The OSI (Open Systems Interconnection) Model is a set of rules that explains how different computer systems communicate over a network. OSI Model was developed by the International Organization for Standardization (ISO). The OSI Model consists of 7 layers and each layer has specific functions and responsibilities.

- Physical Layer
- Data Link Layer
- Network Layer
- Transport Layer
- Session Layer
- Presentation Layer
- Application Layer

we will focus on Application layer and transport layer

Application layer can be divided into two parts 
    - Client server protocol
        - !Http
        - FTP
        - SMTP
        - !WebSocket
    - Peer2Peer protocol
        - !webRTC


![](../../assets/diagrams/HLD/networklayer.drawio.png)

## Cap Theorem
- Latency vs throughput
- Availablity VS consisitency
- Performance vs Scalability
    - Vertical scaling
    - Horizontal scaling

![](../../assets/images/HDL/cap1.png)

![](../../assets/images/HDL/cap2.png)



## Monolithic vs Microservices

#### Phases to create microservices
- Decomposition
    - Discompose by business capacity
    - Decompose by subdomain
- Database
    - single DB or Shared DB
- Communication
    - API based
    - Event based
- Integration
    - API gateways
- Observablity


![](../../assets/images/HDL/micro1.png)
![](../../assets/images/HDL/micro2.png)
![](../../assets/images/HDL/micro3.png)
![](../../assets/images/HDL/micro4.png)
![](../../assets/images/HDL/micro5.png)
![](../../assets/images/HDL/micro6.png)
![](../../assets/images/HDL/micro7.png)
![](../../assets/images/HDL/micro8.png)
![](../../assets/images/HDL/micro9.png)


## System Scaling to 1 Million

![](../../assets/images/HDL/scalingSystem1.png)
![](../../assets/images/HDL/scalingSystem2.png)
![](../../assets/images/HDL/scalingSystem3.png)

## Consistent Hashing

![](../../assets/images/HDL/consitanthasing1.png)
![](../../assets/images/HDL/consistanthasing2.png)


## URL Shortner

![](../../assets/images/HDL/urlShortner1.png)
![](../../assets/images/HDL/urlShortner2.png)
![](../../assets/images/HDL/urlShortner3.png)
![](../../assets/images/HDL/urlShortner4.png)

## Back of Envelope Estimation


![](../../assets/images/HDL/boee1.png)
![](../../assets/images/HDL/boee2.png)
![](../../assets/images/HDL/boee3.png)
![](../../assets/images/HDL/boee4.png)
![](../../assets/images/HDL/boee5.png)
![](../../assets/images/HDL/boee6.png)
![](../../assets/images/HDL/boee7.png)


## Design key value DB


![](../../assets/images/HDL/designKeyValueDb1.png)
![](../../assets/images/HDL/designKeyValueDb2.png)
![](../../assets/images/HDL/designKeyValueDb3.png)
![](../../assets/images/HDL/designKeyValueDb4.png)
![](../../assets/images/HDL/designKeyValueDb5.png)
![](../../assets/images/HDL/designKeyValueDb6.png)


## Sql vs NoSql

![](../../assets/images/HDL/sqlnosql1.png)
![](../../assets/images/HDL/sqlnosql2.png)
![](../../assets/images/HDL/sqlnosql3.png)



## Proxy vs Reverse Proxy
 - What is proxy server?
 - What are its differnt types?
    - Forward proxy
    - Reverse proxy
- Proxy vs VPN
- Proxy vs LoadBalancer
- Proxy vs firewall


## [Design chat application](<../../assets/pdfs/1 Design chat application.pdf>)

## [Rate Limiter](<../../assets/pdfs/2 Rate limiter.pdf>)

## [Design Idempotent post api](<../../assets/pdfs/3 Design idempotent post api.pdf>)

## [Design High avaibliabity architecture](<../../assets/pdfs/4 Design high availability architecture .pdf>)

## [Distributed Messgin queue kfka rabbitmq](<../../assets/pdfs/5 Distributed messaging queue (Kafka ,Rabbitmq).pdf>)


## [proxy vs reverse proxy](<../../assets/pdfs/6 Proxy vs reverse proxy.pdf>)

## [Tree](<../../assets/pdfs/7 TREE.pdf>)

## AWS
- [Part 1](<../../assets/pdfs/8 Aws 1.pdf>)
- [Part 2](<../../assets/pdfs/8 Aws 2.pdf>)
- [Part 3](<../../assets/pdfs/8 Aws 3.pdf>)
- [Part 4](<../../assets/pdfs/8 Aws 4.pdf>)


## Algos
- [Base 1](<../../assets/pdfs/Alogos 1.1.pdf>)
- [Base 2](<../../assets/pdfs/Alogos 1.2.pdf>)
- [Base 3](<../../assets/pdfs/Alogos 1.3.pdf>)
- [Best and worst case](<../../assets/pdfs/Alogos 2  Best case and worst case.pdf>)
- [Divide and conquer 1](<../../assets/pdfs/Alogos 2 Divide and conquer 1.pdf>)
- [Divide and conquer 2](<../../assets/pdfs/Alogos 2 Divide and conquer 2.pdf>)
- [Divide and conquer 3](<../../assets/pdfs/Alogos 2 Divide and conquer 3.pdf>)
- [Binary search](<../../assets/pdfs/Alogos 3 Binary search.pdf>)
- [Merge Sort](<../../assets/pdfs/Alogos 4 Merge sort.pdf>)
- [Quick Sort](<../../assets/pdfs/Alogos 5 Quick sort.pdf>)







# Reference : 

https://youtube.com/playlist?list=PL6W8uoQQ2c63W58rpNFDwdrBnq5G3EfT7&si=_3pZ4xCX_dCdcBBM

https://github.com/ashishps1/awesome-system-design-resources

https://leetcode.com/discuss/post/3611301/complete-system-design-case-studies-book-3ky6/

https://leetcode.com/discuss/post/2340482/system-design-template-that-landed-me-to-53gu/
https://leetcode.com/discuss/post/2341201/object-oriented-design-template-that-lan-co46/

https://github.com/donnemartin/system-design-primer
https://www.youtube.com/@ByteByteGo