from prompto.store.Store import IAuditRecord


class AuditRecord(IAuditRecord):

    def asDocument(self):
        doc = dict()
        doc["dbId"] = self.dbId
        doc["metadataDbId"] = self.metadataDbId
        doc["utcTimeStamp"] = self.utcTimestamp
        doc["instanceDbId"] = self.instanceDbId
        doc["operation"] = self.operation.name
        if getattr(self, "instance", None) is not None:
            doc["instance"] = self.convertInstance(self.instance)
        return doc

    def convertInstance(self, instance):
        doc = dict()
        for name in instance.names():
            doc[name] = self.convertValue(instance.getData(name))
        return doc

    def convertValue(self, value):
        if value is None:
            return None
        else:
            return value # TODO convert to Prompto native types if required

    def matches(self, auditPredicates: dict, instancePredicates: dict) -> bool:
        if (0 if auditPredicates is None else len(auditPredicates)) + (0 if instancePredicates is None else len(instancePredicates)) == 0:
            return False
        else:
            return (auditPredicates is None or all(self.auditMatches(k, v) for k, v in auditPredicates.items())) \
                        and (instancePredicates is None or all(self.instanceMatches(k, v) for k, v in instancePredicates.items()))

    def auditMatches(self, name: str, value: object):
        return value == getattr(self, name, None)


    def instanceMatches(self, name: str, value: object):
        instance = getattr(self, "instance", None)
        return instance is not None and value == instance.getData(name)
