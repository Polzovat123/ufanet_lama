import pandas as pd

from ves.application.pipeline import InterfacePipeline

url_resource = None

if __name__ == '__main__':
        df = pd.DataFrame({
                'id_dialog': [1, 1, 1, 2],
                'from': ['a', 'b', 'a', 'c'],
                'to': ['b', 'a', 'b', 'd'],
                'data': ['12.01.2023', '12.01.2023', '12.01.2023', '12.01.2023'],
                'message': ['can fix?', 'yes', 'thanks', 'hi']
            })

        pipeline = InterfacePipeline(df)
        pipeline.execute()
