import speedtest
import paho.mqtt.client as paho
import json
import logging

def send_message(payload):
        broker = "broker"
        topic = "application/speedtest"

        client = paho.Client(client_id="speedtest_runner")
        client.connect(broker)
        client.publish(topic, payload)

def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("running internet speed test")
    download,upload = run_test()
    logging.info("sending mqtt message")
    send_message(generate_payload(download,upload))

def generate_payload(download:float, upload:float):
    payload = json.dumps({
                "upload": upload,
                "download": download,
            })
    return payload

def run_test():
    st = speedtest.Speedtest(secure=True)
    download_speed = "{:.2f}".format(st.download() / 1000000)
    logging.info(f"download speed is: {download_speed} Mbps")
    upload_speed = "{:.2f}".format(st.upload() / 1000000)
    logging.info(f"upload speed is: {upload_speed} Mbps")
    return (download_speed,upload_speed)

if __name__ == "__main__":
    main()
