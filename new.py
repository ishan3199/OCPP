import asyncio
import logging
import websockets
from ocpp.v16 import call
from ocpp.v16.enums import AuthorizationStatus
from ocpp.v16 import ChargePoint as cp

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):

   async def authorize(self):
       r=call.AuthorizePayload(id_tag="test_cp2")
       response1 = await self.call(r)

       if response1.id_tag_info['status'] == 'Accepted' :
           print("authorized.")
       else:
           print("Not Authorized")



   async def send_boot_notification(self):
       request = call.BootNotificationPayload(
           charge_point_model="Optimus", charge_point_vendor="The Mobility"
       )
       response = await self.call(request)

       if response.status == 'Accepted':
           print("Boot confirmed.")


async def main():
   async with websockets.connect(
       'ws://localhost:8009/CP_3',
        subprotocols=['ocpp1.6']
   ) as ws:

       cp = ChargePoint('CP_3', ws)

       await asyncio.gather(cp.start(), cp.authorize(), cp.send_boot_notification())


if __name__ == '__main__':
   asyncio.run(main())
