class Repo(object):
    def __init__(self):
        self._entities = []

    def validateNotInRepo(self, newEntity):
        for entity in self._entities:
            if entity == newEntity:
                raise ValueError("Entity already in repo!")

    def addS(self, entity):
        self.validateNotInRepo(entity)
        self._entities.append(entity)



class FileRepo(object):
    def __init__(self, filename, readEntity, writeEntity):
        Repo.__init__(self)
        self._filename = filename
        self._readEntity = readEntity
        self._writeEntity = writeEntity

    def __readAllFromFile(self):
        self._entities = []
        with open(self._filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    entity = self._readEntity(line)
                    self._entities.append(entity)

    def __writeAllToFile(self):
        with open(self._filename, "w") as file:
            for entity in self._entities:
                file.write(self._writeEntity(entity) + "\n")

    def validateNotInRepo(self, newEntity):
        Repo.validateNotInRepo(self, newEntity)

    def addS(self, entity):
        self.__readAllFromFile()
        Repo.addS(self, entity)
        self.__writeAllToFile()