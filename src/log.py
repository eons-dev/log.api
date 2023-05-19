import os
import logging
import apie
from flask import request

class log(apie.Endpoint):
    def __init__(this, name="Log aggregation Endpoint"):
        super().__init__(name)

        this.supportedMethods = ['PUT']
        this.mime = 'plain/text'
        this.clobberContent = False

        this.requiredKWArgs.append('message')
        this.requiredKWArgs.append('level')
        this.requiredKWArgs.append('source')
        this.requiredKWArgs.append('timestamp')

    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return '''\
Add a log message to the log aggregator.
'''

    def Call(this):
        this.response.code = 200
        this.response.content.string = "OK"
