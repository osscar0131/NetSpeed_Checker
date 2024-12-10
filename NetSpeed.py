import requests
import time

def download_speed_test(url, chunk_size=1024):
    try:
        total_bytes = 0
        # HTTPS GET
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
        print(f"Total downloaded: {total_bytes / (1024 * 1024):.2f} MB")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Speed: {speed_mbps:.2f} Mbps")
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
        print(f"Upload size: {data_size_mb} MB")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Speed: {speed_mbps:.2f} Mbps")

        return speed_mbps
    except Exception as e:
        print(f"Error: {e}")






if __name__ == "__main__":
    #url = "http://proof.ovh.net/files/10Mb.dat"
    #download_speed_test(url)
    #upload_speed_test(url="")
    pass