class Repo(object):
    def __init__(self):
        self._entities = []

    @property
    def ListOfAll(self):
        return self._entities[:]

    @ListOfAll.setter
    def ListOfAll(self, list):
        self._entities = list

    def add(self, entity):
        if entity in self._entities:
            raise ValueError("Duplicate ID!")
        self._entities.append(entity)

class FileRepo(Repo):
    def __init__(self, file, readEntity, writeEntity):
        Repo.__init__(self)
        self._file = file
        self._readEntity = readEntity
        self._writeEntity = writeEntity

    def __readAllFromFile(self):
        self._entities = []
        try:
            with open(self._file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line.strip()
                    if line != "":
                        entity = self._readEntity(line)
                        self._entities.append(entity)
        except FileNotFoundError:
            open(self._file, "x")

    def __writeAllToFile(self):
        with open(self._file, "w+") as file:
            for entity in self._entities:
                file.write(self._writeEntity(entity) + "\n")

    def add(self, entity):
        '''
        adds entity to the repo
        :param entity: given entity
        :return: the entity is added or an error is raised if duplicate ID
        '''
        self.__readAllFromFile()
        Repo.add(self, entity)
        self.__writeAllToFile()

    def initialize(self):
        self.__readAllFromFile()

class Quiz(FileRepo):
    def __init__(self, difficulty, numberOfQuestions, file, readEntity, writeEntity):
        FileRepo.__init__(self, file, readEntity, writeEntity)
        self._difficulty = difficulty
        self._numberOfQuestions = numberOfQuestions
        self._file = file
        self._entities = []
        #self._entities = [None for i in range(self._numberOfQuestions)] #the entities are questions

    @property
    def Difficulty(self):
        return self._difficulty

    @property
    def NumberOfQuestions(self):
        return self._numberOfQuestions

    @property
    def File(self):
        return self._file

    @property
    def Questions(self):
        return self._entities

    @Questions.setter
    def Questions(self, questions):
        self._entities = questions


    def updateFile(self, questionList):
        for question in questionList:
            self.add(question)