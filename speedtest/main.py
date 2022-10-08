from cProfile import run
import speedtest
import paho.mqtt.client as paho
import json
import logging

class SpeedTestRunner:

    def __send_message(self,payload):
            broker = "broker"
            topic = "application/speedtest"

            client = paho.Client(client_id="speedtest_runner")
            client.connect(broker)
            client.publish(topic, payload)

    def run(self):
        logging.info("running internet speed test")
        download,upload = self.__run_test()
        logging.info("sending mqtt message")
        self.__send_message(self.__generate_payload(download,upload))

    def __generate_payload(self,download:float, upload:float):
        payload = json.dumps({
                    "upload": upload,
                    "download": download,
                })
        return payload

    def __run_test(self):
        st = speedtest.Speedtest(secure=True)
        download_speed = "{:.2f}".format(st.download() / 1000000)
        logging.info(f"download speed is: {download_speed} Mbps")
        upload_speed = "{:.2f}".format(st.upload() / 1000000)
        logging.info(f"upload speed is: {upload_speed} Mbps")
        return (download_speed,upload_speed)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    runner = SpeedTestRunner()
    runner.run()
