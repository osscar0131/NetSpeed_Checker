import requests
import time
import tkinter

def download_speed_test(url, chunk_size=1024):
    try:
        # HTTPS GET
        total_bytes = 0
        response = requests.get(url, stream=True)
        start_time = time.time()

        # 응답 상태 확인
        if response.status_code != 200:
            raise ValueError(f"Invalid response from server: {response.status_code}")
    
        # 응답 수신
        for chunk in response.iter_content(chunk_size=chunk_size):
            total_bytes += len(chunk)
        
        # 속도 계산(Mbps) / 응답 적절성 확인
        elapsed_time = time.time() - start_time
        if elapsed_time == 0 or total_bytes == 0:
            raise ValueError("Download failed or response size is zero.")
        speed_mbps = (total_bytes * 8) / (elapsed_time * 1_000_000)

        # 테스트 결과
        #print(f"Total downloaded: {total_bytes / (1024 * 1024):.2f} MB")
        #print(f"Elapsed time: {elapsed_time:.2f} seconds")
        #print(f"Speed: {speed_mbps:.2f} Mbps")
        return speed_mbps
    except Exception as e:
        print(f"Error: {e}")


def upload_speed_test(url, data_size_mb=10):
    try:
        # 더미 데이터를 생성
        data = b"0" * data_size_mb * 1024 * 1024  # 0000... xMB

        # HTTPS POST
        start_time = time.time()
        response = requests.post(url, data=data)
        elapsed_time = time.time() - start_time

        # 응답 코드 확인
        if response.status_code != 200:
            raise ValueError(f"Invalid response from server: {response.status_code}")
        
        if elapsed_time == 0:
            raise ValueError("Elapsed time is zero, upload failed.")

        # 속도 계산 (Mbps)
        speed_mbps = (len(data) * 8) / (elapsed_time * 1_000_000)
        #print(f"Upload size: {data_size_mb} MB")
        #print(f"Elapsed time: {elapsed_time:.2f} seconds")
        #print(f"Speed: {speed_mbps:.2f} Mbps")

        return speed_mbps
    except Exception as e:
        print(f"Error: {e}")

def response_time_test(url):
    try:
        start_time_rtt = time.time()
        rtt_response = requests.head(url)
        rtt = (time.time() - start_time_rtt) * 1000  # ms

        if rtt_response.status_code != 200:
            raise ValueError(f"Invalid response from server: {rtt_response.status_code}")

        #print(f"Ping: {rtt:.2f} ms")
        return rtt
    except Exception as e:
        print(f"Error: {e}")


def start_download_test():
    speed = download_speed_test(test_url)
    result_text.insert(tkinter.END, f"Speed: {speed:.2f} Mbps" + "\n")

def start_upload_test():
    speed = upload_speed_test(test_url)
    result_text.insert(tkinter.END, f"Speed: {speed:.2f} Mbps" + "\n")

def start_response_test():
    rtt = response_time_test(test_url)
    result_text.insert(tkinter.END, f"Ping: {rtt:.2f} ms" + "\n")


if __name__ == "__main__":
    global test_url
    test_url = "https://proof.ovh.net/files/10Mb.dat"

    #download_speed_test(url)
    #upload_speed_test(url)
    #response_time_test("https://proof.ovh.net")

    # Main window
    window = tkinter.Tk()
    window.title("NetSpeed_Checker 0.1")
    window.geometry("800x600+100+100")
    window.resizable(False, False)



    # Test buttons
    button_download_speed_test = tkinter.Button(window, overrelief="solid",
                                                width=40, command=start_download_test,
                                                text="다운로드 속도 측정")
    button_upload_speed_test = tkinter.Button(window, overrelief="solid",
                                                width=40, command=start_upload_test,
                                                text="업로드 속도 측정")
    button_response_time_test = tkinter.Button(window, overrelief="solid",
                                                width=40, command=start_response_test,
                                                text="Ping 측정")
    
    # Result text
    result_text = tkinter.Text(window, wrap="word", height=20, width=70)
    
    
    
    # Place all labels
    button_download_speed_test.place(relx=0.32, rely=0.1)
    button_upload_speed_test.place(relx=0.32, rely=0.17)
    button_response_time_test.place(relx=0.32, rely=0.24)
    result_text.place(relx = 0.19, rely=0.5)


    # Start main window
    window.mainloop()

    pass