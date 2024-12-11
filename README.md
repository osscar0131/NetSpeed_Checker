## NetSpeed_Checker by osscar0131
    - Version: 0.1
    - Open Source Software Project
    - Used ChatGPT for research / coding assist

This project aims to test your network speed(Mbps) and response time.

By running the program you will download/upload a file of designated size from/to public server, namely OVH.net

Additionally, you may select a manual server URL to test it out yourself.


- TODO
    - [x] Make download_speed_test()
    #### Issue : SSL Cert Verification Error on Hetzner. Need to check each server for capability
    #### Changing plan - there's only one server(OVH.net) working for me right now.
    - [x] Error handling

    - [x] Test download_speed_test() on URLs

    - [x] Make upload_speed_test()
    - [] Test upload_speed_test()
    #### Issues expected : Many servers may not allow upload test

    - [x] Make response_time_test() (Ping / RTT)
    - [x] Test response_time_test()
    #### Make sure you use https: http may cause Error 301 (Moved Permanently)

    - [] Make server selection: Domestic / Global
    #### Changing plan - there's only one server(OVH.net) working for me right now.

    - [] Make GUI


- Servers to check
    - ## Domestic
        1. KT
        #### URL: http://speed.kt.com/
        #### download : No available testfile - site provides their own speedtester
        #### upload : 
        2. SK Broadband
        #### URL: http://myspeed.skbroadband.com/
        #### download : No available testfile - site provides their own speedtester
        #### upload : 
        3. LG U+
        #### URL: http://speed.uplus.co.kr/ftp_test/100MB.dat
        #### download : Error-404
        #### upload : 
        4. NIA
        #### URL: http://speed.nia.or.kr
        #### download : No available testfile - site provides their own speedtester
        #### upload : 
    - ## Global
        1. Hetzner
        #### URL: https://speed.hetzner.de/100MB.bin (Germany)
        #### download : SSL Cert Verification Error
        #### upload : 
        2. DigitalOcean
        #### URL1: https://speedtest-nyc1.digitalocean.com/100mb.test (New York)
        #### URL2: https://speedtest-sgp1.digitalocean.com/100mb.test (Singapore)
        #### download : Non-existent domain
        #### upload : 
        3. *OVH*
        #### URL: http://proof.ovh.net/files/100Mb.dat (France)
        #### download : Working!
        #### upload : 
        3. Cloudflare
        #### URL: https://speed.cloudflare.com/ (France)
        #### download : No available testfile - Website automatically tests net speed
        #### upload : 