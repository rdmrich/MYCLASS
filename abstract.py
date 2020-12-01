from abc import ABC, abstractmethod


# abstract classes
class pc(ABC):
    @abstractmethod
    def process(self):
        pass


class laptop(pc):
    def process(self):
        print('running')


class programmer:
    def debug(self, com):
        print('debugging')
        com.proccess()


com1 = laptop()

#com = pc()
#com.process()
pro = programmer()
pro.debug(com1)


