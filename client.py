import os
import asyncio

import aiofiles
from datetime import timedelta
from telethon import TelegramClient
from dotenv import load_dotenv
load_dotenv()


class SendMessagesClient(TelegramClient):
    """
    A class to handle sending messages to group members using TelegramClient.
    """

    def set_delay(self) -> None:
        """
        Set the delay between sending messages.

        Asks the user for input to set the delay between messages in seconds.
        """
        while True:
            try:
                message_delay = int(input("Enter message delay in seconds: "))
                if message_delay < 0:
                    raise ValueError()
                break
            except ValueError or message_delay < 0:
                print("Time delay should be an integer greater than 0")
        self.message_delay = timedelta(seconds=message_delay)

    async def _get_group_name(self) -> str:
        """
        Retrieve the name of the group from a text file.

        Returns:
            str: The name of the group to send messages to.
        """
        async with aiofiles.open(
            "groups.txt",
            "r",
            encoding="UTF-8"
        ) as groups_file:
            group_name = await groups_file.readline()
        return group_name

    async def _get_message_text(self) -> str:
        async with aiofiles.open(
            "text.txt",
            "r",
            encoding="UTF-8"
        ) as groups_file:
            message_text = await groups_file.readline()
        return message_text

    async def _send_messages_to_group_members(
        self,
        group_name: str,
        text: str
    ) -> None:
        """
        Send messages to all group members.

        Args:
            group_name (str): The name of the group to send messages to.
        """
        async for participant in self.iter_participants(
            group_name
        ):
            await self.send_message(
                participant.id,
                message=text,
                schedule=self.message_delay
            )

    async def start_sending(self):
        """
        Start sending messages to group members.
        """
        group_name_task = self._get_group_name()
        message_text_task = self._get_message_text()

        group_name, message_text = await asyncio.gather(
            group_name_task,
            message_text_task,
        )

        self.set_delay()

        await self._send_messages_to_group_members(
            group_name=group_name,
            text=message_text
        )


if __name__ == "__main__":
    client = SendMessagesClient(
        "session",
        api_id=os.getenv("API_ID"),
        api_hash=os.getenv("API_HASH")
    )
    with client:
        client.loop.run_until_complete(
            client.start_sending()
        )
