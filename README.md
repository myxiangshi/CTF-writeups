# writeups-ctf

😄利用CTF入门安全研究，在此以CTF样本为例，记录各种漏洞利用。

🚩我们的[CTF战队](https://ctftime.org/team/152403)

## 目录

- [pwn](#pwn)
- [web](#web)
- [misc](#misc)

## <a id="pwn">pwn</a>

#### 入门

[栈溢出](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/%E6%A0%88%E6%BA%A2%E5%87%BA.pdf)

[使用ROPEmporium学习ROP技术](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/ROPEmporium/%E4%BD%BF%E7%94%A8ROPEmporium%E5%AD%A6%E4%B9%A0ROP%E6%8A%80%E6%9C%AF.pdf)

[格式化字符串](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2.pdf)

[整数溢出](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/%E6%95%B4%E6%95%B0%E6%BA%A2%E5%87%BA.pdf)

[CTF Pwn 板块精选贴分类索引](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/CTF%E3%80%8EPwn%E3%80%8F%E7%89%88%E5%9D%97%E7%B2%BE%E9%80%89%E5%B8%96%E5%88%86%E7%B1%BB%E7%B4%A2%E5%BC%95.pdf)

[Q版缓冲区溢出教程](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/Q%E7%89%88%E7%BC%93%E5%86%B2%E5%8C%BA%E6%BA%A2%E5%87%BA%E6%95%99%E7%A8%8B.pdf)

[i春秋月刊第6期：Linux Pwn入门教程](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/i%E6%98%A5%E7%A7%8B%E6%9C%88%E5%88%8A%E7%AC%AC6%E6%9C%9F%EF%BC%9ALinux%20Pwn%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B.pdf)

[通过ELF动态装载机制进行漏洞利用](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/%E9%80%9A%E8%BF%87ELF%E5%8A%A8%E6%80%81%E8%A3%85%E8%BD%BD%E6%9C%BA%E5%88%B6%E8%BF%9B%E8%A1%8C%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8.pdf)

[i春秋月刊第7期：Android逆向](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/i%E6%98%A5%E7%A7%8B%E6%9C%88%E5%88%8A%E7%AC%AC7%E6%9C%9F%EF%BC%9AAndroid%E9%80%86%E5%90%91.pdf)

[Fuzzing Android & iOS](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/Fuzzing%20Android%20%26%20iOS.pdf)

[glibc内存分配源码分析](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/glibc%E5%86%85%E5%AD%98%E5%88%86%E9%85%8D%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90.pdf)

[glibc内存管理ptmalloc源代码分析](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/glibc%E5%86%85%E5%AD%98%E7%AE%A1%E7%90%86ptmalloc%E6%BA%90%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90.pdf)

[xdef2019_Linux操作系统内核的攻击和防护演化](https://github.com/ByeRose/writeups-ctf/blob/main/pwn/collect/xdef2019_Linux%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%86%85%E6%A0%B8%E7%9A%84%E6%94%BB%E5%87%BB%E5%92%8C%E9%98%B2%E6%8A%A4%E6%BC%94%E5%8C%96.pdf)

#### 实例

|                                                              |      |                        |
| ------------------------------------------------------------ | ---- | ---------------------- |
| [ciscn_2019_n_1](https://github.com/ByeRose/writeups-ctf/tree/main/pwn/ciscn_2019_n_1) | 栈   | 栈溢出                 |
| [when_did_you_born](https://github.com/ByeRose/writeups-adworld/blob/main/pwn/%5B%E6%A0%88%E6%BA%A2%E5%87%BA%5Dwhen_did_you_born%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | 栈   | 栈溢出                 |
| [hello_pwn](https://github.com/ByeRose/writeups-adworld/blob/main/pwn/%5B%E6%A0%88%E6%BA%A2%E5%87%BA%5Dhello_pwn%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | 栈   | 栈溢出                 |
| [guess_num](https://github.com/ByeRose/writeups-adworld/blob/main/pwn/%5B%E6%A0%88%E6%BA%A2%E5%87%BA%5Dguess_num%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | 栈   | 栈溢出                 |
| [goodluck](https://github.com/ByeRose/writeups-ctf/tree/main/pwn/uiuctf2017_goodluck) | 栈   | 格式化字符串           |
| [cgpwn2](https://github.com/ByeRose/writeups-adworld/blob/main/pwn/%5Bret2sys%5Dcgpwn2%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | 栈   | 栈溢出; ret2text       |
| [rip](https://github.com/ByeRose/writeups-ctf/tree/main/pwn/buuctf_rip) | 栈   | 栈溢出; ret2text       |
| [warmup](https://github.com/ByeRose/writeups-ctf/tree/main/pwn/csaw_2016_warmup) | 栈   | 栈溢出; ret2text       |
| [pwn1](https://github.com/ByeRose/writeups-ctf/tree/main/pwn/sctf2016_pwn1) | 栈   | 栈溢出; ret2text       |
| [ciscn_2019_c_1](https://github.com/ByeRose/writeups-ctf/tree/main/pwn/ciscn_2019_c_1) | 栈   | 栈溢出; ret2libc       |
| [level3](https://github.com/ByeRose/writeups-adworld/blob/main/pwn/%5Bret2libc%5Dlevel3%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%20.pdf) | 栈   | 栈溢出; ret2libc       |
| [pwn3](https://github.com/ByeRose/writeups-ctf/tree/main/pwn/cctf2016_pwn3) | 栈   | 格式化字符串; ret2libc |



---



## <a id="web">web</a>

#### 入门

[i春秋半月刊第2期：代码审计]()

[i春秋半月刊第3期：代码审计]()

[i春秋半月刊第4期：SQL注入]()

[i春秋月刊第5期：进击的XSS]()

#### 实例



---



## <a id="misc">misc</a>

>  [攻防世界](https://adworld.xctf.org.cn/)MISC区大合集

#### 入门

- [常见文件结构](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%E5%B8%B8%E8%A7%81%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84.md)

- [信息搜集技术](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%E4%BF%A1%E6%81%AF%E6%90%9C%E9%9B%86%E6%8A%80%E6%9C%AF.pdf)

- [编码分析](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%E7%BC%96%E7%A0%81%E5%88%86%E6%9E%90.pdf)

- [图片分析](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%E5%9B%BE%E7%89%87%E5%88%86%E6%9E%90.pdf)

- [音频隐写](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%E9%9F%B3%E9%A2%91%E9%9A%90%E5%86%99%20.pdf)

- [流量包分析](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%E6%B5%81%E9%87%8F%E5%8C%85%E5%88%86%E6%9E%90.pdf)

- [压缩包分析](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%E5%8E%8B%E7%BC%A9%E5%8C%85%E5%88%86%E6%9E%90.pdf)

- [磁盘内存&pyc](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%E7%A3%81%E7%9B%98%E5%86%85%E5%AD%98%26pyc.pdf)

#### 实例

|                                                              |                                                              |                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| :muscle:**basic**                                            |                                                              |                                                              |                                                              |
| [this_is_flag](https://blog.csdn.net/weixin_44604541/article/details/109058125) | [pdf](https://blog.csdn.net/weixin_44604541/article/details/109058125) | [如来十三掌](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E4%B8%8E%E4%BD%9B%E8%AE%BA%E7%A6%85%2CRot13%2CBase64%5D%E5%A6%82%E6%9D%A5%E5%8D%81%E4%B8%89%E6%8E%8C%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [give_you_flag](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bgif%2CQRcode%5Dgive_you_flag%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [坚持60s](https://blog.csdn.net/weixin_44604541/article/details/109058125) | [gif](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bascii%2C%E8%84%9A%E6%9C%AC%5Dgif%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [掀桌子](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bascii%2C%E8%84%9A%E6%9C%AC%5D%E6%8E%80%E6%A1%8C%E5%AD%90%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [ext3](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%5Dext3%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [stegano](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bpdf%2Cmorse%5Dstegano%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [SimpleRAR](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5BRAR%2Cgif%2CQRcode%5DSimpleRAR%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [base64stego](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5BBase64%E9%9A%90%E5%86%99%5Dbase64stego%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [功夫再高也怕菜刀](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bwireshark%2Cforemost%5D%E5%8A%9F%E5%A4%AB%E5%86%8D%E9%AB%98%E4%B9%9F%E6%80%95%E8%8F%9C%E5%88%80%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
|                                                              |                                                              |                                                              |                                                              |
| :sob:advance                                                 |                                                              |                                                              |                                                              |
| [base64÷4](https://blog.csdn.net/fool_best/article/details/104176814) | [wireshark-1](https://blog.csdn.net/fool_best/article/details/104136590) | [pure_color](https://blog.csdn.net/gongjingege/article/details/108035013) | [Aesop_secret](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5BAES%2Cps%5DAesop_secret%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [a_good_idea](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5BPIL%2Cbinwalk%5Da_good_idea%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Training-Stegano-1](https://blog.csdn.net/qq_43312665/article/details/104209475) | [can_has_stdio?](https://blog.csdn.net/weixin_47717433/article/details/108300271) | [János-the-Ripper](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E7%88%86%E7%A0%B4%2Czip%5DJ%C3%A1nos-the-Ripper%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [Test-flag-please-ignore](https://blog.csdn.net/harry_c/article/details/99615704) | [hit-the-core](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E5%AD%97%E7%AC%A6%E4%B8%B2%5Dhit-the-core%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [快乐游戏题](https://blog.csdn.net/gongjingege/article/details/108169629) | [Banmabanma](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%9D%A1%E5%BD%A2%E7%A0%81%5DBanmabanma%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [easycap](https://blog.csdn.net/harry_c/article/details/99686762) | [reverseMe](https://blog.csdn.net/gongjingege/article/details/108173174) | [stage1](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bpyc%5Dstage1%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Hear-with-your-Eyes](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E9%9F%B3%E9%A2%91%5DHear-with-your-Eyes%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [What-is-this](https://blog.csdn.net/harry_c/article/details/99404172) | [再见李华](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bmd5%2Cforemost%5D%E5%86%8D%E8%A7%81%E6%9D%8E%E5%8D%8E%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [embarrass](https://blog.csdn.net/gongjingege/article/details/108034693) | [神奇的Modbus](https://blog.csdn.net/qq_46927150/article/details/105880372) |
| [MISCall](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bgit%5DMISCall%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Get-the-key.txt](https://blog.csdn.net/weixin_43877387/article/details/103133884) | [Reverse-it](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bjpg%5DReverse-it%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [something_in_image](https://blog.csdn.net/weixin_45556441/article/details/109864134) |
| [打野](https://blog.csdn.net/qq_43312665/article/details/104262278) | [我们的秘密是绿色的](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%A0%85%E6%A0%8F%EF%BC%8C%E5%87%AF%E6%92%92%EF%BC%8C%E4%BC%AA%E5%8A%A0%E5%AF%86%EF%BC%8C%E6%98%8E%E6%96%87%E6%94%BB%E5%87%BBour%20secret%5D%E6%88%91%E4%BB%AC%E7%9A%84%E7%A7%98%E5%AF%86%E6%98%AF%E7%BB%BF%E8%89%B2%E7%9A%84_%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [倒立屋](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bzsteg%5D%E5%80%92%E7%AB%8B%E5%B1%8B%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [小小的PDF](https://blog.csdn.net/weixin_44604541/article/details/109840744) |
| [2017_Dating_in_Singapore](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%97%A5%E5%8E%86%5D2017_Dating_in_Singapore%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [simple_transfer](https://blog.csdn.net/RuoLi_s/article/details/109630540) | [Erik-Baleog-and-Olaf](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E5%83%8F%E7%B4%A0%2C%E4%BA%8C%E7%BB%B4%E7%A0%81%5DErik-Baleog-and-Olaf%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [labour](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bgpx%5Dlabour%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [glance-50](https://blog.csdn.net/harry_c/article/details/99862218) | [Ditf](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bforemost%2Cpacpng%2Cbase64%2CHTTP%2C%E5%88%86%E8%BE%A8%E7%8E%87%5DDitf%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [misc_pic_again](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%AD%A3%E5%88%99%EF%BC%8C%E5%9B%BE%E7%89%87%E9%9A%90%E5%86%99%5Dmisc_pic_again%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [适合作为桌面](https://blog.csdn.net/YUK_103/article/details/103223552) |
| [心仪的公司](https://blog.csdn.net/weixin_44604541/article/details/109451538) | [Miscellaneous-200](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E5%83%8F%E7%B4%A0%5DMiscellaneous-200%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Hidden-Message](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bpcap%2Cascii%5DHidden-Message%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Recover-Deleted-File](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%5DRecover-Deleted-File%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [red_green](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E5%9B%BE%E7%89%87%E9%9A%90%E5%86%99%5Dred_green%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [funny_video](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E8%A7%86%E9%A2%91%EF%BC%8C%E9%9F%B3%E9%A2%91%5Dfunny_video%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [normal_png](https://blog.csdn.net/weixin_44604541/article/details/110870849) | [很普通的数独](https://blog.csdn.net/weixin_44604541/article/details/109506510) |
| [很普通的Disco](https://blog.csdn.net/weixin_44604541/article/details/109534557) | [就在其中](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5BRSA%2Cpcapng%5D%E5%B0%B1%E5%9C%A8%E5%85%B6%E4%B8%AD%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [肥宅快乐题](https://blog.csdn.net/weixin_44604541/article/details/109543998) | [miscmisc](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E5%9B%BE%E7%89%87%E9%9A%90%E5%86%99%2Cword%2C%E6%98%8E%E6%96%87%E6%94%BB%E5%87%BB%5Dmiscmisc%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [flag_universe](https://blog.csdn.net/weixin_44604541/article/details/109570910) | [奇怪的TTL字段](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E8%87%AA%E5%8A%A8%E5%AF%86%E9%92%A5%E5%AF%86%E7%A0%81%2C%E4%BA%8C%E8%BF%9B%E5%88%B6%E9%9A%90%E5%86%99%5D%E5%A5%87%E6%80%AA%E7%9A%84TTL%E5%AD%97%E6%AE%B5%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [2-1](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5BCRC%E7%88%86%E7%A0%B4%5D2-1%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [3-11](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5BBase64%E5%9B%BE%E7%89%87%EF%BC%8CLSB%5D3-11%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [互相伤害!!!](https://blog.csdn.net/weixin_44604541/article/details/109717353) | [签到题](https://blog.csdn.net/Guapichen/article/details/107980578) | [隐藏的信息](https://blog.csdn.net/weixin_44604541/article/details/109770572) | [Become_a_Rockstar](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E5%8F%A6%E7%B1%BB%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%5DBecome_a_Rockstar%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [intoU](https://blog.csdn.net/weixin_44604541/article/details/111059531) | [Cephalopod](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%B5%81%E9%87%8F%5DCephalopod%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Excaliflag](https://blog.csdn.net/weixin_44604541/article/details/109964193) | [Just-No-One](https://blog.csdn.net/weixin_44604541/article/details/110742990) |
| [信号不好先挂了](https://blog.csdn.net/weixin_44604541/article/details/110062566) | [黄金六年](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E8%A7%86%E9%A2%91%E5%B8%A7%2Crar%5D%E9%BB%84%E9%87%91%E5%85%AD%E5%B9%B4%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [打开电动车](https://fishpond.blog.csdn.net/article/details/111193409) | [hong](https://blog.csdn.net/weixin_44604541/article/details/111247886) |
| [3-1](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%B5%81%E9%87%8F%E5%8C%85%2CBase64%5D3-1%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [4-1](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E7%9B%B2%E6%B0%B4%E5%8D%B0%5D4-1%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [4-2](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E8%AF%8D%E9%A2%91%E5%88%86%E6%9E%90%5D4-2%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [5-1](https://blog.csdn.net/weixin_44604541/article/details/110378348) |
| [low](https://blog.csdn.net/weixin_44604541/article/details/110428984) | [misc1](https://blog.csdn.net/weixin_44604541/article/details/110478409) | [latlong](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E6%97%A0%E7%BA%BF%E7%94%B5%5Dlatlong%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Miscellaneous-300](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E7%88%86%E7%A0%B4%2C%E9%A2%91%E8%B0%B1%E5%9B%BE%5DMiscellaneous-300%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| [双色块](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5BASCII%2CDES%E8%A7%A3%E5%AF%86%5D%E5%8F%8C%E8%89%B2%E5%9D%97%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Py-Py-Py](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bpyc%E9%9A%90%E5%86%99%5DPy-Py-Py%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [warmup](https://blog.csdn.net/weixin_44604541/article/details/109566704) | [传感器1](https://blog.csdn.net/weixin_44604541/article/details/109614250) |
|                                                              |                                                              |                                                              |                                                              |
| [qr-easy](https://yous.be/2014/12/07/seccon-ctf-2014-qr-easy-write-up/) | [halo](https://blog.csdn.net/weixin_44604541/article/details/111737216) | [saleae](https://m09ic.top/posts/41838/)                     | [mysql](https://fishpond.blog.csdn.net/article/details/111109033) |
| [Disk](https://blog.csdn.net/lycnjupt/article/details/84237825) | [A-Weird-C-Program](https://blog.csdn.net/weixin_44604541/article/details/112402771) | [picture2](https://blog.csdn.net/weixin_44604541/article/details/111311012) | [test.pyc](https://blog.csdn.net/weixin_44604541/article/details/111404198) |
| [Avatar](https://blog.csdn.net/weixin_44604541/article/details/111473759) | [侧信道初探](https://blog.csdn.net/weixin_44604541/article/details/111513482) | [Keyword](https://fishpond.blog.csdn.net/article/details/111676599) | [clemency](https://blog.csdn.net/xuandao_ahfengren/article/details/106428165) |
| [MulTzor](https://blog.csdn.net/qq_35713009/article/details/89340976) | [Keyes_secret](https://blog.csdn.net/weixin_44604541/article/details/112005839) | [message](https://blog.csdn.net/weixin_44604541/article/details/112062209) | [arrdeepee](https://nandynarwhals.org/hitbgsec2017-arrdeepee/) |
| [regexpire](https://eugenekolo.com/blog/csaw-qual-ctf-2016/#regexpire) | [恶臭的数据包](https://blog.csdn.net/weixin_44604541/article/details/112235777) | [crc](https://blog.csdn.net/weixin_44604541/article/details/112356639) | [challenge_how_many_Vigenère](https://blog.csdn.net/weixin_44604541/article/details/113558114) |
| [神奇的压缩文件](https://blog.csdn.net/weixin_44604541/article/details/112427198) | [pyHAHA](https://blog.csdn.net/weixin_44604541/article/details/112468128) | [北京地铁](https://blog.csdn.net/weixin_44604541/article/details/112785198) | [wireshark](https://fishpond.blog.csdn.net/article/details/112862469) |
| [picture3](https://blog.csdn.net/xuandao_ahfengren/article/details/106428165) | [7-2](https://github.com/susers/Writeups/blob/master/2017/WDCTF-finals/Misc/7-2/Write-up.md) | [ewm](https://blog.csdn.net/weixin_44604541/article/details/112955064) | [refrain](https://blog.bushwhackers.ru/0ctf-2019-quals-refrain/) |
| [Mysterious-GIF](https://blog.csdn.net/weixin_44604541/article/details/113252338) | [4433](https://fishpond.blog.csdn.net/article/details/113529718) | [Run1](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bpython%E6%B2%99%E7%AE%B1%E9%80%83%E9%80%B8%5DRun1%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [NdisBackDoor](https://www.jianshu.com/p/04ef45f4b243)       |
| [Run](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bpython%E6%B2%99%E7%AE%B1%E9%80%83%E9%80%B8%5DRun1%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [流量分析](https://blog.csdn.net/weixin_44604541/article/details/113603748) | [传感器2](https://blog.csdn.net/weixin_44604541/article/details/113642842) | [Russian-zips](https://blog.csdn.net/weixin_44604541/article/details/113741829) |
| [the_golden_gate](https://github.com/ctfs/write-ups-2014/tree/master/seccon-ctf-2014/the-golden-gate) | [opm-3](https://github.com/p4-team/ctf/tree/master/2016-03-12-0ctf/opm) | [Baby_enc](https://kataware.hatenablog.jp/entry/2017/05/22/174953) | [Unknown-format](https://duksctf.github.io/2017/02/04/ALEXCTF2017-Unknown-Forat.html) |
| [Make-similar](https://github.com/ctfs/write-ups-2014/tree/master/olympic-ctf-2014/make-similar) | [Pixel-Princess](https://github.com/ctfs/write-ups-2014/tree/master/ectf-2014/pixel-princess) | [Hidden_secret](https://blog.csdn.net/zippo1234/article/details/109595185) | [NdisBackDoor1](https://www.jianshu.com/p/04ef45f4b243)      |
| [picture](https://h3110w0r1d.com/archives/67/)               | [要啥有啥](https://l-team.org/archives/lctf2016_wp_3.html)   | [disordered_jpg](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E5%AD%97%E8%8A%82%5Ddisordered_jpg%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [神秘的交易](https://github.com/EmpireCTF/empirectf/tree/master/writeups/2018-06-19-SCTF#434-misc--%E7%A5%9E%E7%A7%98%E7%9A%84%E4%BA%A4%E6%98%93) |
| [secret_in_the_center](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5Bzip%E4%BF%AE%E5%A4%8D%5Dsecret_in_the_center%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) | [Noise](https://www.xctf.org.cn/library/details/8723e039db0164e2f7345a12d2edd2a5e800adf7/) | [picture1](https://www.xctf.org.cn/library/details/8723e039db0164e2f7345a12d2edd2a5e800adf7/) | [traffic1](https://blog.csdn.net/mutou990/article/details/108248461) |
| [misc2](https://blog.csdn.net/pigredfive/article/details/103301138) | [Flying_High](https://nandynarwhals.org/hitbgsec2017-flyinghigh/) | [santa-walks-into-a-bar](https://ph03nix.club/2016/12/27/3dsctf-2016-misc100-santa-walks-into-a-bar.html) | [LooL](https://github.com/ctfs/write-ups-2014/tree/master/d-ctf-2014/misc-300) |
| [Usb-probing](https://vincentkool.github.io/2017-AlexCTF-Fore3/) | [Hidden Write](https://www.cnblogs.com/tr1ple/p/9986587.html) | [happy_puzzle](https://nikoeurus.github.io/2019/10/28/UNCTF/#happy-puzzle%EF%BC%88800-points%EF%BC%89) | [摩斯电码](https://github.com/ByeRose/writeups-ctf/blob/main/misc/%5B%E9%9F%B3%E9%A2%91%5D%E6%91%A9%E6%96%AF%E7%94%B5%E7%A0%81%20%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C.pdf) |
| *Blocks*                                                     | [3-2](https://chybeta.github.io/2017/09/16/%E9%97%AE%E9%BC%8E%E6%9D%AF-CTF-writeup/) | [traffic](https://github.com/susers/Writeups/tree/master/2017/%E5%8E%A6%E9%97%A8%E9%82%80%E8%AF%B7%E8%B5%9B/Misc/traffic) | [第四扩展FS](https://www.cnblogs.com/kagari/p/8889412.html)  |
| [玩具车](https://my.oschina.net/u/4403673/blog/3345410)      | *godwave*                                                    | [memory_forensics](https://wooy0ung.github.io/writeup/2018/05/01/ciscn-2018-memory-forensics/) | [寻找入侵者](https://lanvnal.com/2018/04/29/CISCN2018-WP/#toc-heading-11) |
| [文件分析](https://cloud.tencent.com/developer/article/1078231) | [Whisper](https://www.sqlsec.com/2018/01/ctfimg.html#toc-heading-17) | [联盟决策大会](https://www.anquanke.com/post/id/178392)      | [我萌吗](https://www.codercto.com/a/3957.html)               |
| *Wiretapped*                                                 | *benefit*                                                    | *jpg*                                                        | [memory_forensics1](https://wooy0ung.github.io/writeup/2018/05/01/ciscn-2018-memory-forensics/) |

