

class BuildPrompt:
    def build(self, type_task='asking'):
        if type_task == 'ask':
            return 'and you need to answer to question: '
        if type_task == 'decribe':
            return 'and you need to describe to question: '
        else:
            raise 'Incorrect params to build schema'
