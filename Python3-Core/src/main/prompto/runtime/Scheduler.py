from threading import Timer
from datetime import datetime

from prompto.runtime.ApplicationContext import ApplicationContext


class Scheduler(object):

    timers = dict()
    counter = 0

    @staticmethod
    def nextJobId():
        Scheduler.counter = Scheduler.counter + 1
        return Scheduler.counter


    @staticmethod
    def schedule(method, executeAt, repeatEvery, jobName):
        jobId = Scheduler.nextJobId()
        def task():
            if repeatEvery is not None:
                interval = repeatEvery.totalMilliseconds() / 1000
                Scheduler.timers[jobId] = Timer(interval, task)
                Scheduler.timers[jobId].start()
            try:
                method.interpret(ApplicationContext.get())
            finally:
                if repeatEvery is None:
                    del Scheduler.timers[jobId]
        interval = executeAt.timestamp() - datetime.utcnow().timestamp()
        if interval < 0:
            interval = 0
        Scheduler.timers[jobId] = Timer(interval, task)
        Scheduler.timers[jobId].start()
        return jobId


    @staticmethod
    def cancel(jobId):
        timer = Scheduler.timers.get(jobId, None)
        if timer is not None:
            timer.cancel()
            del Scheduler.timers[jobId]
        else:
            pass # TODO log or throw
