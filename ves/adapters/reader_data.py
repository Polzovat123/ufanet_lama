import pandas as pd
import numpy as np

from ves.entity.dialog import Dialog
from ves.entity.message import Message


class InterfaceReaderDialog:
    def __init__(self, resource):
        self.dialogs = []
        resource.groupby(['id_dialog'], group_keys=False).apply(
            lambda x: self._parse_dialog(x)
        )

    def _parse_dialog(self, dialog):
        client = dialog.values[0][1]
        service = dialog.values[0][2]

        dialog_ans = Dialog(client, service)
        for row in dialog.values:
            print(row)
            msg = Message(row[3], row[4])
            dialog_ans.add_message(msg)

        self.dialogs.append(dialog_ans)


if __name__ == '__main__':
    df = pd.DataFrame({
        'id_dialog': [1, 1, 1, 2],
        'from': ['a', 'b', 'a', 'c'],
        'to': ['b', 'a', 'b', 'd'],
        'data': ['12.01.2023', '12.01.2023', '12.01.2023', '12.01.2023'],
        'message': ['can fix?', 'yes', 'thanks', 'hi']
    })

    parser = InterfaceReaderDialog(df)
    print(len(parser.dialogs))