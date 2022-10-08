# Internet Speed Test

<div align="center">
  
  [![GitHub](https://img.shields.io/github/license/joseph-mccarthy/internet-speed-test?style=for-the-badge)](https://github.com/joseph-mccarthy/internet-speed-test/blob/main/licence)
  [![wakatime](https://wakatime.com/badge/github/joseph-mccarthy/linternet-speed-test.svg?style=for-the-badge)](https://wakatime.com/badge/github/joseph-mccarthy/internet-speed-test)

</div>

Small python script that runs an internet speed test using the __speedtest-cli__. The intention of this script is that it's run from the __crontab__. Once the test has been completed then the results are converted from bytes to Mbps. Then the converted result is published to an mqtt topic. For this example the broker is named __broker__ and the topic is __application/speedtest__ obviously this needs to be updated to your details and additional code for authenitication.

Here is an example of the mqtt payload added to the queue:

```json
{
    "upload":"50.12",
    "download":"123.21"
}
```

## License

Copyright (c) 2022 Joseph McCarthy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

---

## Author Info

- [GitHub](https://github.com/joseph-mccarthy)
- [Website](https://joseph-mccarthy.github.io/)
